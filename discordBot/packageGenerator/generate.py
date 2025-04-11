import os, json, shutil
from zipper import create_zip_archive

def makePackageInfo(size: int):
    with open('discordBot\\packageGenerator\\category.json', 'r', encoding='utf-8') as f:
        categories = json.load(f)
    
    notDone = [i for i in categories if not i['isDone']]
    package = [notDone[i] for i in range(size)]
    
    return package

def makePackage(package: list):
    with open('discordBot\\packageGenerator\\packages\\packageInfo.json', 'w', encoding='utf-8') as f:
        json.dump(package, f, ensure_ascii=False, indent=4)
    
    for i in package:
        name = i['imagePath'].split("imageDownloader\\webImages\\")[1]
        shutil.copyfile(i['imagePath'], 'discordBot\\packageGenerator\\packages\\' + name)

    listDir = os.listdir('discordBot\\packageGenerator\\packages')
    files = []
    for i in listDir:
        files.append('discordBot\\packageGenerator\\packages\\'+i)
        
    create_zip_archive(files, 'discordBot\\packageGenerator\\package.zip')
    
    for i in os.listdir('discordBot\\packageGenerator\\packages'):
        if i != 'package.zip':
            os.remove(f'discordBot\\packageGenerator\\packages\\{i}')

if __name__ == "__main__":
    makePackage(makePackageInfo(4))

