#!/usr/bin/env python

class Book:

    title = None
    year = None
    genre  = None
    summary = None
    position_marker = None 

    def __init__(self, book_data):
        self.title = book_data["title"]
        self.year = book_data["year"]
        self.genre = book_data["genre"]
        self.summary = book_data["summary"]
        self.position_marker = book_data["position_marker"]

    def getTitle(self):
        return self.title

    def getYear(self):
        return self.year
        
    def getGenre(self):
        return self.genre

    def getSummary(self):
        return self.summary

    def getPositionMarker(self):
        return self.position_marker
