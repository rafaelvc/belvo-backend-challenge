# BELVO Backend Challenge


## Install and run instructions: 

```
$git clone https://github.com/rafaelvc/belvo-backend-challenge
$cd belvo-backend-challenge
$docker-compose up -d
```

## API descriptions
### Users (users/ endpoint)
- List users
```
$http GET http://localhost:8080/users/
```
- Create a user
```
Input JSON: {"name":"user_name", "email":"user_email", "age":number_age}
```
```
$http POST http://localhost:8080/users/ < belvo-backend-challenge/UserTransAPI/test-json/user.json
```
- Get user details
Input paramenter: user_id 
```
$http GET http://localhost:8080/users/?user_id=<user_id>
```
### Transactions 
#### Add User transactions (usertransadd/ endpoint)
....
#### User's accounts balance summary (userbalance/ endpoint)
- Input paramenter: user_id 
```
$http GET http://localhost:8080/userbalance/?user_id=<user_id>
```
#### User's balance summary by category
- Input paramenter: user_id 
```
$http GET http://localhost:8080/userbalancebycategory/?user_id=<user_id>
```

## Unit tests

- Unit tests are in the ```UserTransAPI/tests.py``` file. Running the test:
```
$docker exec -it belvo-backend-1_app /bin/bash
$cd belvophase2/
$python manage.py test
```










