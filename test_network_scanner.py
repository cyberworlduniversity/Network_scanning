import unittest
from unittest.mock import patch
import network_scanner

class NetworkScannerTests(unittest.TestCase):
    def test_argument_parser_accepts_target(self):
        with patch("sys.argv", ["network_scanner.py", "--target", "192.168.1.0/24"]):
            self.assertEqual(network_scanner.get_arguments().ip, "192.168.1.0/24")

    def test_argument_parser_requires_target(self):
        with patch("sys.argv", ["network_scanner.py"]):
            with self.assertRaises(SystemExit) as exc:
                network_scanner.get_arguments()
            self.assertEqual(exc.exception.code, 2)

    def test_print_result_formats_discovered_hosts(self):
        with patch("builtins.print") as output:
            network_scanner.print_result([{"ip": "192.168.1.2", "mac": "00:11:22:33:44:55"}])
        self.assertIn("192.168.1.2", output.call_args_list[1].args[0])

if __name__ == "__main__":
    unittest.main()
