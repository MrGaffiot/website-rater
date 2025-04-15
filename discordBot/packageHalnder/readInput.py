import json
import packageHalnder.dbHanderl as dbHanderl
import os

dbHanderl = dbHanderl.databaseHandler()

def writeInput():
    with open('discordBot/packageHalnder/exportData.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for i in data:
        if i['good'] == True:
            dbHanderl.addEntry(url=i['url'], imagePath=i['imagePath'], quality="good")
        elif i['good'] == False:
            dbHanderl.addEntry(url=i['url'], imagePath=i['imagePath'], quality="bad")
        elif i['good'] == "misc":
            dbHanderl.addEntry(url=i['url'], imagePath=i['imagePath'], quality="misc")
    
    os.remove('discordBot/packageHalnder/exportData.json')

if __name__ == '__main__':
    writeInput()

