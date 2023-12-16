from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
import pandas as pd
import math
from dataset import Dataset
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def calculate_distance(volunteer, person, coordinates_of_cities ):
    lat1, lon1 = coordinates_of_cities[volunteer['Lokalizacja']]
    lat2, lon2 = coordinates_of_cities[person['Lokalizacja']]
    return haversine(lat1, lon1, lat2, lon2)
def predict():
    dataset = Dataset()
    person_data = dataset.get_persons()
    volunteer_data = dataset.get_volunteers()
    person_data['Odległość od Wolontariusza'] = person_data.apply(
        lambda row: calculate_distance(volunteer_data.iloc[0], row, dataset.get_coordinates_of_cities()), axis=1)
    scaler = MinMaxScaler()
    encoder = OneHotEncoder()
    person_data[['Stopień Samodzielności']] = scaler.fit_transform(person_data[['Stopień Samodzielności']])
    volunteer_data[['Stopień Samodzielności']] = scaler.transform(volunteer_data[['Stopień Samodzielności']])
    encoded_categorical = encoder.fit_transform(pd.concat([person_data.iloc[:, :3], volunteer_data.iloc[:, :3]])) 
    encoded_data = np.hstack([
    encoded_categorical.toarray(), 
    np.vstack([
        person_data.iloc[:, 3].values.reshape(-1, 1),  # Zmiana kształtu na (2, 1)
        volunteer_data.iloc[:, 3].values.reshape(1, 1)  # Zmiana kształtu na (1, 1)
        ])
    ])
    encoded_volunteers = encoded_data[-1:]
    encoded_persons = encoded_data[:-1]
    similarity_scores = cosine_similarity(encoded_volunteers, encoded_persons)
    return similarity_scores
