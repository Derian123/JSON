import json
from urllib.request import urlopen


def main():

    titles = []
    contents = urlopen("http://mysafeinfo.com/api/data?list=englishmonarchs&format=json").read()
    cont = json.loads(contents.decode('utf-8'))
    for item in cont:
        titles.append(item["nm"])
    print("\n".join(titles))

main()