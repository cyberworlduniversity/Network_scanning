#!/usr/bin/env python3
"""Discover live IPv4 hosts on an authorized local network using ARP."""

import argparse


def get_arguments(argv=None):
    parser = argparse.ArgumentParser(
        description="Discover hosts on a local network you own or are authorized to assess."
    )
    parser.add_argument(
        "-t", "--target", dest="ip", required=True,
        help="IPv4 address or CIDR network, for example 192.168.1.0/24",
    )
    return parser.parse_args(argv)


def scan(ip):
    """Send ARP requests and return responding hosts. Requires Scapy and privileges."""
    try:
        import scapy.all as scapy
    except ImportError as exc:
        raise RuntimeError("Scapy is missing. Install dependencies with: python -m pip install -r requirements.txt") from exc

    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    answered = scapy.srp(broadcast / request, timeout=2, verbose=False)[0]
    return [{"ip": packet[1].psrc, "mac": packet[1].hwsrc} for packet in answered]


def print_result(result_list):
    print("IP\t\t\tMAC_Address")
    print("-" * 42)
    for client in result_list:
        print(f"{client['ip']}\t\t{client['mac']}")
    if not result_list:
        print("No responding hosts found.")


def main(argv=None):
    options = get_arguments(argv)
    try:
        print_result(scan(options.ip))
    except PermissionError:
        raise SystemExit("Permission denied. Run with the required network-capture privileges.")
    except RuntimeError as exc:
        raise SystemExit(str(exc))


if __name__ == "__main__":
    main()
