import os, json, shutil
from packageGenerator.zipper import create_zip_archive

def makePackageInfo(size: int):
    with open('discordBot/packageGenerator/category.json', 'r', encoding='utf-8') as f:
        categories = json.load(f)
    
    notDone = [i for i in categories if not i['isDone']]
    print(notDone)
    package = [notDone[i] for i in range(size)]
    print(package)
    
    for i in package:
        print(package[package.index(i)]["imagePath"].split("imageDownloader/webImages/"))
        package[package.index(i)]["imagePath"] = package[package.index(i)]["imagePath"].split("imageDownloader/webImages/")[0]
    
#    for i in categories:
#        for i in package:
#            if i['url'] == categories[categories.index(i)]['url']:
#                categories[categories.index(i)]["isDone"] = True
    
    with open('discordBot/packageGenerator/category.json', 'w', encoding='utf-8') as f:
        json.dump(categories, f, ensure_ascii=False, indent=4)
    
    return package

def makePackage(package: list):
    with open('discordBot/packageGenerator/packages/packageInfo.json', 'w', encoding='utf-8') as f:
        json.dump(package, f, ensure_ascii=False, indent=4)
    
    print(f'package: {package}')
    
    for i in package:
        shutil.copyfile("imageDownloader/webImages/"+i['imagePath'], 'discordBot/packageGenerator/packages/' + i['imagePath'])

    listDir = os.listdir('discordBot/packageGenerator/packages')
    print(listDir)
    files = []
    for i in listDir:
        files.append('discordBot/packageGenerator/packages/'+i)
        
    create_zip_archive(files, 'discordBot/packageGenerator/package.zip')
    
    for i in listDir:
        if i != 'package.zip':
            os.remove(f'discordBot/packageGenerator/packages/{i}')

if __name__ == "__main__":
    makePackage(makePackageInfo(4))

