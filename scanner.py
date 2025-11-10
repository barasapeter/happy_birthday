import re
import urllib.request
from urllib.parse import urlparse
import os

def is_direct_download_link(text):
    pattern = r"(?i)\bhttps?://\S+\b"
    matches = re.findall(pattern, text)
    
    return bool(matches)
def contains_malicious_link(url):
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        if "malicious" in content.lower():
            return True
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if check_reputation(domain):
            return True
        return False
    except (urllib.error.URLError, ValueError):
        return False

def check_reputation(domain):
    # Placeholder logic, assuming any domain with "malicious" in it is flagged as malicious
    if "malicious" in domain:
        return True
    else:
        return False



