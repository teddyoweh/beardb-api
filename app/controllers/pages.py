from flask import render_template, Blueprint, request,jsonify
import flask
import uuid
from Beardb.Beardb import Beardb
from Beardb.Bucket import Bucket
import base64
import json
import hashlib
import datetime
from flask_cors import CORS,cross_origin
import json
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

 
def hashvar(string):

    return hashlib.sha256(string.encode('utf-8')).hexdigest()
blueprint = Blueprint('pages', __name__)


################
#### routes ####
################

def makesecret(data,uid):
    encoded = base64.b64encode(str(data).encode('utf-8'))
    encoded = encoded.decode('utf-8')
    datee = datetime.datetime.now()
    newcode = str(datee) + str(uid) + str(encoded)
    return hashvar(newcode)

#make blank page
    
@blueprint.route('/', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Authorization'])
def blank():
    if(request.method == 'POST'):
        print()
        
        # print(request.form)
        response = flask.jsonify({'message': 'ok'})
        # response.headers["Access-Control-Allow-Origin"] = "*"
 
        return response




@blueprint.route('/newuser', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Authorization'])
    
def newuser():
    """_summary_: create a new user

    Returns:
        _type_: _description_
        args:fullname,email, password, 
    """
    
    if request.method=='POST':
       
        form = request.get_json()
        uid=uuid.uuid1()
        print(form)
        newdata = {
        'id':str(uid),
        'email':form['email'],
        'fullname':form['fullname'],
        'password':form['password'],
        'secretKey':makesecret(str(form['password']),uid),
        'projects':[],
        'databases':[],
        'buckets':[],
        'created':str(datetime.datetime.now())
        
        
        
        }
        with open('users.json', 'r') as f:

            data = json.load(f)
        
            data.append(newdata)
        
        with open('users.json', 'w') as f:
        
            json.dump(data, f)
            
        return {'status':'success'}
  
# make a login route

@blueprint.route('/login', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Authorization'])
def login():
    if request.method=='POST':
        form = request.get_json()
        print(form)
        with open('users.json', 'r') as f:

            data = json.load(f)
        emails=[]
        for i in data:
            emails.append(i['email'])
        print(emails)
        if form['email'] in emails:
            index = emails.index(form['email'])
            if data[index]['secretKey'] == form['secret']:
                response = flask.jsonify({'message': 'ok'})
                response.status_code = 200
                return response
            response = flask.jsonify({'message': 'wrong password'})
            response.status_code = 402
            
            return response 
            
        else:
            response = flask.jsonify({'message': 'email not found'})
            response.status_code = 401
            return response
           
        
            
                        
           
                    
@blueprint.route('/me', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Authorization'])
def me():
    if request.method=='POST':
        
        form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        print(form)     
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                return {'status':'success','data':i}
        return {'status':'failed','data':{}}
         
  
@blueprint.route('/newproject', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Authorization'])
def newproject():
    if request.method=='POST':
        
        form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                if form['project'] in i['projects']:
                    return {'status':'failed','reason':'project already exists'}
                i['projects'].append(form['project'])
               
                project = Beardb(str(form['project'])+'_'+str(i['id']))
                with open('users.json', 'w') as f:
            
                    json.dump(data, f)
                
            
                return {'status':'success'}
        return {'status':'failed'}
     
@blueprint.route('/newdatabase', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Authorization'])
def newdatabase():
    if request.method=='POST':
        
        form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                if form['database'] in i['databases']:
                    return {'status':'failed','reason':'database already exists'}
                i['databases'].append(
                {
                'name':form['database'],
                'project':form['project']
                })
               
                project = Beardb(str(form['project'])+'_'+str(i['id']))
                project.load_database(form['database']) 
                with open('users.json', 'w') as f:
            
                    json.dump(data, f)
                
            
                return {'status':'success'}
        return {'status':'failed'}
        
@blueprint.route('/newbucket', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Authorization'])
def newbucket():
    if request.method=='POST':
        
        form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                if form['bucket'] in i['buckets']:
                    return {'status':'failed','reason':'bucket already exists'}
                i['buckets'].append(
                {
                'name':form['bucket'],
                'database':form['database'],
                'project':form['project'],
                'modified':str(datetime.datetime.now()),
                'created':str(datetime.datetime.now())
                })
               
                project = Beardb(str(form['project'])+'_'+str(i['id']))
                project.load_database(form['database']) 
                bucketname = Bucket(project=project, bucket_name=form['bucket'])
                with open('users.json', 'w') as f:
            
                    json.dump(data, f)
                
            
                return {'status':'success'}
        return {'status':'failed'}

@blueprint.route('/insertdata', methods=['GET', 'POST'])
def insertdata():
    
    
    if request.method=='POST':
        
        form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                i['buckets']={
                'name':form['bucket'],
                'database':form['database'],
                'project':form['project'],
                'modified':str(datetime.datetime.now())
                }
               
                project = Beardb(str(form['project'])+'_'+str(i['id']))
                project.load_database(form['database']) 
                bucketdata = Bucket(project=project, bucket_name=form['bucket'])
                bucketdata.insert(data=json.loads(form['data']))
                with open('users.json', 'w') as f:
            
                    json.dump(data, f)
                
            
                return {'status':'success'}
        return {'status':'failed'}
@blueprint.route('/updatedata', methods=['GET', 'POST'])
def updatedata():
        if request.method=='POST':
            
            form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                i['buckets']={
                'name':form['bucket'],
                'database':form['database'],
                'project':form['project'],
                'modified':str(datetime.datetime.now())
                }
               
                project = Beardb(str(form['project'])+'_'+str(i['id']))
                project.load_database(form['database']) 
                bucketdata = Bucket(project=project, bucket_name=form['bucket'])
                query=json.loads(form['query'])
                newdata=json.loads(form['data'])
                bucketdata.update(query=query,data=newdata)
                with open('users.json', 'w') as f:
            
                    json.dump(data, f)
                
            
                return {'status':'success'}
        return {'status':'failed'}
@blueprint.route('/fetchdata', methods=['GET', 'POST'])
def fetchdata():
        if request.method=='POST':
            
            form = request.get_json()
        
        
            with open('users.json', 'r') as f:
    
                data = json.load(f)
            
            logged = False
            for i in data:
                if i['secretKey']==form['secret'] and i['email']==form['email']:
                    logged = True
                    i['buckets']={
                    'name':form['bucket'],
                    'database':form['database'],
                    'project':form['project'],
                    'modified':str(datetime.datetime.now())
                    }
                   
                    project = Beardb(str(form['project'])+'_'+str(i['id']))
                    project.load_database(form['database']) 
                    bucketdata = Bucket(project=project, bucket_name=form['bucket'])
                   
                    
                    with open('users.json', 'w') as f:
                
                        json.dump(data, f)
                    
                
                    return {'status':'success','data':bucketdata.fetchData(query=json.loads(form['data']))}
            return {'status':'failed'}

    
@blueprint.route('/updatedatabyid', methods=['GET', 'POST'])
def updatedatabyid():
        if request.method=='POST':
            
            form = request.get_json()
        
        
            with open('users.json', 'r') as f:
    
                data = json.load(f)
            
            logged = False
            for i in data:
                if i['secretKey']==form['secret'] and i['email']==form['email']:
                    logged = True
                    i['buckets']={
                    'name':form['bucket'],
                    'database':form['database'],
                    'project':form['project'],
                    'modified':str(datetime.datetime.now())
                    }
                   
                    project = Beardb(str(form['project'])+'_'+str(i['id']))
                    project.load_database(form['database']) 
                    bucketdata = Bucket(project=project, bucket_name=form['bucket'])
                   
                    bucketdata.update(id=form['userid'],data=json.loads(form['data']))
                    with open('users.json', 'w') as f:
                
                        json.dump(data, f)
                    
                
                    return {'status':'success'}
            return {'status':'failed'}

    

@blueprint.route('/getbucketslist', methods=['GET', 'POST'])
def getbucketslist():

    if request.method=='POST':
        
        form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                return {'status':'success','buckets':i['buckets']}
               
          
        return {'status':'failed'}
         
@blueprint.route('/getprojectslist', methods=['GET', 'POST'])
def getprojectslist():

    if request.method=='POST':
        
        form = request.get_json()
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                return {'status':'success','projects':i['projects']}
               
          
        return {'status':'failed'}
         
  
  
  
  

        #print(form)
        # status, errors = validate_dict(form)
        # if(status):
        #     users = Bucket(project=project, bucket_name='users')
           
        #     if(len(users.fetchData(query={'username':form['username']}))>0):
        #         errors['username'] = 'Username already exists.'
        #         status = False
        #     if(status):
        #         users.insert(data=form)
        #     return 'success'
        # #print(validate_dict(form))
        # return validate_dict(form)