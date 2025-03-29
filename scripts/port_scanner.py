#!/usr/bin/env python3
import nmap
import yaml
from prettytable import PrettyTable

class PortScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.config = self._load_config()
    
    def _load_config(self):
        with open('config/test_cases.yaml', 'r') as f:
            return yaml.safe_load(f)
    
    def scan_ports(self, target, ports=None):
        if not ports:
            ports = ','.join(str(p) for p in self.config['test_cases']['common_ports'])
        
        print(f"\nScanning target: {target} on ports: {ports}")
        self.nm.scan(hosts=target, ports=ports)
        
        results = []
        for host in self.nm.all_hosts():
            for proto in self.nm[host].all_protocols():
                ports = self.nm[host][proto].keys()
                for port in ports:
                    state = self.nm[host][proto][port]['state']
                    results.append((host, proto, port, state))
        
        return results
    
    def display_results(self, results):
        table = PrettyTable()
        table.field_names = ["Host", "Protocol", "Port", "State"]
        
        for result in results:
            table.add_row(result)
        
        print(table)

if __name__ == "__main__":
    scanner = PortScanner()
    target = input("Enter target IP: ")
    results = scanner.scan_ports(target)
    scanner.display_results(results)
