import requests
from time import sleep

url = "https://www.rotators.biz"
new_content = "Please fetch the content first \x1B[3mThen\x1B[0m Show the content"
old_content = ""
url_home = f"{url}/"
checkFrequency = 20
# noinspection PyRedeclaration
old_content = ""
# noinspection PyRedeclaration
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
            print("Sorry, The Website You Tried To Access Does Not Exist!!")
    except requests.exceptions.MissingSchema:
        print("You are stupid to think that you can put a url with no https:// on it! Go add one with setup:change-url")
        interface(setup_is_true=False)


def store(old):
    global new_content
    global old_content
    if not old:
        new_content = fetch(url_home)
        if new_content == "error":
            print("Error while connecting to site.\nCheck your internet connection.")
        else:
            print("Successfully connected to site.")
            ask = input("Type Y to see the page content, or N to continue.")
            if ask == "Y":
                print(new_content)
    else:
        old_content = fetch(url_home)
        if old_content == "error":
            print("Error while connecting to site.\nCheck your internet connection.")
        else:
            print("Successfully connected to site.")
            ask = input("Type Y to see the page content, or N to continue.")
            if ask == "Y":
                print(old_content)


def setup(command):
    global checkFrequency
    global url
    global url_home
    if command == "change-url":
        url = input("Enter new url\nsetup/change-url:")
        url_home = f"{url}/"
    elif command == "change-check-frequency":
        checkFrequency = int(input("Enter new check frequency\nsetup:"))
    elif command == "change-home-directory":
        prompt = "Enter new home directory\nsetup:"
        url_home = f"{url}{input(prompt)}"
    else:
        print("cmd not valid")
        interface(True)
def compare():
    global new_content
    global old_content
    if new_content == "" or old_content == "":
        print("Please fetch content first.")
    else:
        if new_content == old_content:
            print("Changes Have Been Made!!!!")
        else:
            print("No changes!!!!")
def check():
    global checkFrequency
    global check_amount
    for i in range(1, check_amount):
        print("checking...")
        compare()
        sleep(checkFrequency)

def interface(setup_is_true):
    cmd = input()
    if setup_is_true:
        setup_cmd = input("What would you like to configure?\nsetup:")
        setup_is_true(setup_cmd)
    if cmd == "fetch-old":
        store(True)
        interface(setup_is_true=False)
    if cmd == "fetch-new":
        store(False)
        interface(setup_is_true=False)
    if cmd == "quit":
        exit()
    if cmd == "show-new":
        print()
        interface(setup_is_true=False)
    if cmd == "bald":
        print("Thank You For Your Baldness\n")
        interface(setup_is_true=False)
    if cmd == "setup":
        setup_cmd = input("What would you like to configure?\nsetup:")
        setup_is_true(setup_cmd)
        interface(setup_is_true=False)
    if len(cmd) > 22:
        print("cmd not valid")
    if cmd == "check":
        check()
        interface(setup_is_true=False)
    if "setup" in cmd:
        cmd.replace("setup", "")
        setup_is_true(cmd)
        interface(setup_is_true=False)
    else:
        print("cmd not valid")
        interface(setup_is_true=False)


try:
    print("welcome to the website checker")
    interface(setup_is_true=False)
except KeyboardInterrupt:
    print("Dont leave me!")
