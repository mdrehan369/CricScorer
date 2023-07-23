import pymongo
from PIL import Image
import io
import gridfs
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
        
        # image = Image.open(data['profilepicture'])
        # bytes_obj = io.BytesIO()
        # image.save(bytes_obj, format='JPEG')
        # data['image'] = bytes_obj.getvalue()

        grid_obj = gridfs.GridFS(self.database)

        with open(data['profilepicture'], 'rb') as f:
            contents = f.read()
        
        image_id = grid_obj.put(contents)
        data['image_id'] = image_id

        players.insert_one(data)

    def getplayers(self):

        players = self.database['players'].find({})
        grid_obj = gridfs.GridFS(self.database)
        # fs = self.database['fs.files']
        data = []

        for index, player in enumerate(players):
            if(player['profilepicture'] != ''):
                image_id = player['image_id']
                output = grid_obj.get(image_id).read()
                with open(f'images/image{index}.jpg', 'wb') as f:
                    f.write(output)
                player['profilepicture'] = f'images/image{index}.jpg'

            data.append(player)

        return data
        
    def searchplayer(self, number):
        return self.database['players'].find_one({'mobilenumber' : number})

    