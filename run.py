# from BeardbAPI import BeardbAPI
# service = BeardbAPI()
# service.storage('tddy','')
# api  =service.app
# # api.config('localhost', 9000)

# from bearDB  import Beardb
# from beardb import Bucket
from beardb import  Beardb

project = Beardb('projectname')
project.load_database('class') 