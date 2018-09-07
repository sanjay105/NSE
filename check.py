from nsetools import Nse
import json,csv
from apscheduler.schedulers.blocking import BlockingScheduler
import pprint
#from datetime import time
import time
res=[]
def getVal():
    nse=Nse()
    q=nse.get_quote('SBIN')
    #print(q)
    #asc=nse.get_stock_codes()
    #with open('abc.json','w+') as ofile:
        #json.dump(q,ofile)
    #with open('asc.json','w+') as ofile:
        #json.dump(asc,ofile)
    #print(asc)
    q['curtime']=str(time.ctime())
    #print(q['curtime'])
    res.append(q)
    print(res)
    moveToCSV()
def moveToCSV():
    keys=res[0].keys()
    fname='results/postlunch/'+str(len(res))+"-10min"+'.csv';
    with open(fname,'w') as o:
        dict_writer=csv.DictWriter(o,fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(res)
sch=BlockingScheduler()
sch.add_job(getVal,'interval',minutes=1)
sch.start()
#getVal()
