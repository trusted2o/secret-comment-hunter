
## Overview

**Secret Comment Hunter** is a powerful reconnaissance tool to scan web targets for exposed comments, secrets, credentials, and sensitive paths in JavaScript, JSON, ENV, YAML, XML, PHP files, and more. It also generates useful GitHub dork URLs to assist in bug hunting and vulnerability research.

---

## Features

- Scans all related JS, JSON, ENV, YML, XML, PHP files for comments and secrets
- Detects common secret patterns like API keys, passwords, tokens, AWS keys, Slack tokens, etc.
- Performs path bruteforcing for common sensitive files like `.env`, `config.json`, `.git/config`, etc.
- Generates GitHub dorks tailored to the target domain for public repository reconnaissance
- Saves results neatly into timestamped output directories
- Simple single-command CLI interface
- Displays an eye-catching ASCII banner on launch

---

## Installation

### Prerequisites

- Python 3.8+  
- `pip` package manager

### Steps

1. Clone the repository
   git clone https://github.com/trusted2o/secret-comment-hunter.git
   cd secret-comment-hunter
   
2. Install dependencies via pip
pip install -r requirements.txt

## Usage
Run the tool with a single command followed by the target URL: python3 secret-comment-hunter.py https://example.com
Example:
python3 secret-comment-hunter.py http://testphp.vulnweb.com

## The tool will:
Crawl and scan all JS and related files for suspicious comments/secrets
Bruteforce common sensitive paths
Generate GitHub dork URLs for the target
Save all output in a timestamped directory inside output/

## Output
All results are saved inside an output folder named after the target and timestamp, for example:
output/secretcommenthunter-http_example_com-20250804_2015/

## This folder includes:

js_files.txt — List of all discovered JS and related file URLs

secrets_found.txt — Suspicious comments and secret findings

js_comments.txt — All scanned comments (non-suspicious as well)

path_bruteforce.txt — Results of sensitive path bruteforce

github_dorks_results.txt — Generated GitHub dork URLs

## Contribution
Feel free to open issues or submit pull requests for new features, bug fixes, or improvements.

## License
This project is licensed under the MIT License.

## Author
Developed by Al-Amin
