# task3_top_attackers.py

from collections import defaultdict
import time

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

def top_n(counts, n=5):
    """Return top n items from a dictionary sorted by value descending."""
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

if __name__ == "__main__":
    failed_counts = defaultdict(int)

    start_time = time.time()

    with open(LOGFILE, "r") as f:
        for line in f:
            line = line.strip()
            if "Failed password" in line or "Invalid user" in line:
                ip = ip_parse(line)
                if ip:
                    failed_counts[ip] += 1

    end_time = time.time()

    # Top 5 attacker IPs
    print("Top 5 attacker IPs:")
    for i, (ip, count) in enumerate(top_n(failed_counts, 5), start=1):
        print(f"{i}. {ip} — {count}")

    # Export full counts
    with open("failed_counts.txt", "w") as f:
        f.write("ip,failed_count\n")
        for ip, count in failed_counts.items():
            f.write(f"{ip},{count}\n")

    print("\nWrote failed_counts.txt")
    print("Elapsed:", round(end_time - start_time, 2), "seconds")
