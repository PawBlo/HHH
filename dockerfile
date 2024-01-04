# Użyj obrazu Pythona jako podstawy
FROM python:3.8

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Sklonuj repozytorium z Git
RUN git clone https://github.com/PawBlo/HHH.git .


# Zainstaluj zależności Pythona
RUN pip install -r  requirements.txt

# Przekieruj port 8080
EXPOSE 8080

# Uruchom aplikację przy użyciu Uvicorn
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]