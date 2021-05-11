# drf-restaurant-api {as a django beginer project}
> restaurant-ordering-system.\
---

## Features


####Restaurants

 * Food menu
 * Restaurant manager 
 * Order confirmation
---

####Custom user
* Login
* Registration
* Profile
* etc...
---

####Name of App
* base
* user
* food
* restaurant
* order
---

#### Used Technologies
* Docker
* Python
* Django
* Django-Rest-Framework
* JWT
* PostgreSQL
* Redis
* Postman/Insomnia 

---
## installation
---
###Linux
---
#### Step 1
```
install virtualenv
create env
workon env
pip install -r requirements.txt
```
---
#### Step 2

```
docker-compose up --build
```
---
#### Step 3

```
docker-compose exec app bash
cd src
./manage.py makemigrations
./manage.py migrate
```

