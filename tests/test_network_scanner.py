import unittest
from unittest.mock import patch, MagicMock
from scripts.network_scanner import NetworkScanner

class TestNetworkScanner(unittest.TestCase):
    @patch('scripts.network_scanner.nmap.PortScanner')
    def test_scan_network(self, mock_nmap):
        # Setup mock
        mock_scanner = MagicMock()
        mock_nmap.return_value = mock_scanner
        
        mock_scanner.all_hosts.return_value = ['192.168.1.1', '192.168.1.2']
        mock_scanner.__getitem__.side_effect = lambda x: MagicMock(state=lambda: 'up')
        
        # Test
        scanner = NetworkScanner()
        hosts = scanner.scan_network('192.168.1.0/24')
        
        # Assert
        self.assertEqual(len(hosts), 2)
        self.assertIn('192.168.1.1', hosts)
        self.assertIn('192.168.1.2', hosts)
        mock_scanner.scan.assert_called_with(hosts='192.168.1.0/24', arguments='-sn')

if __name__ == '__main__':
    unittest.main()
