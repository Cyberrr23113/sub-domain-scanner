import socket

def check_host(host, port):
    try:
        sock = socket.create_connection((host, port), timeout=5)
        return True
    except:
        return False

def check_subdomains(domain, wordlist):
    with open(wordlist, "r") as subdomains:
        for subdomain in subdomains:
            subdomain = subdomain.strip() + "." + domain
            if check_host(subdomain, 80):
                print("[X] Bulunan subdomain:", subdomain)

print("""
	                                            
   LOADING kdeneonn
▇▇▇▇▇▇▇▇▇▇▇▇▇▇▢
╭━╮╭━╮╭╮　╱
╰━┫╰━┫╰╯ ╱╭╮
╰━╯╰━╯　╱ ╰╯
COMPLETE
                           

coder: https://t.me/kdeneonn




                       
""")

target_domain = input("target sample site (google.com): ")
wordlist = "wordlist.txt"

check_subdomains(target_domain, wordlist)
