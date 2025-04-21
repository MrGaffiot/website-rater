import os, json

with open('imageDownloader/urls.json', 'r', encoding='utf-8') as f:
    urls = json.load(f)

with open('discordBot/packageGenerator/category.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

images = os.listdir('imageDownloader/webImages/')

for image in images:
    if image == "imageGenerator.py":
        continue
    print(image)
    try:
        cleanImage = image.split('screenshot_')[1].split('.')[0]
    except:
        continue
    
    for url in urls:
        if 'www' in url:
            if 'http://' in url:
                if url.split('http://')[1].split('.')[1] == cleanImage:
                    if image:
                        categories.append({"url": url, "isDone": False, "imagePath": image})
            else:
                if url.split('https://')[1].split('.')[1] == cleanImage:
                    if image:
                        categories.append({"url": url, "isDone": False, "imagePath": image})
        else:
            if 'http://' in url:
                if url.split('http://')[1].split('.')[0] == cleanImage:
                    if image:
                        categories.append({"url": url, "isDone": False, "imagePath": image})
            else:
                if url.split('https://')[1].split('.')[0] == cleanImage:
                    if image:
                        categories.append({"url": url, "isDone": False, "imagePath": image})
            
duplicateFinder = set()
final = []

for i in categories:
    if i["url"] not in duplicateFinder:
        duplicateFinder.add(i["url"])
        final.append(i)
    else:
        print("duplicate found")
        
with open('discordBot/packageGenerator/category.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=4)

