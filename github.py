import os
from urllib.parse import urlparse

def generate_github_dorks(target, output_dir):
    print("\n[*] Generating GitHub dork URLs...")
    parsed = urlparse(target)
    safe_host = parsed.netloc or target

    dorks = [
        f"https://github.com/search?q=filename:.env+{safe_host}",
        f"https://github.com/search?q=filename:.git-credentials+{safe_host}",
        f"https://github.com/search?q=filename:config.json+{safe_host}",
        f"https://github.com/search?q=filename:firebase.json+{safe_host}",
        f"https://github.com/search?q=filename:docker-compose.yml+{safe_host}",
        f"https://github.com/search?q=apikey+{safe_host}",
        f"https://github.com/search?q=secret+{safe_host}",
        f"https://github.com/search?q=token+{safe_host}",
    ]

    dorks_file = os.path.join(output_dir, "github_dorks_results.txt")
    with open(dorks_file, "w", encoding="utf-8") as f:
        for dork in dorks:
            print(dork)
            f.write(dork + "\n")

    print(f"[✓] GitHub dorks saved to {dorks_file}")
