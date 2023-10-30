# BoB-BackendPart

A repository for the BoB API server using Django and Postgresql

## Table Of Contents
- [System Architecture](#system-architecture)
- [Running the server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Directory Structure](#directory-structure)
- [License](#license)

## System Architecture

- Python Django
- postgresql

## Running the server

First, Clone this repository.
```
git clone https://github.com/LSTM2023/BoB-BackendPart.git
```

Before you run the server, you should install docker, docker-compose.

And then, Run the following command.
```
docker-compose up --build -d
```

## API Endpoints

List of available routes:

### User information routes
`/api/user/login` : User login

`/api/user/exist/` : Is User Exist

`/api/user/edit/` : User edit

`/api/user/registration/` : User registration

`/api/user/remove/` : User remove

`/api/user/ftoken/retrieve/` : User firebase token retrieve

`/api/user/ftoken/update/` : User firebase token update

`/api/user/find/email/` : User password search by email

### Baby information routes
`/api/baby/list/` : Baby list

`/api/baby/set/` : Baby registration

`/api/baby/<int:babyid>/get/` : Baby search

`/api/baby/<int:babyid>/delete/` : Baby delete

`/api/baby/modify/` : Baby modification

### User-Baby relationship information routes
`/api/baby/lists/` : User-Baby relationship list

`/api/baby/connect/` : User-Baby relationship registration

`/api/baby/rearer/` : Baby's rearer search

`/api/baby/activate/` : Baby's rearer activate

### Baby life information routes
`/api/life/list/` : Baby's life information list

`/api/life/lists/` : Specific Baby's life list

`/api/life/set/` : Baby's life registration

`/api/life/<int:babyid>/get/` : Specific baby's life search

### Baby growth information routes
`/api/growth/list/` : Baby's growth information list

`/api/growth/set/` : Baby's growth information registration

`/api/growth/<int:babyid>/get/` : Baby's growth information search

### Baby health screenings/vaccination information routes
`/api/health/list/` : Baby health screenings/vaccination information list

`/api/health/set/` : Baby health screenings/vaccination information registration

`/api/health/<int:babyid>/get/` : Baby health screenings/vaccination information search

### Baby diary information routes
`/api/daily/list/` : Baby diary information list

`/api/daily/lists/` : Specific baby diary information list

`/api/daily/set/` : Baby diary information registration

`/api/daily/get/` : Baby diary information search

`/api/daily/edit/` : Baby diary information modification

`/api/daily/delete/` : Baby diary inforatmion delete

## Directory Structure
```
BoB-Backend
├── Dockerfile
├── LICENSE
├── LICENSE.bak
├── LICENSE_3rd
├── README.md
├── bob_project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── settings.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── wsgi.cpython-311.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── lstm_api
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   └── urls.cpython-311.pyc
│   ├── account
│   │   ├── __pycache__
│   │   │   ├── adapters.cpython-311.pyc
│   │   │   └── api.cpython-311.pyc
│   │   ├── adapters.py
│   │   ├── api.py
│   │   └── serializers.py
│   ├── admin.py
│   ├── apps.py
│   ├── baby
│   │   ├── __pycache__
│   │   │   ├── api.cpython-311.pyc
│   │   │   └── serializers.cpython-311.pyc
│   │   ├── api.py
│   │   └── serializers.py
│   ├── daily_note
│   │   ├── __pycache__
│   │   │   ├── api.cpython-311.pyc
│   │   │   └── serializers.cpython-311.pyc
│   │   ├── api.py
│   │   └── serializers.py
│   ├── growth_log
│   │   ├── __pycache__
│   │   │   ├── api.cpython-311.pyc
│   │   │   └── serializers.cpython-311.pyc
│   │   ├── api.py
│   │   └── serializers.py
│   ├── health_check
│   │   ├── __pycache__
│   │   │   ├── api.cpython-311.pyc
│   │   │   └── serializers.cpython-311.pyc
│   │   ├── api.py
│   │   └── serializers.py
│   ├── life_log
│   │   ├── __pycache__
│   │   │   ├── api.cpython-311.pyc
│   │   │   └── serializers.cpython-311.pyc
│   │   ├── api.py
│   │   └── serializers.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_userbabyrelationship_relation.py
│   │   ├── 0003_user_is_staff.py
│   │   ├── 0004_remove_user_relation_user_phone.py
│   │   ├── 0005_auto_20230406_2222.py
│   │   ├── 0006_alter_userbabyrelationship_relation.py
│   │   ├── 0007_userbabyrelationship_active.py
│   │   ├── 0008_auto_20230414_0920.py
│   │   ├── 0009_auto_20230414_0927.py
│   │   ├── 0010_auto_20230414_1031.py
│   │   ├── 0011_auto_20230414_1032.py
│   │   ├── 0012_auto_20230421_0914.py
│   │   ├── 0013_healthcheck_date.py
│   │   ├── 0014_auto_20230724_2206.py
│   │   ├── 0015_user_token.py
│   │   ├── 0016_rename_token_user_ftoken.py
│   │   ├── 0017_rename_ftoken_user_token.py
│   │   ├── 0018_dailynote.py
│   │   ├── 0019_alter_dailynote_photo.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── 0002_userbabyrelationship_relation.cpython-311.pyc
│   │       ├── 0003_user_is_staff.cpython-311.pyc
│   │       ├── 0004_remove_user_relation_user_phone.cpython-311.pyc
│   │       ├── 0005_auto_20230406_2222.cpython-311.pyc
│   │       ├── 0006_alter_userbabyrelationship_relation.cpython-311.pyc
│   │       ├── 0007_userbabyrelationship_active.cpython-311.pyc
│   │       ├── 0008_auto_20230414_0920.cpython-311.pyc
│   │       ├── 0009_auto_20230414_0927.cpython-311.pyc
│   │       ├── 0010_auto_20230414_1031.cpython-311.pyc
│   │       ├── 0011_auto_20230414_1032.cpython-311.pyc
│   │       ├── 0012_auto_20230421_0914.cpython-311.pyc
│   │       ├── 0013_healthcheck_date.cpython-311.pyc
│   │       ├── 0014_auto_20230724_2206.cpython-311.pyc
│   │       ├── 0015_user_token.cpython-311.pyc
│   │       ├── 0016_rename_token_user_ftoken.cpython-311.pyc
│   │       ├── 0017_rename_ftoken_user_token.cpython-311.pyc
│   │       ├── 0018_dailynote.cpython-311.pyc
│   │       ├── 0019_alter_dailynote_photo.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── urls.py
│   ├── user
│   │   ├── __pycache__
│   │   │   ├── api.cpython-311.pyc
│   │   │   └── serializers.cpython-311.pyc
│   │   ├── api.py
│   │   └── serializers.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## License
BoB-BackendPart is released under the LGPL-3.0 License.
