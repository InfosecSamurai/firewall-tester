import unittest
from unittest.mock import patch, MagicMock
from scripts.rule_analyzer import RuleAnalyzer

class TestRuleAnalyzer(unittest.TestCase):
    @patch('scripts.rule_analyzer.iptables.easy.dump_chain')
    def test_analyze_rules(self, mock_iptables):
        # Setup mock
        mock_iptables.return_value = [
            "ALLOW ALL FROM ANY",
            "ALLOW TCP 22 FROM 192.168.1.0/24"
        ]
        
        # Test
        analyzer = RuleAnalyzer()
        vulnerabilities = analyzer.analyze_rules(analyzer.get_current_rules())
        
        # Assert
        self.assertEqual(len(vulnerabilities), 1)
        self.assertEqual(vulnerabilities[0]['rule'], "ALLOW ALL FROM ANY")
        self.assertEqual(vulnerabilities[0]['risk'], "CRITICAL")

if __name__ == '__main__':
    unittest.main()
