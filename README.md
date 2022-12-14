# BearDB MicroService
 Deploy JSON Databases Remotely 

## Introduction

BearDB is a database system that implements encrypted versions of JSON data, making it easy to access, manage, and deploy remotely. With Beardb, you can securely store and manage your data without worrying about unauthorized access. The system is designed to be user-friendly and easy to set up, even for users with limited technical experience.

To deploy Beardb on a remote server, you will need to have access to a server that meets the system's requirements. These requirements include a Linux-based operating system, a minimum of 4GB of RAM, and at least 10GB of free storage space. Once you have a suitable server, you can download and install the Beardb software and follow the provided instructions to set up the database.

Once Beardb is up and running on your remote server, you can easily manage your data using the system's intuitive interface. You can create, read, update, and delete records as needed, and access your data from any device with an internet connection. The system's encryption features ensure that your data remains secure, even when accessed remotely.

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



## Gettings Projects
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


## Gettings Databases
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

