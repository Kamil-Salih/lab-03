# task2_failed_counts.py

from collections import defaultdict

LOGFILE = "sample_auth_small.log"

def ip_parse(line):
    """Extract the source IP from a log line."""
    if " from " in line:
        parts = line.split()
        try:
            anchor = parts.index("from")
            ip = parts[anchor + 1]
            return ip.strip()
        except (ValueError, IndexError):
            return None
    return None

if __name__ == "__main__":
    failed_counts = defaultdict(int)

    with open(LOGFILE, "r") as f:
        for line in f:
            line = line.strip()
            if "Failed password" in line or "Invalid user" in line:
                ip = ip_parse(line)
                if ip:
                    failed_counts[ip] += 1

    print("Failed login counts per IP:")
    for ip, count in failed_counts.items():
        print(f"{ip} — {count}")
