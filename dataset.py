from typing import Any
import pandas as pd
import numpy as np 


class Dataset():
    def __init__(self):
        self.volunteers = pd.DataFrame({
            'gender': ['female'],
            'location': ['Miasto1'],
            'type_of_assistance': ['shopping'],
            'degree_of_independence': [50],
            'communication_language' : ['polish'],
            'availability' : [40] 
            })
        self.persons_in_need = pd.DataFrame({
        'gender': ['male', 'female'],
        'location': ['Miasto1', 'Miasto2'],
        'type_of_assistance': ['shopping', 'cleaning '],
        'degree_of_independence': [30, 70],
        'communication_language' : ['polish', 'english'],
        'availability' : [20, 40]
        # ... inne pola
        })
        self.coordinates_of_cities = {
            'Miasto1': (52.40692, 16.92993),  # Warszawa
            'Miasto2': (53.1514500,  16.7378200),  # Katowice
        }
        self.personal_info_persons = {
            "1":{'name' : "Jan", "age" : 80, "description" : """Pan Jan jest żołnierzem w stanie spoczynku. Został ranny podcza
                      a misji w Czechosłowacji. Ma problemy z lewą nogą i pomocy z zrobieniem
                      zakupów. Jest kochającym dziadkiem."""},
            "2" : {'name' :  "Kazimierz", 'age':82, "description":"""Pan Kazimierz jest emerytowanym kolejrarzem. Przepracował na kolei ponad
                        40 lat. Ma problemy z kręgosłupem i potrzebuje pomocy ze cleaning m."""}}
        self.personal_info_volunteers = {
            'name' : "Asia",
            'age' : 22,
            'description' : """W wolnym czasie Asia uwielbia czytać książki, uprawiać jogę 
            oraz eksplorować nowe miejsca. Jej zainteresowania pozwalają jej łatwo nawiązywać
              kontakt z różnymi osobami. Zawsze gotowa do pomocy,
                Asia jest szczególnie zainteresowana działaniami związanymi z opieką 
                nad seniorami, ale także chętnie angażuje się w pomoc dzieciom i młodzieży."""
        }
    def get_persons(self):
        return self.persons_in_need
    def get_volunteers(self):
        return self.volunteers
    def get_personal_info_persons(self):
        return  self.personal_info_persons
    def get_personal_info_volunteers(self):
        return self.personal_info_volunteers
    def get_coordinates_of_cities(self):
        return self.coordinates_of_cities