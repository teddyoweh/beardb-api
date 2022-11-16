from flask import render_template, Blueprint, request
import uuid
from Beardb.Beardb import Beardb
from Beardb.Bucket import Bucket
import base64
import json
import hashlib
import datetime
import json
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
    
    
project = Beardb('beardftp')
project.load_database('beardftp') 
@blueprint.route('/newuser', methods=['GET', 'POST'])
def newuser():
    if request.method=='POST':
        form = request.form
        form = dict(form)
        uid=uuid.uuid1()
        print(form)
        newdata = {
        'id':str(uid),
        'email':form['email'],
        'fullname':form['fullname'],
        
        'secretKey':makesecret(str(form['secret']),uid),
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
  
  
@blueprint.route('/me', methods=['GET', 'POST'])
def me():
    if request.method=='POST':
        form = request.form
        form = dict(form)
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
            
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                return {'status':'success','data':i}
        return {'status':'failed','data':{}}
         
  
@blueprint.route('/newproject', methods=['GET', 'POST'])
def newproject():
    if request.method=='POST':
        form = request.form
        form = dict(form)
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                i['projects'].append(form['project'])
               
                project = Beardb(str(form['project'])+'_'+str(i['id']))
                with open('users.json', 'w') as f:
            
                    json.dump(data, f)
                
            
                return {'status':'success'}
        return {'status':'failed'}
     
@blueprint.route('/newdatabase', methods=['GET', 'POST'])
def newdatabase():
    if request.method=='POST':
        form = request.form
        form = dict(form)
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
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
def newbucket():
    if request.method=='POST':
        form = request.form
        form = dict(form)
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
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
        form = request.form
        form = dict(form)
        
        
        with open('users.json', 'r') as f:

            data = json.load(f)
        
        logged = False
        for i in data:
            if i['secretKey']==form['secret'] and i['email']==form['email']:
                logged = True
                i['buckets'].append(
                {
                'name':form['bucket'],
                'database':form['database'],
                'project':form['project'],
                'modified':str(datetime.datetime.now())
                })
               
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
            form = request.form
        form = dict(form)
        
        
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


@blueprint.route('/updatedatabyid', methods=['GET', 'POST'])
def updatedatabyid():
        if request.method=='POST':
            form = request.form
        form = dict(form)
        
        
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
        form = request.form
        form = dict(form)
        
        
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
        form = request.form
        form = dict(form)
        
        
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