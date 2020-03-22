# Medishare - a WirVSVirus Hackthon Project
This Project was developed during the [wirvsvirus-hackathon](https://wirvsvirushackathon.org/) from 20th - 22nd March 2020.

SETUP python envronment: "pip install -r requirements.txt"  
RUN: "python .\medishare.py"  

Starte aktuell auf: "http://localhost:8080/"  

Connection für DB:  
SQLite lokal: thisapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  
ODER  
MySQL: thisapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://medishare:test123@medishare-mysql:3306/medishare'


Open topics:
  + publish to production web server, as build in flask server is not for realtime production cases  
  + search api for different search scenarios  
  + complete user management and authentication
