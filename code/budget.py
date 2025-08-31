from envelope import *

class Budget:
    def __init__(self, default_envelopes = None):
        self.envelopes = {}
        
        # Add default envelopes
        if default_envelopes:
            for name in default_envelopes:
                self.add_envelope(name)
        
    def add_envelope(self, name):
        self.envelopes[name] = Envelope(name)
        print(f"Added envelope: {name}\n")
        
    def deposit(self, name, amount):
        if name in self.envelopes:
            self.envelopes[name].deposit(amount)
            print(f"Deposited ${float(amount)} into envelope: {name}\n")
        else:
            print("envelope does not exist")
        
    def spend(self, name, amount):
        if name in self.envelopes:
            self.envelopes[name].spend(amount)
            print(f"Spent ${float(amount)} from envelope: {name}\n")
        else:
            print("Envelope does not exist")
        
    def print_all_envelopes(self):
        for env in self.envelopes:
            self.envelopes[env].load_contents()