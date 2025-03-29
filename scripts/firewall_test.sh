#!/bin/bash

# Firewall Tester - Main Script

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Configuration
TARGET="$1"
OUTPUT_DIR="outputs"
REPORT_DIR="$OUTPUT_DIR/scan_reports"
VULN_DIR="$OUTPUT_DIR/vulnerability_reports"

# Create output directories if they don't exist
mkdir -p $REPORT_DIR
mkdir -p $VULN_DIR

# Run tests
echo "Starting Firewall Tests..."
echo "Target: $TARGET"
echo ""

# Network scan
echo "Running Network Scan..."
python3 network_scanner.py $TARGET > $REPORT_DIR/network_scan_$(date +%Y%m%d_%H%M%S).txt

# Port scan
echo "Running Port Scan..."
python3 port_scanner.py $TARGET > $REPORT_DIR/port_scan_$(date +%Y%m%d_%H%M%S).txt

# Rule analysis
echo "Analyzing Firewall Rules..."
python3 rule_analyzer.py > $VULN_DIR/rule_analysis_$(date +%Y%m%d_%H%M%S).txt

# Vulnerability checks
echo "Running Vulnerability Checks..."
python3 vulnerability_checker.py $TARGET > $VULN_DIR/vulnerability_checks_$(date +%Y%m%d_%H%M%S).txt

echo ""
echo "All tests completed!"
echo "Reports saved to $OUTPUT_DIR"
