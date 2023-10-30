# BoB-BackendPart

A repository for the BoB API server using Django and Postgresql

## Table Of Contents
- [System Architecture](#system-architecture)
- [Running the server](#running-the-server)
- [API Endpoints](#api-endpoints)

## System Architecture

- Python Django
- postgresql

## Running the server

Before you wanna run the server, you should install docker, docker-compose

And then, Run the following command
```
docker-compose up --build -d
```

## API Endpoints

List of available routes:

### User routes
`/api/user/login` : User login
`/api/user/exist/` : Is User Exist

## License
BoB-BackendPart is released under the LGPL-3.0 License.
