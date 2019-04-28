import wikipediaapi
import requests
import json
import datetime
import pydot
import graphviz
import os

from IPython.display import Image, display


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

g = pydot.Dot(graph_type="digraph")

node = pydot.Node(start_page.title, style="filled", fillcolor="red")
g.add_node(node)

link_pages = get_links(start_page)
# now get the first five links off of the links pages
for link_page in link_pages:
    sub_link_pages = get_links(link_page)
    for s_page in sub_link_pages:
        # create a node for each sub page
        node = pydot.Node(s_page.title, style="filled", fillcolor="yellow")
        g.add_node(node)
        edge = pydot.Edge(start_page.title, s_page.title)
        g.add_edge(edge)

g.write_png('example1.png')

    
