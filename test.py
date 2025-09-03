import datetime

class player():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def add(self, coins):
        self.balance = int(self.balance) + coins



def main():
    loadedPlayerData = loadSavegame()
    player1 = player(loadedPlayerData["name"], int(loadedPlayerData["balance"]))

    #player1.add(10) #nur zum testen

    result = updateSavegame(player1)
    saveSavegame(result)

def updateSavegame(o):
    current_time = datetime.datetime.now()
    time = str(current_time.year) + str(current_time.month) +str(current_time.day) +str(current_time.hour) +str(current_time.minute) +str(current_time.second)
    return dict(name = o.name , balance = o.balance, lastSaved = time)

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
            saveString = saveString + f"{key} = {value},"
            lastItem += 1
        elif lastItem == len(d): #beim letzten eintrag sollte das Komma weggelassen werden
            saveString = saveString + f"{key} = {value}"  
    file = open("savegame/savegame.txt", "w")
    file.write(saveString)
    file.close()

main()
