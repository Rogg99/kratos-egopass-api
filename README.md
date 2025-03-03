# KRATOS TEST PAYMENT BACKEND

## Name

Kratos Test PAYMENT API

## Description

Ce projet decline le backend de l'application de Paiement des EGOPASS de test de l'entreprise KRATOS Inc.


## Prerequis
- Docker v4.35 or later


## Installation

- docker compose build

- docker compose up server

### make migration

- docker compose run --rm -it django makemigrations

### migrate

- docker compose run --rm -it django migrate

### charger les données de test dont le compte admin
- docker compose run --rm -it django initialize_datas
 
### URLs

- console d'administration django
    - URL:  [http://localhost:7899/kratos-payment/api/v1/admin/] ou 
    [http://localhost:454/kratos-payment/api/v1/admin/] 
    - username: admin
    - password: admin

- url de la documentation:
    - [http://localhost:454/kratos-payment/api/] 
    - [http://localhost:7899/kratos-payment/api/] 
    