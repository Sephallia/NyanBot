import threading

class NyanUser:

    def __init__(self, id):
        self.id = id
        self.searches = 0
        self.banned = False
        
    def PerformedSearch(self):
        self.searches += 1
        
        # If they do a bunch of searches all at once, block them for half an hour.
        if self.searches >= 8:
            threading.Timer(1800.0, self.ResetSearches).start()
        # Otherwise, the search counter will decay 5 minutes after their search
        else:
            threading.Timer(600.0, self.DecrementSearches).start()
    
    def DecrementSearches(self):
        # We don't want to decrement if they've spammed so much that they're
        # temporarily blocked.
        if (self.searches > 0 and self.searches < 8):
            self.searches -= 1
    
    def ResetSearches(self):
        self.searches = 0