import requests
from bs4 import BeautifulSoup
import os

def init():
    print("Initializing Manga File")
    try:
        f = open("mangalist.txt", "a")
        print("mangalist.txt found, now entering manage mode")
    except:
        print("mangalist.txt not found, creating new mangalist")
        f = open("mangalist.txt", "w")
    print("\n\n\n\n\n")
    print("Kamiyomi AlphaV1 is licensed under the GNU Public License V3")
    print("I don't know what that means, but it's not my problem")
    print("\n\n\n\nType 'help' for help with commands")
    f.close()

    return True

def add(command):
    # TODO add the adder function and implement in scan.py

    if len(command) < 3:
        print("Invalid length, returning null")
        return False
    
    if command[1] == "url":
        add_url(command[2])
    elif command[1] == "name":
        add_nam(command)
    else:
        print("Command modifier '", command[1], "'invalid")
        print("Please use either 'url' for urls or 'name' for manga names")
    
    return True


def add_url(command):
    f = open("mangalist.txt", "a")
    manga_page=requests.get(command)
    if not manga_page.status_code == 200:
        print(f"status error:{ manga_page.status_code }")
        
    manga_title=BeautifulSoup(manga_page.text,'html.parser')

    print("Manga ", str(manga_title.find("ul",class_="manga-info-text").h1.text)," successfully add")
    
    try:
        f.write(command + "\n")
    except:
        print("Invalid URL error, please try again with a different URL")
    return True


def add_nam(command):
    #TODO complete function
    
    print("Please use url, function unavailible at this time")
    return


def delr(command):
    #TODO add the remover function
    return


def helpr():
    #TODO support per command help statements
    print("Commands")
    print("'add' - adds manga to file")
    print("'del' - removes manga from file")
    print("'exit' - allows you to escape from my program :D7")
    


def main():
    init()
    no_exit = True

    while no_exit:
        c = input(":D> ")

        c = c.split()

        if c[0] == "add":
            add(c)
        elif c[0] == "del":
            delr(c)
        elif c[0] == "exit":
            no_exit = False
        elif c[0] == "help":
            helpr()
        else:
            print("No command found")
        


################
main()
