#!/usr/bin/env python3
import os
import time
from scanner import scan_target
from bruteforce import brute_force_paths
from github import generate_github_dorks

BANNER = r"""
oooooooo8 ooooooooooo  oooooooo8 oooooooooo  ooooooooooo ooooooooooo       oooooooo8   ooooooo  oooo     oooo oooo     oooo ooooooooooo oooo   oooo ooooooooooo 
888         888    88 o888     88  888    888  888    88  88  888  88     o888     88 o888   888o 8888o   888   8888o   888   888    88   8888o  88  88  888  88 
 888oooooo  888ooo8   888          888oooo88   888ooo8        888         888         888     888 88 888o8 88   88 888o8 88   888ooo8     88 888o88      888     
        888 888    oo 888o     oo  888  88o    888    oo      888         888o     oo 888o   o888 88  888  88   88  888  88   888    oo   88   8888      888     
o88oooo888 o888ooo8888 888oooo88  o888o  88o8 o888ooo8888    o888o         888oooo88    88ooo88  o88o  8  o88o o88o  8  o88o o888ooo8888 o88o    88     o888o    

"""

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Secret Comment Hunter - JS and Secret Scanner")
    parser.add_argument("target", help="Target URL or domain (e.g. https://example.com)")
    args = parser.parse_args()

    print(BANNER)
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    safe_name = args.target.replace("://", "_").replace("/", "_").replace(".", "_")

    output_dir = os.path.join("output", f"{safe_name}")
    os.makedirs(output_dir, exist_ok=True)

    print(f"[*] Starting scan on: {args.target}")
    print(f"[*] Results will be saved in: {output_dir}\n")

    # 1. Scan target (JS files, comments, secrets)
    scan_target(args.target, output_dir)

    # 2. Bruteforce paths
    brute_force_paths(args.target, output_dir)

    # 3. Generate GitHub dorks
    generate_github_dorks(args.target, output_dir)

    print("\n[✓] Scan complete!")

if __name__ == "__main__":
    main()
