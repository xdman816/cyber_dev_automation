* Cybersecurity Dev Project - 11/13/2024

* monitor_downloads.sh: bash script that detects when a file is downloaded, extracts the SHA256 hash of that file, and immediately launches virustotal_search.py
* virustotal_serach.py: using VT file report API call, determine if download is malicious. If it is, then output the common tags (malware names) and the first and last date of submission. 