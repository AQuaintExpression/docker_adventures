bb# Introduction to PostgreSQL

The primary focus is getting PostgreSQL up and running and </br>
taking a first look at the database. </br>

PostgreSQL [Docker Image](https://hub.docker.com/_/postgres)

## Run a simple PostgreSQL database (docker)

```
 docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

## Run a simple PostgreSQL database (compose)

```
docker compose up
```

We can access our database from the adminer web page on `http://localhost8080` </br>


When running containers, its always important to pull the image by tag </br>
to ensure you always get the same container image, else it will pull latest. </br>
We will do that in the next step. </br>

## Persisting Data

To persist data to PostgreSQL, we simply mount a docker volume. </br>
This is the way to persist container data. </br>
PostgreSQL stores its data by default under `/var/lib/postgresql/data` 
Also take note we are running a specific version of PostgreSQL now:

```
docker run -it --rm --name postgres `
  -e POSTGRES_PASSWORD=admin123 `
  -v ${PWD}/pgdata:/var/lib/postgresql/data `
  postgres:16.3
```

We can enter the container to connect to SQL:

```
# enter the container
docker exec -it postgres bash

# login to postgres
psql -h localhost -U postgres

#create a table
CREATE TABLE customers (firstname text,lastname text, customer_id serial);

#add record
INSERT INTO customers (firstname, lastname) VALUES ( 'Bob', 'Smith');

#show table
\dt

# get records
SELECT * FROM customers;

# quit 
\q

```

Now we can see our data persisted by killing and removing the container:

```
docker rm -f postgres
```

Run it again with the above `docker run` command and list our record with the above commands we've learnt </br>

## Networking

PostgreSQL by default uses port `5432`. </br>
Since we are running in Docker, we can bind a different port if we wish with Docker's `-p` flag. </br>
For example, we can expose port `5000` outside the container :

```
docker run -it --rm --name postgres `
  -e POSTGRES_PASSWORD=admin123 `
  -v ${PWD}/pgdata:/var/lib/postgresql/data `
  -p 5000:5432 `
  postgres:16.3
```
Note that this does not change the port which PostgreSQL runs on. </br>
To change that, we need to explore the configuration.

## Configuration 

PostgreSQL can be configured using environment variables as well as a config file. </br>

PostgreSQL has a ton of configuration options. </br>
In the next chapter, we will explore the configuration of PostgreSQL. </br>

## Docker Compose

Let's update our compose file to reflect our latest changes. </br>

We need to update the docker image, the port we want to expose outside of the container as well as a volume mount for persistence. </br>

```
version: '3.1'
services:
  db:
    image: postgres:16.3
    restart: always
    environment:
      POSTGRES_PASSWORD: admin123
    ports:
    - 5000:5432
    volumes:
    - ./pgdata:/var/lib/postgresql/data
  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
```

## Update the docker-compose.yaml file 

Here we need to update the file to contain yet another service that will handle the aquisition + data processing. </br>

We need to create a new volume mapping for the kaggle.json file as well. </br>

First connect to your kaggle account (or create one if you don't have it and download the kaggle.json file --> Profile -> Settings -> API -> Create New Token). </br>

After you have downloaded the file open a powershell prompt in the folder where the `kaggle.json` file has been saved and execute the following command: </br>
`mv kaggle.json $ENV:USERPROFILE\.kaggle\`



