import requests
from bs4 import BeautifulSoup
import json


def scan(nurl, chaps):
    page = requests.get(url=nurl)

    if page.status_code == 200:
        print("Success!")
    elif page.status_code == 404:
        print("Not Found.")
    else :
        print("Not Identified")
    manga = BeuatifulSoup(page.text,'html.parser')
    chapter_list=[]
    chaps=manga.select('div.chapter-list')
    for chapter in chaps:
        chapter_title= chapter.a.text
        chapter_url = chapter.a.get('href')
        chapter_list.append({"title": chapter_title, "url": chapter_url})
    new_chaps = chapter_list

    # I don't like this, but whatever it works
    # If future me wonders what it is, basically new_chaps by default is a "manganelo.chapter" obje
    

    if chaps == "":
        print("New Manga!!!")
        print("Adding %s to your library" %(manga.title))
        print("New Chapter: ", nurl)
        return new_chaps
    if new_chaps == chaps:
        return new_chaps
    print("New chapter: ", nurl)
    return new_chaps
    

def main():
    init_time = 0
    chapter_list = []
    while True:
        #TODO add different source scanning (so scan as it is becomes scan_nelo)
        #TODO add different manga scanning
       
        manga_list = open("mangalist.txt", "r")

        manga_list = (manga_list.read()).split()

        # Basically makes chapter_list the same length as manga_list, using the blank string as an indicator
        # that there is a newly added manga to the list
        if len(chapter_list) != len(manga_list):
            for i in range(len(manga_list) - len(chapter_list), len(manga_list) + 1):
                chapter_list.append('')

        for i, manga in enumerate(manga_list):
            chapter_list = scan(manga, chapter_list)
            #TODO add JSON/Class support for scan

        time.sleep(15)    

main()
