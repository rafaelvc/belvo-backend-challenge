# BELVO Backend Challenge


## Install and run instructions: 

```
$git clone https://github.com/rafaelvc/belvo-backend-challenge
$cd belvo-backend-challenge
$docker-compose up -d
```

## API descriptions
### Users (users/ endpoint)
*List users*
```
$http GET http://localhost:8080/users/
```
Output:
``` [ {"name":"user1", email:"email1", "age":99 }, ... ]```

*Create a user*

```$http POST http://localhost:8080/users/ name='Rafael Cabral' email=rafael@tryingbelvo.com age=33```

Output:
``` {"name":"Rafael Cabral", email:"rafael@tryingbelvo.com", "age":33 }```

*Get user details*

Input paramenter: *user_id* 
```
$http GET http://localhost:8080/users/?user_id=1
```
Output: ```{"name":"Rafael Cabral", email:"rafael@tryingbelvo.com", "age":33 }```

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
## Perforamce discussion

> Can you highlight the parts of the application that are likely to be performance
bottlenecks when the user base grows to, say, 10 million users? How would you solve
them (you don’t need to solve them in code, just outlining and explaining the strategy to
solve them is sufficient).








