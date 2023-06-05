# PyBank

A simple python api using Flask, SQL Alchemy, Postgres and Docker for study only. It makes some transactions through accounts changing their balance.

## Running the application

Simply call:<br>
<code>docker-compose up</code>

> After docker is running you need to enter in application container and run migrations:

>> - <code>$ docker exec -it api bash</code><br>
>> - <code>$ flask db init</code><br> 
>> - <code>$ flask db migrate</code><br> 
>> - <code>$ flask db upgrade</code><br>
