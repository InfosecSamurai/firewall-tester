#!/usr/bin/env python3
import nmap
import yaml
from prettytable import PrettyTable

class NetworkScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.config = self._load_config()
        
    def _load_config(self):
        with open('config/test_cases.yaml', 'r') as f:
            return yaml.safe_load(f)
    
    def scan_network(self, target):
        print(f"\nScanning network: {target}")
        self.nm.scan(hosts=target, arguments='-sn')
        
        hosts = []
        for host in self.nm.all_hosts():
            if self.nm[host].state() == 'up':
                hosts.append(host)
        
        return hosts
    
    def display_results(self, hosts):
        table = PrettyTable()
        table.field_names = ["IP Address", "Status"]
        
        for host in hosts:
            table.add_row([host, "Active"])
        
        print(table)

if __name__ == "__main__":
    scanner = NetworkScanner()
    target = input("Enter target network (e.g., 192.168.1.0/24): ")
    hosts = scanner.scan_network(target)
    scanner.display_results(hosts)
