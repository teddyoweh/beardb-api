# BearDB MicroService

![beardbimg](https://www.beardb.net/assets/logo.d0f8a85f.png)
A microservice using the Beardb database system is a standalone service that is designed to deploy JSON databases remotely and provide API endpoints for accessing the data stored in these databases. This microservice utilizes the Beardb database system, which is a highly scalable and flexible database management system that is specifically designed to handle large amounts of data in the form of JSON documents.

The microservice provides a set of API endpoints that allow users to retrieve data from the JSON databases that are deployed on the server. These API endpoints can be accessed using HTTP POST requests, and they return data in the form of JSON objects. This allows users to easily access and manipulate the data stored in the databases, and it also enables them to integrate the microservice with other systems and applications.



## Introduction
 

### Install Libaries
```sh
$ python3 -m pip install BeardbAPI 
```
```sh
$ python3 -m pip install gunicorn
```

### Import Libraries
```py
from BeardbAPI.API import BeardbAPI
```
#### Running the Development MicroService
run.py
```py
test = BeardbAPI()
test.run(host='127.0.0.1',port=5555)
```
Terminal
```sh
$ python3 run.py
```
#### Running the Production MicroService
run.py
```py
test = BeardbAPI()
api = test.service()
```
Terminal
```sh
$ gunicorn run:api
```
The file system automatically starts the database environment in the current directory of the driver code.
To avoid that pass in the directory you want to make the database enviroment.
Run the following code
```py
test.storage(app_name='test_app',dir='')
```
#### Optimal Driver Code (Development)
run.py
```py
test = BeardbAPI()
test.storage(app_name='test_app',dir='')
test.run(host='127.0.0.1',port=5555)
```
Terminal
```sh
$ python3 run.py
```
#### Optimal Driver Code (Production)
run.py
```py
test = BeardbAPI()
test.storage(app_name='test_app',dir='')
api = test.service()
```
Terminal
```sh
$ gunicorn run:api
```
# API Documentation

## API Endpoints
```sh
[POST] - \me
[POST] - \newuser
[POST] - \newproject
[POST] - \newdatabase
[POST] - \newbucket
[POST] - \insertdata
[POST] - \fetchdata
[POST] - \fetchbyid
[POST] - \updatebyid
[POST] - \updatedata
[POST] - \deletedata
[POST] - \deletebyid
[POST] - \getbuckets
[POST] - \getdatabases
[POST] - \getprojects
```

## API QuickStart
To access any of the endpoint you have to include your email and secret in the body of the API Request.

```json
{
"email":"teddyoweh@gmail.com"
"secret":"a60e1bb1be7fc59ea08378f2840a8a4f44c07d19b315c3e78a279660a3f8a6f5"
}
```
You can get you secret by creating a new user, steps to do so is listed in the API GUIDES Below
All of the endpoints require only a **POST** Method

# API GUIDES
- [Create New User](#create-new-user)
- [Get User Data](#get-user-data)
- [Create Project](#create-project)
- [Create Database](#create-database)
- [Create Bucket](#create-bucket)
- [Insert Data](#insert-data)
- [Update Data With Query](#update-data-with-query)
- [Update Data With ID](#update-data-with-id)
- [Fetch Data With Query](#fetch-data-with-query)
- [Fetch Data With ID](#fetch-data-with-query)
- [Delete Data With Query](#delete-data-with-query)
- [Delete Data With ID](#delete-data-with-id)
- [Get Projects](#get-projects)
- [Get Databases](#get-databases)
- [Get Buckets](#get-buckets)

## Headers
```sh
Server: gunicorn
Date: Wed, 14 Dec 2022 08:11:34 GMT
Connection: close
Content-Type: application/json
Content-Length: 582
Access-Control-Allow-Origin: *
```

## Create New User
### Body
- email
- fullname
- password
### Method 
	POST

### Endpoint 
```sh
\newuser
```

### Response
```json
 

{
 "status": "success"
	"data": {
 
 	   "email": "teddyoweh@gmail.com",
           "fullname": "testt",
           "id": "db067f2a-7ac4-11ed-aaf7-324d38bf6d76",
           "password": "tstt",
           "secretKey": "a60e1bb1be7fc59ea08378f2840a8a4f44c07d19b315c3e78a279660a3f8a6f5"
           "databases": [
              {
               "name": "appp",
               "project": "idea"
              }
           ],

           "projects": [
             "idea"
           ],
           "buckets": [
             {
              "database": "appp",
              "modified": "2022-12-13 03:47:55.373527",
              "name": "users",
              "project": "idea"
             },
            ]
            "created": "2022-12-13 03:02:22.519349",

          },

}

```


## Get User Data
### Body
- email
- secret
### Method
	POST
### Endpoint 
```sh
\me
```

### Response
```json
 

{
 "status": "success"
	"data": {
 
 	   "email": "teddyoweh@gmail.com",
           "fullname": "testt",
           "id": "db067f2a-7ac4-11ed-aaf7-324d38bf6d76",
           "password": "tstt",
           "secretKey": "a60e1bb1be7fc59ea08378f2840a8a4f44c07d19b315c3e78a279660a3f8a6f5"
           "databases": [
              {
               "name": "appp",
               "project": "idea"
              }
           ],

           "projects": [
             "idea"
           ],
           "buckets": [
             {
              "database": "appp",
              "modified": "2022-12-13 03:47:55.373527",
              "name": "users",
              "project": "idea"
             },
            ]
            "created": "2022-12-13 03:02:22.519349",

          },

}

```



## Create Project

### Body
- email
- secret
- project
### Method
	POST
### Endpoint 
```sh
\newproject
```

### Response
```json
{
 "status": "success"	
}

```



## Create Database

### Body
- email
- secret
- project
- database


### Method
	POST
### Endpoint 
```sh
\newdatabase
```

### Response
```json
{
 "status": "success"	
}

```




## Create Bucket

### Body
- email
- secret
- project
- database
- bucket

### Method
	POST
### Endpoint 
```sh
\newbucket
```

### Response
```json
{
 "status": "success"	
}

```



## Insert Data

### Body
- email
- secret
- project
- database
- bucket
- data 

#### JSON FORMAT FOR Data
```json
"{'name':'teddy'}"
```

### Method
	POST
### Endpoint 
```sh
\insertdata
```

### Response
```json
{
 "status": "success"	
}

```




## Update Data With Query

### Body
- email
- secret
- project
- database
- bucket
- data 
- query

#### JSON FORMAT FOR Data & Query
```json
"{'name':'teddy'}"
```

### Method
	POST
### Endpoint 
```sh
\updatedata
```

### Response
```json
{
 "status": "success"	
}

```

## Update Data With ID

### Body
- email
- secret
- project
- database
- bucket
- data 
- id

#### JSON FORMAT FOR Data 
```json
"{'name':'teddy'}"
```

### Method
	POST
### Endpoint 
```sh
\updatedata
```

### Response
```json
{
 "status": "success"	
}

```





## Fetch Data With Query

### Body
- email
- secret
- project
- database
- bucket
- query

#### JSON FORMAT FOR  Query
```json
"{'name':'teddy'}"
```

### Method
	POST
### Endpoint 
```sh
\updatedata
```

### Response
```json
{
"data": {
	"id": "c0c5cc02-7ac8-11ed-a31f-324d38bf6d76",
	"name": "teddy"
},
"status": "success"
}

```

## Fetch Data With ID

### Body
- email
- secret
- project
- database
- bucket
- id


### Method
	POST
### Endpoint 
```sh
\fetchbyid
```

### Response
```json
{
"data": {
	"id": "c0c5cc02-7ac8-11ed-a31f-324d38bf6d76",
	"name": "teddy"
},
"status": "success"
}

```




## Delete Data With Query

### Body
- email
- secret
- project
- database
- bucket
- query

#### JSON FORMAT FOR Data & Query
```json
"{'name':'teddy'}"
```

### Method
	POST
### Endpoint 
```sh
\updatedata
```

### Response
```json
{
 "status": "success"	
}

```

## Delete Data With ID

### Body
- email
- secret
- project
- database
- bucket
- id


### Method
	POST
### Endpoint 
```sh
\updatedata
```

### Response
```json
{
 "status": "success"	
}

```



## Get Projects
### Body
- email
- secret

### Method 
	POST

### Endpoint 
```sh
\getprojects
```

### Response
```json
 

{
 "status": "success"
	"data": {
           "projects": [
             "idea"
           ],
          },

}

```


## Get Databases
### Body
- email
- secret

### Method 
	POST

### Endpoint 
```sh
\getdatabases
```

### Response
```json
 

{
 "status": "success"
	"data": {
          "databases": [
		{
		"name": "appp",
		"project": "idea"
		}
               ],
          },

}

```



## Get Buckets
### Body
- email
- secret

### Method 
	POST

### Endpoint 
```sh
\getbuckets
```

### Response
```json
 

{
 "status": "success"
	"data": {
           "buckets": {
			"database": "appp",
			"modified": "2022-12-14 00:55:30.617538",
			"name": "users",
			"project": "idea"
		},
          },

}

```

