import json
from json import JSONEncoder, JSONDecoder


"""
The way saving is going to work is we're going to fill SaveData with all the
data we want to save then encode it into JSON.  Then we also load it to
a SaveData object on opening of the program
"""


class SaveData:
    def __init__(self):
        pass



class DataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class DataDecoder(JSONDecoder):
    pass


def load_file(game_data_file):
    f = open(game_data_file, 'r')
    saveDataDict = json.load(f)
    datRet = SaveData()
    datRet.__dict__ = saveDataDict
    return # returns the independent variables of Save Data 


def save_on_file(game_data_path, json_string):
    f = open(game_data_path+"/save.json", 'w+')
    f.write(json_string)


def jsonify_game_data(game_data_path):
    saveDat = SaveData()
    return json.dumps(saveDat, cls=DataEncoder, indent=4)
