class SmallTv:
    def __init__(self,brand,price,warrenty):
        self.brand=brand
        self.price=price
        self.warrenty=warrenty
    def sound(self):
        print("the sound look like very clearly")
    def colourless(self):
        print("This smalltv pictures full of shown in colourless")
class ColourTv(SmallTv):
    def __init__(self,brand,price,warrenty,remote):
        super().__init__(brand,price,warrenty)
        self.remote=remote
    def colour(self):
        print("The colourtv shown in colour pictures")
    def gaming(self):
        print("playing apple catch game")
class SmartTv(ColourTv):
    def __init__(self,brand,price,warrenty,remote,setupbox,pendrive):
        super().__init__(brand,price,warrenty,remote)
        self.setupbox=setupbox
        self.pendrive=pendrive
    def AnimationEffect(self):
        print("playing vedio games and using internet connection")
Micromax=SmartTv("honda",35000,1,"yes","airtel","USP")
Micromax.sound()
Micromax.colourless()
Micromax.gaming()
Micromax.AnimationEffect()
     
