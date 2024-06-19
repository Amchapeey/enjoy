import ipaddress
import concurrent.futures
import httpx
from colorama import init, Fore, Style
from tqdm import tqdm
import time

# Initialize colorama
init()

# Logo and title
logo = """
██████╗░░█████╗░██████╗░██████╗░███████╗░█████╗░██╗░░░██╗███╗░░██╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░██║████╗░██║██╔════╝
██████╔╝███████║██║░░██║██████╔╝█████╗░░███████║██║░░░██║██╔██╗██║╚█████╗░
██╔══██╗██╔══██║██║░░██║██╔══██╗██╔══╝░░██╔══██║██║░░░██║██║╚████║░╚═══██╗
██║░░██║██║░░██║██████╔╝██║░░██║███████╗██║░░██║╚██████╔╝██║░╚███║██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═════╝░
"""

title = f"{Fore.GREEN + Style.BRIGHT}SCORPION SCANNER @KOROS PROPERTY{Fore.RESET + Style.RESET_ALL}"

def check_status(ip):
    url = f"http://{ip}"
    try:
        with httpx.Client(timeout=0.07) as client:  # Timeout set to 5 seconds
            response = client.head(url)
            status_code = response.status_code
            if status_code == 302:
                return None  # Ignore status code 302
            return f"{Fore.GREEN}{ip}{Fore.RESET} - Status code: {Fore.CYAN}{status_code}{Fore.RESET}"
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        return f"{Fore.GREEN}{ip}{Fore.RESET} - Error: {Fore.RED}{str(e)}{Fore.RESET}"

def scan_cidr(cidr):
    ips = list(ipaddress.ip_network(cidr, strict=False).hosts())  # Convert to list for tqdm total count
    results = []

    print(logo)
    print(title)
    print("\nScanning in progress...\n")

    start_time = time.time()
    with tqdm(total=len(ips), desc="", 
              bar_format="{desc}: {bar} {percentage:3.0f}% Elapsed: {elapsed} Remaining: {remaining}",
              dynamic_ncols=True, colour='green') as pbar:
        
        def update_progress(result):
            if result:
                results.append(result)
                ip, status = result.split(' - ')
                pbar.set_postfix_str(f"{Fore.CYAN}{status.strip()}{Fore.RESET}")
            pbar.update(1)

        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:  # Adjust max_workers as needed
            futures = []
            for ip in ips:
                futures.append(executor.submit(check_status, str(ip)))

            for future in concurrent.futures.as_completed(futures):
                update_progress(future.result())

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n\nTime taken: {elapsed_time:.2f} seconds\n")
    print("ALIVE IPs:")
    alive_ips = []
    for result in results:
        if result and "Error" not in result and "Status code: 302" not in result:
            ip = result.split(' - ')[0]
            alive_ips.append(ip)
            print(f"{Fore.GREEN}ALIVE IP{Fore.RESET} - {ip}")

    return alive_ips

if __name__ == "__main__":
    while True:
        cidr_range = input("Enter IP CIDR range (e.g., 192.168.1.0/24): ").strip()
        alive_ips = scan_cidr(cidr_range)
        
        choice = input("\nDo you want to scan another CIDR range? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nExiting the Scorpion Scanner.")
            break

