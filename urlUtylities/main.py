import json

def getUrls(path: str):
    urls = []
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        if len(i) == 2:
            urls.append(i[1])
        else:
            continue
    
    return urls

if __name__ == "__main__":
    with open('urls.json', 'w', encoding='utf-8') as f:
        json.dump(getUrls('resultSemiRaw.json'), f, ensure_ascii=False, indent=4)