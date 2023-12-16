from typing import Any
import pandas as pd
import numpy as np 


class Dataset():
    def __init__(self):
        self.volunteers = pd.DataFrame({
            'Płeć': ['Kobieta'],
            'Lokalizacja': ['Miasto1'],
            'Rodzaj Pomocy': ['Zakupy'],
            'Stopień Samodzielności': [50],
            'język komunikacji' : ['polski'],
            'dostępność' : [40] 
            })
        self.persons_in_need = pd.DataFrame({
        'Płeć': ['Mężczyzna', 'Kobieta'],
        'Lokalizacja': ['Miasto1', 'Miasto2'],
        'Rodzaj Pomocy': ['Zakupy', 'Sprzątanie'],
        'Stopień Samodzielności': [30, 70],
        'Język komunikacji' : ['polski', 'angielski'],
        'dostępność' : [20, 40]
        # ... inne pola
        })
        self.coordinates_of_cities = {
            'Miasto1': (52.40692, 16.92993),  # Warszawa
            'Miasto2': (53.1514500,  16.7378200),  # Katowice
        }
        self.personal_info_persons = {
            "1":{'imię' : "Jan", "wiek" : 80, "opis" : """Pan Jan jest żołnierzem w stanie spoczynku. Został ranny podcza
                      a misji w Czechosłowacji. Ma problemy z lewą nogą i pomocy z zrobieniem
                      zakupów. Jest kochającym dziadkiem."""},
            "2" : {'imię' :  "Kazimierz", 'wiek':82, "opis":"""Pan Kazimierz jest emerytowanym kolejrarzem. Przepracował na kolei ponad
                        40 lat. Ma problemy z kręgosłupem i potrzebuje pomocy ze sprzątaniem."""}}
        self.personal_info_volunteers = {
            'imię' : "Asia",
            'wiek' : 22,
            'opis' : """W wolnym czasie Asia uwielbia czytać książki, uprawiać jogę 
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