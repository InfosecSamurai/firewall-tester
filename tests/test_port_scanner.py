import unittest
from unittest.mock import patch, MagicMock
from scripts.port_scanner import PortScanner

class TestPortScanner(unittest.TestCase):
    @patch('scripts.port_scanner.nmap.PortScanner')
    def test_scan_ports(self, mock_nmap):
        # Setup mock
        mock_scanner = MagicMock()
        mock_nmap.return_value = mock_scanner
        
        mock_scanner.all_hosts.return_value = ['192.168.1.1']
        mock_scanner['192.168.1.1'].all_protocols.return_value = ['tcp']
        mock_scanner['192.168.1.1']['tcp'].keys.return_value = [80, 443]
        mock_scanner['192.168.1.1']['tcp'][80] = {'state': 'open'}
        mock_scanner['192.168.1.1']['tcp'][443] = {'state': 'filtered'}
        
        # Test
        scanner = PortScanner()
        results = scanner.scan_ports('192.168.1.1')
        
        # Assert
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0][2], 80)
        self.assertEqual(results[0][3], 'open')
        self.assertEqual(results[1][2], 443)
        self.assertEqual(results[1][3], 'filtered')

if __name__ == '__main__':
    unittest.main()
