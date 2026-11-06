#!/usr/bin/env python3
"""Discover live IPv4 hosts on a small, authorized private network using ARP."""

import argparse
import ipaddress


MAX_ADDRESSES = 256


def validate_target(value):
    """Accept only private IPv4 targets containing at most 256 addresses."""
    try:
        network = ipaddress.ip_network(value, strict=False)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Enter a valid IPv4 address or CIDR network.") from exc

    if not isinstance(network, ipaddress.IPv4Network):
        raise argparse.ArgumentTypeError("IPv6 targets are not supported.")
    if not network.is_private or network.is_loopback or network.is_link_local:
        raise argparse.ArgumentTypeError("Only private, non-loopback IPv4 networks are allowed.")
    if network.is_multicast or network.is_reserved or network.is_unspecified:
        raise argparse.ArgumentTypeError("This address range is not a valid scan target.")
    if network.num_addresses > MAX_ADDRESSES:
        raise argparse.ArgumentTypeError(
            f"Target is too large ({network.num_addresses} addresses). Limit: {MAX_ADDRESSES}."
        )
    return str(network)


def get_arguments(argv=None):
    parser = argparse.ArgumentParser(
        description="Discover hosts on a small private network you own or are authorized to assess."
    )
    parser.add_argument(
        "-t", "--target", dest="ip", required=True, type=validate_target,
        help="Private IPv4 address or CIDR network (maximum 256 addresses), e.g. 192.168.1.0/24",
    )
    return parser.parse_args(argv)


def scan(ip):
    """Send ARP requests and return responding hosts. Requires Scapy and privileges."""
    try:
        import scapy.all as scapy
    except ImportError as exc:
        raise RuntimeError(
            "Scapy is missing. Install dependencies with: python -m pip install -r requirements.txt"
        ) from exc

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
