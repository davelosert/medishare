# Medishare - a WirVSVirus Hackthon Project
This Project was developed during the [wirvsvirus-hackathon](https://wirvsvirushackathon.org/) from 20th - 22nd March 2020.
It is a prototype of the medishare app - described in detail on our [DevPost-Page]().

The app was developed with a Pyhon-Backend, MySQL-Database and Vue-Frontend.

# Setup
To make it run, follow these steps:

In order for the project to run 

1. Install [NodeJS](https://nodejs.org/en/) as well as [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/install/) on your machine.

2. Build the Frontend:
```
    cd frontend && npm install && npm run build
```
3. Start the App:
```
    ./start.sh
```
This will run `docker-compose` and start three containers: `medishare-nginx`, `medishare-mysql` and `medishare-backend`. The website is exposed on Port 80, so you can view the app by navigating to http://localhost

The API is reachable under http://localhost/api (e.g. http://localhost/api/categories/)

You can stop the app and clean up by exeuting `./stop.sh`.
