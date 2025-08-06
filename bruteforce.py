import os
import requests

HEADERS = {'User-Agent': 'Mozilla/5.0'}

COMMON_PATHS = [
    "/.env",
    "/.git/config",
    "/config.json",
    "/credentials.json",
    "/firebase.json",
    "/docker-compose.yml",
    "/admin",
    "/login",
    "/backup",
    "/backup.zip",
]

def brute_force_paths(target, output_dir):
    print("\n[*] Starting path bruteforce...")

    found_paths_file = os.path.join(output_dir, "path_bruteforce.txt")

    with open(found_paths_file, "w", encoding="utf-8") as f:
        for path in COMMON_PATHS:
            url = requests.compat.urljoin(target, path)
            try:
                r = requests.get(url, headers=HEADERS, timeout=8)
                if r.status_code == 200:
                    print(f"[!] Found: {url}")
                    f.write(f"200 OK => {url}\n")
                elif r.status_code == 403:
                    print(f"[!] Forbidden: {url}")
                    f.write(f"403 Forbidden => {url}\n")
            except Exception:
                pass

    print(f"[✓] Path bruteforce results saved to {found_paths_file}")
