#!/usr/bin/env python3
import json
import datetime
from prettytable import PrettyTable

class ReportGenerator:
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    def generate_report(self, scan_type, data):
        report = {
            "scan_type": scan_type,
            "timestamp": self.timestamp,
            "data": data
        }
        
        filename = f"outputs/scan_reports/{scan_type}_{self.timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        
        print(f"Report generated: {filename}")
        return filename
    
    def generate_vulnerability_report(self, vulnerabilities):
        report = {
            "report_type": "vulnerability",
            "timestamp": self.timestamp,
            "vulnerabilities": vulnerabilities,
            "risk_summary": self._calculate_risk_summary(vulnerabilities)
        }
        
        filename = f"outputs/vulnerability_reports/vulnerability_{self.timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        
        print(f"Vulnerability report generated: {filename}")
        return filename
    
    def _calculate_risk_summary(self, vulnerabilities):
        summary = {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0
        }
        
        for vuln in vulnerabilities:
            summary[vuln['risk']] += 1
        
        return summary

if __name__ == "__main__":
    # Example usage
    generator = ReportGenerator()
    sample_data = {"test": "sample data"}
    generator.generate_report("port_scan", sample_data)
