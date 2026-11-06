import unittest
from unittest.mock import patch

import network_scanner


class NetworkScannerTests(unittest.TestCase):
    def test_argument_parser_accepts_private_target(self):
        args = network_scanner.get_arguments(["--target", "192.168.1.0/24"])
        self.assertEqual(args.ip, "192.168.1.0/24")

    def test_single_private_address_is_normalized(self):
        args = network_scanner.get_arguments(["--target", "192.168.1.7"])
        self.assertEqual(args.ip, "192.168.1.7/32")

    def test_argument_parser_requires_target(self):
        with self.assertRaises(SystemExit) as exc:
            network_scanner.get_arguments([])
        self.assertEqual(exc.exception.code, 2)

    def test_rejects_public_network(self):
        with self.assertRaises(SystemExit):
            network_scanner.get_arguments(["--target", "8.8.8.0/24"])

    def test_rejects_large_private_network(self):
        with self.assertRaises(SystemExit):
            network_scanner.get_arguments(["--target", "10.0.0.0/16"])

    def test_rejects_ipv6(self):
        with self.assertRaises(SystemExit):
            network_scanner.get_arguments(["--target", "2001:db8::/64"])

    def test_print_result_formats_discovered_hosts(self):
        with patch("builtins.print") as output:
            network_scanner.print_result([{"ip": "192.168.1.2", "mac": "00:11:22:33:44:55"}])
        printed = "\n".join(str(call.args[0]) for call in output.call_args_list)
        self.assertIn("192.168.1.2", printed)
        self.assertIn("00:11:22:33:44:55", printed)


if __name__ == "__main__":
    unittest.main()
