#!/usr/bin/env python3
import json
import iptables
from prettytable import PrettyTable

class RuleAnalyzer:
    def __init__(self):
        self.vulnerable_rules = self._load_vulnerable_rules()
    
    def _load_vulnerable_rules(self):
        with open('config/firewall_rules.json', 'r') as f:
            return json.load(f)['known_vulnerable_rules']
    
    def get_current_rules(self):
        try:
            return iptables.easy.dump_chain('filter', 'INPUT')
        except Exception as e:
            print(f"Error accessing iptables: {e}")
            return []
    
    def analyze_rules(self, rules):
        vulnerabilities = []
        
        for rule in rules:
            for vuln_rule in self.vulnerable_rules:
                if vuln_rule['rule'] in str(rule):
                    vulnerabilities.append({
                        'rule': str(rule),
                        'risk': vuln_rule['risk'],
                        'description': vuln_rule['description']
                    })
        
        return vulnerabilities
    
    def display_results(self, vulnerabilities):
        if not vulnerabilities:
            print("\nNo vulnerable firewall rules detected!")
            return
        
        table = PrettyTable()
        table.field_names = ["Rule", "Risk Level", "Description"]
        
        for vuln in vulnerabilities:
            table.add_row([vuln['rule'], vuln['risk'], vuln['description']])
        
        print("\nVulnerable Firewall Rules Detected:")
        print(table)

if __name__ == "__main__":
    analyzer = RuleAnalyzer()
    current_rules = analyzer.get_current_rules()
    vulnerabilities = analyzer.analyze_rules(current_rules)
    analyzer.display_results(vulnerabilities)
