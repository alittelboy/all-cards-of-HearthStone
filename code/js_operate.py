import json

for series in range(0,20):
    print("series" , str(series))
    for i in range(0,5):
        with open("series" + str(series) + str(i) + ".txt",'r',encoding="utf-8") as f1:
            tstr = f1.readline()
            print(tstr)
            tjs = json.loads(tstr)
            if (tjs["data"]["total"])== 0:
                continue
            else:
                print(tjs["data"]["total"])
                cards = tjs["data"]["cards"]
                for card in cards:
                    print(card["cname"])
                    with open("cards.txt","a",encoding="utf-8") as f2:

                        f2.write(str(card["id"]) + "\t" + str(card["cname"]) + "\t" + str(card["ename"]) + "\t" + str(card["img"]) + "\t" + str(card["artist"]) + "\t" + str(card["description"]).replace("\r",",").replace("\n",",").replace("\t",",") + "\t" + str(card["series"]) + "\t" + str(card["seriesAbbr"]) + "\t" + str(card["seriesName"]) + "\t" + str(card["factions"]) + "\t" + str(card["mana"]) + "\t" + str(card["attack"]) + "\t" + str(card["hp"]) + "\t" + str(card["rule"]).replace("\r",",").replace("\n",",").replace("\t",",") + "\t" + str(card["rarity"]) + "\t" + str(card["race"]) + "\t" + str(card["clazz"]) + "\n" )