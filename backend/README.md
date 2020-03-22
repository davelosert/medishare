# Backend

## Folder db

This folder contains two Python modules that create the medishare database in MySQL.

## docker file

This docker file contains the building instructions for a modified MySQL Docker image. Python is installed here and the modules for building the database are called. As soon as a container is created from this docker image, the database is available.

## docker-compose

This file is used to build a docker stack containing MySQL with the database medishare. Furthermore a nginx webserver is included.
