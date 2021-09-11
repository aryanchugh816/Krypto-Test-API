# Krypto Test API - Crypto Price Tracker

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose -f docker-compose.prod.copy.yml up --build
```

Open the logs associated with the `celery` service to see the tasks running periodically:

```sh
$ docker-compose logs -f 'celery'
```
---

## Features implemented
- [x] JWT Auth for users with Register, Login, Logout, Email Confirmation & Password Reset by Email
- [x] All API Endpoints as specified in the task sheet
- [x] Implemented extra worker for cronjob of scraping prices and sending  mass email so that main API endpoints never block up and only the celery worker will be scaled if necessary
- [x] Used RabbitMQ as message broker (as is best to retain data when container crashes) and celery as result backend to distribute the load on Postgres - primary backend database
- [x] Wrapped everything in a single docker-compose file with all the required data and env files supplied in this repository
- [ ] This can be easily hosted on any cloud provider using github actions to form a CI/CD pipeline as everything is wrapped in a docker container

## API Endpoints
**All the endpoints are documented using a swagger documentation at */api/*, port: 8000**

**Main endpoints listed below**

| Endpoint | Description |
| -------- | ----------- |
| /api/auth/ | Endpoints for user auth |
| /api/auth/register | Register a user using email and password |
| /api/auth/login | Login a user to receive *access* and *refresh* JWT tokens |
| /api/auth/logout | Used to logout a user and makes both JWT tokens useless to the backend as refresh token is blacklisted |
| /api/event/ | Endpoints related to tracking of crypto currency (Only accessible by authorised users) |
| [GET]/api/event/ | Used to get a list of tracking events issued by user |
| [POST]/api/event/ | Used to place new event tracker |
| [PATCH]/api/event/{id}/ | Used to partially update an event tracker |
| [DELETE]/api/event/{id}/ | Used to delete an event tracker |
---

## Architecture Summary
The backend is developed on *Django* with implementation of REST architecture using *Django REST Framework*. For periodic tasks *Celery* and *Celery Beat* are used and taks scheduling is mentioned in themain *settings.py* file. *RabbitMQ* is used as the message broker (as it helps in retaining data when container crashes) and *Reddis* as result backend. *Postgres* is used as the primary database for django backend.

## Future Work
A lot of features can be implemented for this tracker besides email updates like 
- Insights and analytics dashboard using ml models 
- Tracking and forcasting time-series for selected crypto currency using deep learning model as a paid subscription
- Customizable reinforcement learning bots to help trade several currencies with ease and automate minor pipelines
- Target customers by implementing a marketplace to directly buy&sell currencies and hire mentors for professional expertise with a minimal cost on each transaction coming to Krypto

With minimal efforts this application can be clustered using kubernetes and few more technologies and a dedicated frontend and load balancer which will help manage future high bandwidth as it supports auto scaling  both horizontally and vertically

---


## Name: Aryan CHugh
## College Registration ID: 18BIT0307
## Work Email: chugharyan816@gmail.com
## Mobile Number: 9999600340