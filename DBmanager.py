import pymongo
from PIL import Image
import io
# import os
# import re


class DataBase():

    def __init__(self, connection_string):

        self.client = pymongo.MongoClient(connection_string)
        self.database = self.client['CricScorer']
    
    def searchcoll(self, collection):
        # client = pymongo.MongoClient('mongodb://localhost:27017')
        for db in self.client['CricScorer']:
            if(db == collection):
                return True
        return False
    
    def searchplayer(self, number):

        players = self.database['players']
        data = players.find({})

        for player in data:
            if(player['mobilenumber'] == number):
                return player
            
        return None
    
    def addplayer(self, data):

        players = self.database['players']

        if(data['profilepicture'] == ''):
            players.insert_one(data)
            return
        
        image = Image.open(data['profilepicture'])
        bytes_obj = io.BytesIO()
        # fullpath = os.path.abspath()
        # extension = re.match(r'')
        image.save(bytes_obj, format='JPEG')
        data['image'] = bytes_obj.getvalue()

        players.insert_one(data)





        

    