import json

class SalesRecord:
    def __init__(
                self,
                date,
                refdocid,
                username,
                paymenttype,
                customername,
                locationname,
                invoiceqty,
                paidamount,
                discountamount,
                focamount,
                invoiceamount,
                netamount):
        self.date = date
        self.refdocid = refdocid
        self.username = username
        self.paymenttype = paymenttype
        self.customername = customername
        self.locationname = locationname
        self.invoiceqty = invoiceqty
        self.paidamount = paidamount
        self.discountamount = discountamount
        self.focamount = focamount
        self.invoiceamount = invoiceamount
        self.netamount = netamount

    def toJson(saleRecordList):
        return json.dumps([saleRecord.__dict__ for saleRecord in saleRecordList],indent= 2) 
        
    def fromJson(stringdata):
        resultjson = json.dumps([result['data'] for result in stringdata[0]][0])
        jsondatalist = json.loads(resultjson)
        salesRecordList = [SalesRecord(item['date'],
                                       item['refdocid'],
                                       item['username'],
                                       item['paymenttype'],
                                       item['customername'],
                                       item['locationname'],
                                       item['invoiceqty'],
                                       item['paidamount'],
                                       item['discountamount'],
                                       item['focamount'],
                                       item['invoiceamount'],
                                       item['netamount']
                                       ) 
                           for item in jsondatalist]
        return salesRecordList

