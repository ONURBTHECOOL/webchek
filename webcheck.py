import requests
from time import sleep

url = "https://rotators.biz"
urlHome = f"{url}/index.html"
checkFrequency = 20
old_content = ""
new_content = ""
check_amount = 20

def fetch(address):
    try:
        try:
            output = requests.get(address)
            if output.status_code == 200:
                return output.text
            else:
                print("error")
        except requests.exceptions.ConnectionError:
            print("Sorry, The Website You Tryed To Accsess Dose Not Exist!!")
    except requests.exceptions.MissingSchema:
        print("You are stupid to thing that you can put a url with no https:// thing on it!")


def store(old):
    global new_content
    global old_content
    if not old:
        new_content = fetch(url)
        if new_content == "error":
            print("Error while connecting to site.\nCheck your internet connection.")
        else:
            print("Successfully connected to site.")
            ask = input("Type Y to see the page content, or N to continue.")
            if ask == "Y":
                print(new_content)
            else:
                pass
    else:
        old_content = fetch(urlHome)
        print("store success")
        print(old_content)


def setup(command):
    global checkFrequency
    global url
    if command == "change-url":
        url = input("Enter new url\n")
    elif command == "change-check-frequency":
        checkFrequency = int(input("Enter new check frequency\n"))
    else:
        print("cmd not valid")
def compare():
    global new_content
    global old_content
    if new_content == old_content:
        print("Changes Have Been Made!!!!")
    else:
        print("No changes!!!!")
def check():
    global checkFrequency
    global check_amount
    for i in range(check_amount):
        sleep(checkFrequency)
        print("checking...")
        compare()

def interface():
    cmd = input()
    if cmd == "fetch-old":
        store(True)
        interface()
    if cmd == "fetch-new":
        store(False)
        interface()
    if cmd == "quit":
        exit()
    if cmd == "show-new":
        print()
        interface()
    if cmd == "bald":
        print("Thank You For Your Baldness\n")
        interface()
    if cmd == "setup":
        setup_cmd = input("What would you like to configure?\n")
        setup(setup_cmd)
        interface()
    if len(cmd) > 22:
        print("no")
    if cmd == "check":
        check()
        interface()
    else:
        print("cmd not valid")
        interface()


print("welcome to the website checker")
interface()