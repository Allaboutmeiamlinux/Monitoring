import time
import random
import sys
from tqdm import tqdm

# ANSI escape sequences for colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Simulate packet details with fake MAC/IP addresses
def random_mac():
    return ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])

def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# Display banner with animation
def print_banner():
    banner = """
    ██████╗ █████╗  ██████╗ ██╗  ██╗███████╗████████╗
    ██╔══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝╚══██╔══╝
    ██████╔╝███████║██████╔╝███████║█████╗     ██║   
    ██╔═══╝ ██╔══██║██╔═══╝ ██╔══██║██╔══╝     ██║   
    ██║     ██║  ██║██║     ██║  ██║███████╗   ██║   
    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝ 
                                          by linux   
    """
    for char in banner:
        print(f"{CYAN}{char}{RESET}", end='', flush=True)
        time.sleep(0.05)
    print("\n")

# Simple loading message for starting packet monitoring with animation
def loading_message():
    print(f"{CYAN}Starting packet monitoring...{RESET}")
    for _ in tqdm(range(10), desc="Initializing", ncols=75, colour="cyan"):
        time.sleep(0.2)
    print(f"{CYAN}Packet monitoring started!{RESET}")
    time.sleep(1)

# Simulate fake packet listing with one by one IP and MAC address change
def list_fake_ips_macs():
    print(f"{CYAN}Monitoring network for IP and MAC addresses...\n{RESET}")
    
    try:
        while True:
            # Generate a fake source and destination IP and MAC addresses
            src_ip = random_ip()
            dst_ip = random_ip()
            src_mac = random_mac()
            dst_mac = random_mac()

            # Print the IPs and MACs one by one with continuous listing
            print(f"{GREEN}Source IP: {src_ip} ({src_mac}){RESET}")
            time.sleep(0.5)  # Simulate delay for next packet

            print(f"{GREEN}Destination IP: {dst_ip} ({dst_mac}){RESET}")
            time.sleep(0.5)  # Simulate delay for next packet

            # Add some space for clarity between updates
            time.sleep(0.1)  # Short break before the next set of IP/MAC addresses

    except KeyboardInterrupt:
        print(f"\n{CYAN}Packet monitoring stopped by user.{RESET}")
        sys.exit()

# Simulate packet analysis with more animation
def analyze_packets():
    print(f"{YELLOW}Analyzing captured packets...{RESET}")
    for _ in tqdm(range(20), desc="Analyzing packets", ncols=75, colour="yellow"):
        packet_id = random.randint(1000, 9999)
        protocol = random.choice(["TCP", "UDP", "ICMP"])
        status = random.choice(["Delivered", "Failed", "Timeout"])
        analysis_info = f"Analyzing packet ID: {packet_id} | Protocol: {protocol} | Status: {status}"
        sys.stdout.write(f"\r{analysis_info}")
        sys.stdout.flush()
        time.sleep(0.4)
    print(f"\n{YELLOW}Packet analysis complete: No suspicious activity detected!{RESET}")
    time.sleep(1)

# Simulate TCP Handshake with more animation
def tcp_handshake():
    print(f"{MAGENTA}Simulating TCP Handshake...{RESET}")
    for _ in tqdm(range(20), desc="Establishing connection", ncols=75, colour="magenta"):
        sys.stdout.write(f"\rSYN --> ACK <-- SYN-ACK")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\n{MAGENTA}TCP Handshake completed: Connection established!{RESET}")
    time.sleep(1)

# Fake packet generator to simulate a network attack or sniffing with animation
def fake_packet_generator():
    print(f"{RED}Generating packets for network attack...{RESET}")
    for _ in tqdm(range(10), desc="Injecting packets", ncols=75, colour="red"):
        src_ip = random_ip()
        dst_ip = random_ip()
        src_mac = random_mac()
        dst_mac = random_mac()

        # Simulate fake packet injection
        packet_info = f"[!] Packet: Src IP: {src_ip} ({src_mac}) -> Dst IP: {dst_ip} ({dst_mac})"
        sys.stdout.write(f"\r{packet_info}")
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"\n{RED}packet generation complete!{RESET}")
    time.sleep(1)

# Simulate more hacking animations
def hacking_animation():
    print(f"\n{MAGENTA}Hacking Network...{RESET}")
    for _ in tqdm(range(15), desc="Hacking in progress", ncols=75, colour="magenta"):
        sys.stdout.write(f"\rConnecting... | Searching for vulnerabilities... | Bypassing firewall...")
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"\n{MAGENTA}Hacking successful! Access granted to network.{RESET}")
    time.sleep(1)

# Main function to simulate fake packet monitoring tool
def main():
    try:
        print_banner()  # Display the ASCII art banner
        loading_message()  # Display the loading message
        hacking_animation()  # Simulate hacking animation
        list_fake_ips_macs()  # Continuously list fake IP and MAC addresses one by one
        analyze_packets()  # Simulate analyzing captured packets
        tcp_handshake()  # Simulate TCP handshake for a fake connection
        fake_packet_generator()  # Simulate fake packet injection for network attack simulation

        print(f"{GREEN}Packet monitoring completed successfully!{RESET}")

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
