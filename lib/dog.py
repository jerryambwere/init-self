#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt"):
        self.breed=breed
        self.name=name
    pass
cindy=  Dog("Cindy","Shephered")
print(cindy.breed)
print(cindy.name)