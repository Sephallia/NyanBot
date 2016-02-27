import threading

class NyanUser:

    def __init__(self, id):
        self.id = id
        self.searches = 0
        self.banned = False
        
    def PerformedSearch(self):
        self.searches += 1
        
        if self.searches >= 8:
            threading.Timer(1800.0, self.ResetSearches).start()
            
    def ResetSearches(self):
        self.searches = 0