from dbhelper import DbConnection
from salesRecords import SalesRecord
import json

def getAllSetupData():
    try :
        result = DbConnection().getDataByProcedure('usp_getallsetupdata',['default'])
        print(result)

    except (Exception) as error:
        print(error)  

def getSupplierList():
    try: 
        result = DbConnection().getDataByQuery("select json_agg(supplier) from supplier;")
        print (result)
    except(Exception) as error:
        print(error)     

def getSalesRecord():
    try: 
        resultraw = DbConnection().getDataByProcedure('usp_getsaleenqlist',['2022-05-01','2022-05-02'])
        salesdata =  SalesRecord.fromJson(stringdata=resultraw)
        jsonresult = SalesRecord.toJson(salesdata)

        print(jsonresult)
        # print (json.dumps(salesdata))
        # jsonresultstring = SalesRecord.toJson(list(salesdata))
        #  print (list(salesdata))
    except(Exception) as error:
        print(error)                    
