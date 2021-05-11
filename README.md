# drf-restaurant-api {as a django beginer project}
> restaurant-ordering-system.\
---

## Features


*Restaurants
	* Food menu
 * Restaurant manager 
	* Order confirmation

*Custom user
* **Login**
 * Registration
 * Profile
 * Admin Order management dashboard
 **(Only for superuser)**
 * etc...


## Used Technologies
* Docker
* Python
* Django
* Django-Rest-Framework
* JWT
* PostgreSQL
* Redis
* Postman/Insomnia 

## installation
#### Step 1
```install virtualenve
create env
workon dir
pip install -r requirements.txt ```

####Step 2

```docker-compose up --build```

## run commands
```docker-compose exec app bash
cd src
./manage.py makemigrations
./manage.py migrate```

