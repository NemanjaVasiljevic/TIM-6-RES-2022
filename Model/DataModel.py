from asyncio.windows_events import NULL
import sys
sys.path.append('../')
from msilib.schema import Error
from mysqlx import DatabaseError
from Database.DatabaseFunctions import (AddToTable, ReadFromTable, ReadHistorical)


listCodes = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

########################################################################################################

class Request:
    def __init__(self,request,data):
        self.request = request
        self.data = data


#########################################################################################################

class Data:
    def __init__(self, value, code):
        self.value = value
        self.code = code

    def __str__(self):
        return f"Code: {self.code} Value: {self.value}"


#########################################################################################################

class Reader:
    def __init__(self,database):
        self.database = database


    def WriteData(self,data):
            try:
                AddToTable(data.value, data.code, self.database)
            except DatabaseError:
                return F"Whoops. Something went wrong with writting in base!"


    def ReadData(self,code1, code2):
        try:
            data1, data2 = ReadFromTable(code1,code2, self.database)
            return data1, data2
        except:
            return Error


    def ReadHistory(self,historicalValue):
        try:
            retVal = ReadHistorical(historicalValue,self.database)
            return retVal

        except:
            return print(F"Greska u ReadHistory")

        
    def CalculateDifference(self,new):
        
        if new.code == "CODE_DIGITAL":
            return True

        
        try:
            old = ReadFromTable(new.code,"", self.database)
        
        except:
            return DatabaseError

            
        if type(old) is NULL:
            print("Prvi prolaz jos nista nema u bazi")
            return True
        
        oldData = Data(old[0],old[1])
        difference = float(oldData.value) * 0.02

        print(F"\nGornja granica: {float(oldData.value) + difference} Donja granica: {float(oldData.value) - difference} Nova vrednost: {new} Stara vrednost: {oldData}\n")

        if(new.value > float(oldData.value) + difference or new.value < float(oldData.value) - difference):
            return True
        else:
            return False


#########################################################################################################


class CollectionDescription:
    
        def __init__(self,historicalCollection,code):
            if code ==listCodes[0] or code == listCodes[1] :
                self.dataSet = 1

            elif code ==  listCodes[2] or code == listCodes[3]:
                self.dataSet = 2

            elif code == listCodes[4] or code == listCodes[5]:
                self.dataSet = 3

            elif code ==listCodes[6] or code == listCodes[7]:
                self.dataSet = 4

            else:
                self.dataSet = 0

            self.historicalCollection = historicalCollection



#########################################################################################################

class HistoricalValue:
        def __init__(self, code, fromTime, toTime):
            self.code = code
            self.fromTime = fromTime
            self.toTime = toTime


#########################################################################################################

class DeltaCD:
   def __init__(self,ADD,UPDATE):
       self.ADD=ADD
       self.UPDATE=UPDATE