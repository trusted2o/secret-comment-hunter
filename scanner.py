import os
import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from tqdm import tqdm

HEADERS = {'User-Agent': 'Mozilla/5.0'}

SUSPICIOUS_PATTERNS = [
    r"TODO",
    r"FIXME",
    r"HACK",
    r"BUG",
    r"NOTE",
    r"pass(word)?\s*=\s*['\"]?[\w\d@#$%^&+=!]{4,}['\"]?",
    r"api[-_]?key\s*[:=]\s*['\"]?[A-Za-z0-9\-_]{16,}['\"]?",
    r"secret\s*[:=]\s*['\"]?[A-Za-z0-9\-_]{8,}['\"]?",
    r"slack_token\s*[:=]\s*['\"]?xox[baprs]-[A-Za-z0-9\-]+['\"]?",
    r"aws(.{0,10})?(key|secret|token)['\"]?[:=]\s*['\"][A-Za-z0-9\/+=]{20,}['\"]?",
]

COMMON_EXTENSIONS = [".js", ".json", ".env", ".yml", ".xml", ".php"]

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all("script", src=True):
        links.add(requests.compat.urljoin(base_url, tag['src']))
    for tag in soup.find_all("a", href=True):
        href = tag['href']
        if any(href.endswith(ext) for ext in COMMON_EXTENSIONS):
            links.add(requests.compat.urljoin(base_url, href))
    return list(links)

def scan_file(url):
    try:
        res = requests.get(url, timeout=10, headers=HEADERS)
        if res.status_code == 200:
            matches = []
            for pattern in SUSPICIOUS_PATTERNS:
                for match in re.findall(pattern, res.text, re.IGNORECASE):
                    matches.append((pattern, match))
            return matches
    except:
        pass
    return []

def scan_target(target, output_dir):
    try:
        response = requests.get(target, timeout=10, headers=HEADERS)
        response.raise_for_status()
        links = extract_links(response.text, target)
        print(f"[+] Total JS/related links found: {len(links)}")

        # Save JS file URLs
        js_files_path = os.path.join(output_dir, "js_files.txt")
        with open(js_files_path, "w", encoding="utf-8") as f:
            for link in links:
                f.write(link + "\n")

        # Scan files for suspicious comments/secrets
        suspicious_path = os.path.join(output_dir, "secrets_found.txt")
        comments_path = os.path.join(output_dir, "js_comments.txt")
        total_suspicious = 0

        with open(suspicious_path, "w", encoding="utf-8") as suspicious_file, \
             open(comments_path, "w", encoding="utf-8") as comments_file:

            for link in tqdm(links, desc="Scanning files"):
                findings = scan_file(link)
                if findings:
                    for pattern, match in findings:
                        suspicious_file.write(f"{link} | Pattern: {pattern} | Match: {match}\n")
                        total_suspicious += 1
                else:
                    comments_file.write(f"{link} - No suspicious comments found.\n")

        print(f"[✓] Suspicious findings: {total_suspicious}")
        print(f"[✓] Saved secrets to {suspicious_path}")
        print(f"[✓] Saved comments to {comments_path}")

    except requests.RequestException as e:
        print(f"[!] Error accessing target: {e}")
