# main.py
import sys
from parse_nmap import extract_open_ports
from analyze_ports import analyze_ports

def main(xml_path):
    ports = extract_open_ports(xml_path)
    if not ports:
        print("No open ports found.")
        return
    print(f"Found {len(ports)} open port(s). Analyzing...")
    report = analyze_ports(ports)
    print("\n=== Summary ===")
    print(report.summary)
    for p in report.ports:
        print(f"\nPort {p.port} ({p.service})")
        print(f"  Purpose: {p.purpose}")
        print(f"  Risk: {p.risk}")
        print(f"  Suggestion: {p.suggestion}")

if __name__ == "__main__":
    main(sys.argv[1])