import wikipediaapi
import requests
import json
import datetime


def get_links(page):
    links = page.links
    # return the first five links from the page
    link_arr = []
    link_wiki = wikipediaapi.Wikipedia('en')
    for i, link in enumerate(links):
        if i > 4:
            break
        link_page = link_wiki.page(link)
        link_arr.append(link_page)

    return link_arr


# use the wikipedia library to easily interact with wikipedia pages
wiki_wiki = wikipediaapi.Wikipedia('en')

input_page = input("Page to search: ")
# lets start by statically setting our starter page to 'dog'
start_page = wiki_wiki.page(input_page)
if start_page.exists() != True:
    print("Page: %s does not exist" % input_page)
    exit

link_pages = get_links(start_page)
# now get the first five links off of the links pages
for link_page in link_pages:
    sub_link_page = get_links(link_page)
    print(sub_link_page)

    
