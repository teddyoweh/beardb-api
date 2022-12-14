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
[POST] - \bucketlist
[POST] - \databaselist
[POST] - \projectlist
```
# API GUIDES

## Creating New User
### Params
- email
- fullname
- password
- 
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


## Getting User Data
### Params
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

### Params
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



## Create Project

### Params
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

### Params
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

### Params
- email
- secret
- project
- database
- bucket
- data 
```sh
	("{'name':'teddy'}")
```

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




