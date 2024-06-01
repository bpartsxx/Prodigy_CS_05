#!/usr/bin/env python3

# File: analyze_packets.py

from scapy.all import sniff

def packet_handler(packet):
    """
    Function to handle captured packets.
    Prints packet summary and detailed info.
    """
    print(packet.summary())  # Print packet summary
    print(packet.show())     # Print detailed packet info

def main():
    """
    Main function to capture and analyze packets.
    """
    print("Starting packet capture. Press Ctrl+C to stop.")
    # Capture packets, calling packet_handler for each packet
    sniff(prn=packet_handler)

if __name__ == "__main__":
    main()
