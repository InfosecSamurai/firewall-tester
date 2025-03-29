# 🔥 Firewall Tester 🔍
**By InfosecSamurai**  
*A comprehensive security tool for testing firewall configurations and identifying vulnerabilities*

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/InfosecSamurai/firewall-tester/issues)

## 🌟 Features
- 🕵️‍♂️ Network discovery scanning
- 🚪 Port scanning with common vulnerability checks
- 🔍 Firewall rule analysis with risk assessment
- 📊 Automated report generation (JSON/TXT)
- 🛡️ Detection of misconfigured rules
- 📈 Risk level classification (Critical/High/Medium/Low)

## 📦 Installation

### Prerequisites
- Linux/macOS (Tested on Ubuntu 20.04/22.04 and Kali Linux)
- Python 3.6+
- Nmap (`sudo apt install nmap`)
- Root privileges (for firewall rule analysis)

### Setup
```bash
git clone https://github.com/InfosecSamurai/firewall-tester.git
cd firewall-tester

# Install requirements
pip install -r requirements.txt

# Create output directories
mkdir -p outputs/{scan_reports,vulnerability_reports}
```

## 🚀 Usage

### Quick Start (Full Test Suite)
```bash
sudo ./scripts/firewall_test.sh <TARGET_IP_OR_SUBNET>
# Example:
sudo ./scripts/firewall_test.sh 192.168.1.1
```

### Individual Modules
```bash
# Network scanning
python3 scripts/network_scanner.py 192.168.1.0/24

# Port scanning
python3 scripts/port_scanner.py 192.168.1.1

# Firewall rule analysis (requires root)
sudo python3 scripts/rule_analyzer.py

# Vulnerability checks
python3 scripts/vulnerability_checker.py 192.168.1.1
```

## 📊 Sample Report Output

```json
{
  "scan_type": "comprehensive",
  "target": "192.168.1.1",
  "findings": [
    {
      "issue": "Overly Permissive Rule",
      "rule": "ACCEPT all -- anywhere anywhere",
      "risk": "CRITICAL",
      "recommendation": "Restrict to specific IP ranges"
    }
  ],
  "stats": {
    "open_ports": 5,
    "critical_vulns": 2,
    "high_risk_items": 3
  }
}
```

## 🛠️ Customization
Edit configuration files to tailor tests:
```yaml
# config/test_cases.yaml
test_cases:
  common_ports: [21, 22, 80, 443, 3389]
  vulnerability_checks:
    - name: "DNS Test"
      protocol: "UDP"
      port: 53
```

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## 📜 License
MIT © 2025 InfosecSamurai

## ☕ Support
If you find this tool useful, consider:  
[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge)](https://buymeacoffee.com/infosecsamurai)
