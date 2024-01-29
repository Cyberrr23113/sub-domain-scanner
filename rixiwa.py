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
	                                            
 _ __(_)_  _(_)_      ____ _    | |__   ___ | |_ 
| '__| \ \/ / \ \ /\ / / _` |   | '_ \ / _ \| __|
| |  | |>  <| |\ V  V / (_| |   | |_) | (_) | |_ 
|_|  |_/_/\_\_| \_/\_/ \__,_|___|_.__/ \___/ \__|
                           |_____|               

                           

coder: https://t.me/rixiwa_bot




                       
""")

target_domain = input("Hedef site örnk(google.com): ")
wordlist = "wordlist.txt"

check_subdomains(target_domain, wordlist)
