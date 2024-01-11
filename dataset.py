from typing import Any
import pandas as pd
import numpy as np 


class Dataset():
    def __init__(self):
        self.volunteers = pd.DataFrame({
            'gender': ['female'],
            'location': ['Miasto1'],
            'type_of_assistance': [['shopping']],
            'degree_of_independence': [50],
            'communication_language' : [['polish']],
            'availability' : [40],
            'hobby' : [['chess']],
            'coordinates_of_city' : [(52.40692, 16.92993)] 
            })
        self.persons_in_need = pd.DataFrame({
        'gender': ['male', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male','female','female', 'male'],
        'location': ["Piła", "Luboń","Poznań","Wrocław","Szczecin","Kraków","Gdańsk","Łódź","Warszawa","Bydgoszcz","Lublin","Katowice","Białystok","Rzeszów","Kielce","Olsztyn","Zielona Góra"],
        'type_of_assistance': [["reading", "writing", "gardening"],
["daily chores", "household repairs"],
["household tasks", "transportation"],
["grocery shopping", "meal preparation"],
["daily routines", "reading"],
["social skills", "employment support"],
["studio organization", "physical assistance"],
["daily life management", "therapy support"],
["home management", "knitting"],
["mobility", "daily activities"],
["communication", "community involvement"],
["eating", "dressing"],
["speech therapy", "physical exercises"],
["reading", "household tasks"],
["basic skills training", "constant care"],
["eating", "dressing"],
["daily routines", "reading"]
],
        'degree_of_independence': [30, 70,30, 40, 50, 35, 25, 60, 45, 30, 55, 50, 20, 40, 65, 50, 10],
        'communication_language' : [['polish'], ['english'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish'],['polish']],
        'availability' : [20, 40, 35, 30, 15, 25, 45, 50, 55, 60, 65, 70, 75, 80, 85, 12, 28]
,
        'hobby': [["gardening"], ["model trains"], ["knitting"], ["cooking"], ["poetry"], ["computers"], ["painting"], ["history"], ["knitting"], ["music"], ["theater"], ["chess"], ["gardening"], ["radio dramas"], ["sports"], ["radio dramas"],["knitting"]],
        'coordinates_of_city' :[(52.40692, 16.92993), (51.107883, 17.038538), (53.428543, 14.552812), (50.064651, 19.944981), (54.352025, 18.646639),
                                 (51.759249, 19.455983), (52.229676, 21.012229), (53.123482, 18.008438), (51.246454, 22.568446), (50.270908, 19.039993), 
                                 (53.132489, 23.168840), (50.041187, 21.999121), (50.866077, 20.628569), (53.770226, 20.490189), (51.935621, 15.506186),  (53.770226, 20.490189), (51.935621, 15.506186) ]
        # ... inne pola
        })
        self.coordinates_of_cities = {
    "Piła": (53.1514500, 16.7378200), # przykładowe współrzędne dla Piły
    "Luboń": (52.3472900, 16.8817800), # przykładowe współrzędne dla Lubonia
    "Poznań": (52.40692, 16.92993),
    "Wrocław": (51.107883, 17.038538),
    "Szczecin": (53.428543, 14.552812),
    "Kraków": (50.064651, 19.944981),
    "Gdańsk": (54.352025, 18.646639),
    "Łódź": (51.759249, 19.455983),
    "Warszawa": (52.229676, 21.012229),
    "Bydgoszcz": (53.123482, 18.008438),
    "Lublin": (51.246454, 22.568446),
    "Katowice": (50.270908, 19.039993),
    "Białystok": (53.132489, 23.168840),
    "Rzeszów": (50.041187, 21.999121),
    "Kielce": (50.866077, 20.628569),
    "Olsztyn": (53.770226, 20.490189),
    "Zielona Góra": (51.935621, 15.506186)
}
        self.personal_info_persons = {
            "1":{'name' : "Jan", "age" : 80, "description" : """Mr. Jan is a retired soldier. He was injured during a mission in Czechoslovakia.
                  He has problems with his left leg and needs help with shopping. He is a loving grandfather."""},
            "2" : {'name' :  "Kazimierz", 'age':82, "description":"""Mr. Kazimierz is a retired railwayman.
                    He worked on the railway for over 40 years. He has back problems and needs help with cleaning."""},
    "3":{"name": "Katarzyna", "age": 72, "description": "Katarzyna is a former teacher who struggles with vision problems. She has dedicated her life to education and now needs assistance in reading and writing correspondence. Katarzyna enjoys gardening but requires help in maintaining her garden. She has a deep love for classical music."},
    "4":{"name": "Piotr", "age": 68, "description": "Piotr is a retired mechanic who suffers from arthritis. He spent years fixing cars and now finds it hard to manage household repairs. Piotr needs help with daily chores and is passionate about model trains."},
    "5" :{"name": "Agnieszka", "age": 35, "description": "Agnieszka is a single mother battling a chronic illness. She struggles to balance her health needs with caring for her two young children. Agnieszka needs assistance with daily household tasks and transportation to medical appointments."},
    "6": {"name": "Marek", "age": 79, "description": "Marek is an elderly widower who lives alone. He has mobility issues due to a recent hip surgery. Marek loves cooking but now needs help with grocery shopping and meal preparation. He is an avid bird watcher."},
    "7":{"name": "Zofia", "age": 76, "description": "Zofia is a former librarian with early-stage Alzheimer's. She needs assistance with daily routines and enjoys reminiscing about her days among books. Zofia loves poetry and needs someone to read to her."},
    "8":{"name": "Tomasz", "age": 24, "description": "Tomasz is a young adult with autism. He is highly skilled in computers but struggles with social interactions. Tomasz needs support in developing social skills and pursuing employment opportunities."},
    "9":{"name": "Magdalena", "age": 50, "description": "Magdalena is a cancer survivor who experiences fatigue and physical limitations. She is an artist who now requires help in setting up and organizing her studio. Magdalena is passionate about painting landscapes."},
    "10":{"name": "Stefan", "age": 65, "description": "Stefan is a veteran who suffers from PTSD. He needs support in managing his daily life and attending therapy sessions. Stefan has a keen interest in history and enjoys visiting museums."},
    "11":{"name": "Dorota", "age": 70, "description": "Dorota is a retired nurse with severe rheumatoid arthritis. She spent her life caring for others and now needs care herself. Dorota loves knitting and requires assistance in managing her home."},
    "12":{"name": "Andrzej", "age": 58, "description": "Andrzej is a former construction worker who suffered a severe back injury. He needs help with mobility and daily activities. Andrzej is a fan of classic rock music and plays the guitar."},
    "13":{"name": "Helena", "age": 81, "description": "Helena is a retired school principal who has lost much of her hearing. She needs assistance with communication and enjoys attending local theater productions. Helena is active in her community and loves mentoring young people."},
    "14":{"name": "Wojciech", "age": 77, "description": "Wojciech is an elderly man with Parkinson's disease. He struggles with tremors and needs help with eating and dressing. Wojciech is a former chess champion and enjoys playing chess with visitors."},
    "15":{"name": "Ewa", "age": 62, "description": "Ewa is a middle-aged woman recovering from a stroke. She requires help with speech therapy and physical exercises. Ewa is an avid gardener and bird enthusiast."},
    "16":{"name": "Krystyna", "age": 69, "description": "Krystyna is a retired seamstress with failing eyesight. She needs help with reading and household tasks. Krystyna enjoys listening to radio dramas and has a vast collection of vintage clothing."},
    "17":{"name": "Michał", "age": 30, "description": "Michał is a young man who suffered a traumatic brain injury in an accident. He is relearning basic skills and needs constant care and support. Michał is passionate about sports and enjoys watching soccer matches."}}
        self.personal_info_volunteers = {
            'name' : "Asia",
            'age' : 22,
            'description' : """In her free time, Asia loves to read books, practice yoga,
              and explore new places. Her interests make it easy for her to connect with various people.
                Always ready to help, Asia is particularly interested in activities related to caring for the elderly, 
                but she is also eager to engage in helping children and youth."""
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