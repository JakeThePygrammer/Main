class Gamer:
    def __init__(self,level,rizz,username,robux,aura):
        self.level = level
        self.rizz = rizz
        self.username = username
        self.robux = robux
        self.aura = aura
    def __str__(self):
        return f"Gamer stats: username = {self.username}, rizz = {self.rizz}, robux = {self.robux}, level = {self.level}, aura = {self.aura}, "
g1 = Gamer(34, 10, "SkibidiNoRizz1", 99, -1000)
g2 = Gamer(28, 69, "SkibidiUltraRizzer123abc", 1000, 1500)
g3 = Gamer(56, 25, "mamamamamkmkmk", 2200, 999)
max_aura = 0
list_gamers = [g1,g2,g3]
for index in list_gamers:
    if index.aura > max_aura:
        max_aura = index.aura
        max_aura_gamer = index
print(f"{max_aura_gamer.username} has the most aura, with {max_aura_gamer.aura} aura.")

