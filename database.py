import pymongo
from pymongo import MongoClient
import re

from bson import ObjectId

class ChatBotMongoDbContext:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.MovieDatabaseContext = self.myclient["Movies"]
        self.MovieCollection = self.MovieDatabaseContext ["Titles and Synopsis"]
        
        
    def findByMovieName(self, Title):
        query = {"Movie:": {"$regex":re.compile(Title, re.IGNORECASE)}}
        mydoc = self.MovieCollection.find(query)
        return mydoc
    
    def createNewMovie (self, Title, Synopsis, tags):
        mydict = {"Title": Title, "Synopsis": Synopsis, "Genre": tags}
        x = self.MovieCollection.insert_one(mydict)
        return x
    
    def updateMovie (self, id, Title, Synopsis, tags):
        myquery = { "_id": ObjectId(id)}
        newvalues = {"$set": { "Title": Title, "Synopsis": Synopsis, "tags": tags}}
        
        x = self.MovieCollection.update_one(myquery, newvalues)
        
        return x

    def deleteMovie (self, id):
        myquery = {"_id": ObjectId(id)}
        
        x = self.MovieCollection.delete_one(myquery)
        
        return x
    
    def DuplicateAndDeleteMovie (self, title, synopsis):
        
        duplicates = {{"Title": title, "Synopsis": synopsis}}
        
        if len(duplicates) or len (synopsis) >1:
            for duplicates in duplicates[1:]:
                self.MovieCollection.delete_one
        
        x = self.MovieCollection.find_one_and_delete(title)
        
        return x
        if len(duplicates) > 1:
            # Retain the first entry and delete the rest
            for duplicate in duplicates[1:]:
                self.collection.delete_one({"_id": duplicate["_id"]})
            return f"Deleted {len(duplicates) - 1} duplicates of the movie titled '{title}'"
        else:
            return f"No duplicates found for the movie titled '{title}'"


        
"""
Search for a movie, for loop and compare the title + synopsis. If synopsis_1 match with 
synopsis_2 and title_1 matches with title_2, delete. 

Pseudocode:

title1 = input from mongodb
Synopsis1 = input from mongodb

for i < moviecollection
title 2 = moviecollection input title
synopsis2 = moviecollection input synopsis

if title1 == title2 && synopsis1 == synopsis2 
then mongodb.deleteone(id of title2)


"""    
db = ChatBotMongoDbContext()

print(db.createNewMovie("Haikyuu: The dumpster battle", " a highschool volleyball team also known as Karasuno goes against one of their most rivalrious team, Nekoma.", "Sports, Shonen, Drama"))

print ( db.updateMovie("66ac61115d1c00795bbcea57","Haikyuu: Dumpster Battle", "Junior high school student, Shoyo Hinata, becomes obsessed with volleyball after catching a glimpse of Karasuno High School playing in the Nationals on TV. Of short stature himself, Hinata is inspired by a player the commentators nickname 'The Little Giant', Karasuno's short but talented wing spiker.", "Drama, Shonen, Sports, Slice of Life"))