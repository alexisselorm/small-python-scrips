from ast import arguments
import random

class Coin:
    def __init__(self, rare = False, clean = True, heads=True, **kwargs):
        
        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads=heads
        
        if self.is_rare:
            self.value  = self.original_value * 1.25
        else:
            self.value  = self.original_value
            
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
        
    def clean(self):
        self.colour = self.clean_colour
            
    def rust(self):
        self.colour = self.rusty_colour
            
    # def __del__(self):
    #     print("Coin spent")
    
    def __str__(self):
       if self.original_value>0.99:
           return "GHC{} coin".format(int(self.original_value))
       else:
           return "{}p coin".format(int(self.original_value * 100)) 
    def flip(self):
        heads_options=[True,False]
        choice = random.choice(heads_options)
        self.heads = choice
    
class One_Cedi(Coin):
    def __init__(self):
        data={
            "original_value":1.00,
            "clean_colour":"gold",
            "rusty_colour": "greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
        }
        super().__init__(**data)
        
class Two_Cedis(Coin):
    def __init__(self):
        data={
            "original_value":2.00,
            "clean_colour":"brownish",
            "rusty_colour": "greenish",
            "num_edges":6,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
        }
        super().__init__(**data)
        
print(Two_Cedis)
class One_pesewa(Coin):
    def __init__(self):
        data={
            "original_value":0.01,
            "clean_colour":"brownish",
            "rusty_colour": "black",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
        }
        super().__init__(**data)

class Five_Pesewas(Coin):
    def __init__(self):
        data={
            "original_value":0.05,
            "clean_colour":"silver",
            "rusty_colour": "brownish",
            "num_edges":1,
            "diameter":12.5,
            "thickness":1.15,
            "mass":5.5
        }
        super().__init__(**data)

class Ten_Pesewas(Coin):
    def __init__(self):
        data={
            "original_value":0.10,
            "clean_colour":"silver",
            "rusty_colour": "brownish",
            "num_edges":1,
            "diameter":12.5,
            "thickness":1.15,
            "mass":5.5
        }
        super().__init__(**data)

class Twenty_Pesewas(Coin):
    def __init__(self):
        data={
            "original_value":0.20,
            "clean_colour":"silver",
            "rusty_colour": "brownish",
            "num_edges":1,
            "diameter":12.5,
            "thickness":1.15,
            "mass":5.5
        }
        super().__init__(**data)
        
        
class Fifty_Pesewas(Coin):
    def __init__(self):
        data={
            "original_value":0.50,
            "clean_colour":"silver",
            "rusty_colour": "brownish",
            "num_edges":1,
            "diameter":12.5,
            "thickness":1.15,
            "mass":5.5
        }
        super().__init__(**data)

one_cedi_coin = One_Cedi()
print(one_cedi_coin.colour)
one_cedi_coin.rust()
print(one_cedi_coin.colour)

coins = [One_pesewa(),Five_Pesewas(), Ten_Pesewas(), Twenty_Pesewas(),Fifty_Pesewas(),One_Cedi(),Two_Cedis()]

for coin in coins:
    arguments = [coin,coin.colour,coin.value,coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    
    string = "{} - Colour: {}-Value : {} diameter(mm):{} ,thickness:{}, edges:{}, mass:{}".format(*arguments)
    
    print(string)