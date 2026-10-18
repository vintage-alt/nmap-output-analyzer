# parse_nmap.py
from libnmap.parser import NmapParser

def extract_open_ports(xml_file):
    """
    Read nmap XML and return a concise list of open ports.
    Output format: [{"host": "192.168.1.1", "port": 22, "service": "ssh", "version": "OpenSSH 8.2"}, ...]
    """
    parsed = NmapParser.parse_fromfile(xml_file)
    results = []
    for host in parsed.hosts:
        for serv in host.services:
            if serv.state == "open":
                results.append({
                    "host": host.address,
                    "port": serv.port,
                    "service": serv.service,
                    "version": f"{serv.banner}" if serv.banner else "unknown"
                })
    return results

if __name__ == "__main__":
    ports = extract_open_ports("scan.xml")
    print(ports)