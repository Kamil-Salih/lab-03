# task1_extract_ips.py

LOGFILE = "sample_auth_small.log"

def ip_parse(line):
    """Extract the source IP from a log line using token-based extraction."""
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
    unique_ips = set()
    total_lines = 0

    with open(LOGFILE, "r") as f:
        for line in f:
            total_lines += 1
            ip = ip_parse(line.strip())
            if ip:
                unique_ips.add(ip)

    print(f"Lines read: {total_lines}")
    print(f"Unique IPs: {len(unique_ips)}")
    print(f"First 10 IPs: {sorted(list(unique_ips))[:10]}")
