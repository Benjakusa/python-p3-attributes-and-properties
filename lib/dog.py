#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        
        # Handle name: if None, don't set; if empty string, validate (will fail)
        if name is not None:
            self.name = "" if name == "" else name
        
        # Handle breed: if None, don't set; if empty string, validate (will fail)
        if breed is not None:
            self.breed = "" if breed == "" else breed
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)
    
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    breed = property(get_breed, set_breed)