# BELVO Backend Challenge



## Install and run instructions: 

```
$git clone https://github.com/rafaelvc/belvo-backend-challenge
$cd belvo-backend-challenge
$docker-compose up -d
```

## API descriptions
### Users (*users/* endpoint)
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
#### Add User transactions (*usertransadd/* endpoint)
Input is a list of one or many User's transactions:
``` 
$echo '[{"reference": "000051", "account": "C00099", "date": "2020-01-03", "amount": -51.13, "type": "outflow", "category": "groceries", "user_id": 1}]' | http POST http://localhost:8080/usertransadd/
```
Output: the list of Transactions were added
#### User's accounts balance summary (*userbalance/* endpoint)
- Input paramenter: user_id 
```
$http GET http://localhost:8080/userbalance/?user_id=<user_id>
```
Json Output:
```
[{
        "account": "C00099",
        "balance": 1738.87,
        "total_inflow": 2500.72,
        "total_outflow": -761.85
    },
    {
        "account": "S00012",
        "balance": 150.72,
        "total_inflow": 150.72,
        "total_outflow": 0
    }
]
```

#### User's balance summary by category (*userbalancebycategory/* endpoint)
- Input paramenter: user_id
- Input parameter: date_begin (YYYY-MM-DD)
- Input parameter: date_end (YYYY-MM-DD)
```
$http GET http://localhost:8080/userbalancebycategory/?user_id=<user_id>&date_begin=<date>&date_end=<date>
```
Json Output:
```
{
    "inflow": {
        "salary": 2500.72,
        "savings": 150.72
    },
    "outflow": {
        "groceries": -102.26,
        "rent": -560.0,
        "transfer": -150.72
    }
}
```
## Unit tests

- Unit tests are located in the ```UserTransAPI/tests.py``` file. Running the test:
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


- *I see a bottleneck during the User's accounts balance summary API processing. My suggestion is to create a database model Account and add the outflow and inflow balances fields to it. Then inflow/outflow balances are updated  when the transaction is just added. That will prevent using aggregations queries to process account balances diminishing drastically database processing. The information asked is just there already computed.*

- *The same idea might be applied for the User's balance summary by category. We should also update the inflow/outflow balances by category for each Transaction which is added. That will prevent using aggregations queries to process account balances diminishing drastically database processing. The information asked is just there already computed.*

- *I would use a more robust database such as PostgreSQL.*


