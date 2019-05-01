import wikipediaapi
import requests
import json
import datetime
import pydot
import graphviz
import os

from IPython.display import Image, display

class Graph:
    def __init__(self, search_term, how_deep=0):
        # initialize the graph
        self.g = pydot.Dot(graph_type="digraph")
        self.wiki_wiki = wikipediaapi.Wikipedia('en')
        self.start_page = self.wiki_wiki.page(search_term)
        self.search_term = search_term
        self.how_deep = how_deep

        # check if the starter page exists
        if self.start_page.exists() != True:
            print("Page: %s does not exist" % search_term)
            exit

    def create_links(self):
        #TODO: Try doing this recursively
        page = self.start_page
        for i in range(self.how_deep):
            print("We are %s levels deep." % i)
            # down the rabbit hole we go
            links = page.links
            for i, link in enumerate(links):
                if i > 8:
                    break
                link_page = self.wiki_wiki.page(link)
                self.create_node(link_page)
                self.create_edge(page, link_page)
            page = link_page

    def create_node(self, sub_page=None):
        node = pydot.Node(sub_page.title, style="filled", fillcolor="red", fontname='Courier', fontsize='10')
        self.g.add_node(node)

    def create_edge(self, parent_page, sub_page):
        edge = pydot.Edge(parent_page.title, sub_page.title)
        self.g.add_edge(edge)

    def write_out(self):
        self.g.write_png(self.search_term+'.png')


def main():
    input_page = input("Page to search: ")

    # create a new graph for this search term
    g = Graph(input_page, 20)
    g.create_links()
    g.write_out()

main()
    
