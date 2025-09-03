import datetime
from customAssetManager import AssetManager

assets = AssetManager()

price_list = {"fish_blue": 5,
                "fish_brown": 10,
                "fish_green": 15,
                "fish_grey": 20,
                "fish_orange":25,
                "fish_pink": 30,
                "fish_red": 100000
                }

class player():
    def __init__(self, name, balance, fish_blue, fish_brown, fish_green, fish_grey, fish_orange, fish_pink, fish_red):
        self.name = name
        self.balance = balance
        self.fish_blue = fish_blue
        self.fish_brown = fish_brown
        self.fish_green = fish_green
        self.fish_grey = fish_grey
        self.fish_orange = fish_orange
        self.fish_pink = fish_pink
        self.fish_red = fish_red

    def updateBalance(self, amounth):
        self.balance += amounth

    def buyItem(self, item):
        match item:
            case "fish_blue":
                if checkPriceBalance(price_list[item], self.balance):
                    self.fish_blue += 1
                    self.updateBalance(price_list[item]*-1)
            case "fish_brown":
                if checkPriceBalance(price_list[item], self.balance):
                    self.fish_brown += 1
                    self.updateBalance(price_list[item]*-1)
            case "fish_green":
                if checkPriceBalance(price_list[item], self.balance):
                    self.fish_green += 1
                    self.updateBalance(price_list[item]*-1)
            case "fish_grey":
                if checkPriceBalance(price_list[item], self.balance):
                    self.fish_grey += 1
                    self.updateBalance(price_list[item]*-1)
            case "fish_orange":
                if checkPriceBalance(price_list[item], self.balance):
                    self.fish_orange += 1
                    self.updateBalance(price_list[item]*-1)
            case "fish_pink":
                if checkPriceBalance(price_list[item], self.balance):
                    self.fish_pink += 1
                    self.updateBalance(price_list[item]*-1)
            case "fish_red":
                if checkPriceBalance(price_list[item], self.balance):
                    self.fish_red += 1
                    self.updateBalance(price_list[item]*-1)


def main():
    #savegame load
    loadedPlayerData = loadSavegame()
    player1 = player(loadedPlayerData["name"], 
                     int(loadedPlayerData["balance"]), 
                     int(loadedPlayerData["fish_blue"]), 
                     int(loadedPlayerData["fish_brown"]), 
                     int(loadedPlayerData["fish_green"]), 
                     int(loadedPlayerData["fish_grey"]), 
                     int(loadedPlayerData["fish_orange"]),
                     int(loadedPlayerData["fish_pink"]), 
                     int(loadedPlayerData["fish_red"]))
    #----------
    #hier game loop einfügen
    #player1.updateBalance(calcAmounth(player1))
    #player1.buyItem("fish_blue")

    #Bereich Texturen
    tex_fish_blue = assets.load_image("fish_blue_outline.png")
    tex_fish_brown = assets.load_image("fish_brown_outline.png")
    tex_fish_green = assets.load_image("fish_green_outline.png")
    tex_fish_grey = assets.load_image("fish_grey_outline.png")
    tex_fish_orange = assets.load_image("fish_orange_outline.png")
    tex_fish_pink = assets.load_image("fish_pink_outline.png")
    tex_fish_red = assets.load_image("fish_red_outline.png")
    #eine funktion könnte die tilemap erstellen (30 breite x 16,875 höhe)

    #savegame save
    result = updateSavegame(player1)
    saveSavegame(result)
    #----------

def checkPriceBalance(price, balance):
    if price < balance:
        return True
    else: return False

def calcAmounth(playerObject):
    amounth = 0
    amounth += playerObject.fish_blue * 1
    amounth += playerObject.fish_brown * 2
    amounth += playerObject.fish_green * 3
    amounth += playerObject.fish_grey * 4
    amounth += playerObject.fish_orange * 5
    amounth += playerObject.fish_pink * 6
    amounth += playerObject.fish_red * 7
    return amounth

def updateSavegame(o):
    current_time = datetime.datetime.now()
    time = str(current_time.year) + str(current_time.month) +str(current_time.day) +str(current_time.hour) +str(current_time.minute) +str(current_time.second)
    return dict(name = o.name, 
                balance = o.balance,
                lastSaved = time,
                fish_blue = o.fish_blue,
                fish_brown = o.fish_brown,
                fish_green = o.fish_green,
                fish_grey = o.fish_grey,
                fish_orange = o.fish_orange,
                fish_pink = o.fish_pink,
                fish_red = o.fish_red)

def loadSavegame():
    file = open("savegame/savegame.txt", "r")
    sgData = file.read().split(",") #kommt als liste
    file.close()
    playerData = {}
    for i in sgData:
        key, value = i.split("=")
        key = key.strip() #um alle leerzeichen zu entfernen
        value = value.strip() #um alle leerzeichen zu entfernen
        playerData[key] = value    
        #alle keys und values werden als strings gespeichert. Wichtig für die Zukunft
    return playerData

def saveSavegame(d):
    saveString = ""
    lastItem = 1
    for key in d:
        value = d[key]
        if lastItem < len(d):
            saveString = saveString + f"{key} = {value},\n"
            lastItem += 1
        elif lastItem == len(d): #beim letzten eintrag sollte das Komma weggelassen werden
            saveString = saveString + f"{key} = {value}"  
    file = open("savegame/savegame.txt", "w")
    file.write(saveString)
    file.close()

main()
