#!/usr/bin/env python

import mysql.connector
import datetime

class User:  
    def __init__(self, id=0, login=None, password=None, levelOFPrioriti=None, firstname=None, lastname=None, midname=None, passportId=None):    
        self.id = id   
        self.login = login    
        self.password = password    
        self.levelOFPrioriti = levelOFPrioriti
        self.firstname = firstname   
        self.lastname = lastname   
        self.midname = midname  
        self.passportId = passportId    

    @property  
    def info(self):    
        return f'{self.id} | {self.login} | {self.password} | {self.levelOFPrioriti}| {self.firstname}| {self.lastname}| {self.midname}| {self.passportId}'
    
    @staticmethod  
    def get_user():    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []    
        c.execute('select * from user')
        for row in c :
            user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])      
            result.append(user)
        c.close()    
        conn.close()    
        return result  

    @staticmethod  
    def add_user(id_, firstname, lastname,  midname, passportId, login, password, levelOFPrioriti):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('insert into user values(%s, %s, %s, %s, %s, %s, %s, %s)', \
            (int(id_), firstname, lastname,  midname, passportId, login, password, levelOFPrioriti))    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def delite_user(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('DELETE FROM user WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def update_user(id_, changeOn, changePar):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE user SET ' + changePar + ' = ' + changeOn + ' WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

class Company:  
    def __init__(self, id=0, codName=None, fullName=None, shortName=None, address=None, bankDetals=None, specialization=None, user_id=None):    
        self.id = id   
        self.codName = codName    
        self.fullName = fullName    
        self.shortName = shortName
        self.address = address   
        self.bankDetals = bankDetals   
        self.specialization = specialization   
        self.user_id = user_id   

    @property  
    def info(self):    
        return f'{self.id} | {self.codName} | {self.fullName} | {self.shortName}| {self.address}| {self.bankDetals}| {self.specialization}| {self.user_id}'
    
    @staticmethod  
    def get_company():    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []    
        c.execute('select * from company')
        for row in c :
            company = Company(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])      
            result.append(company)
        c.close()    
        conn.close()    
        return result  

    @staticmethod  
    def add_company(id_, codName, fullName, shortName, address, bankDetals, specialization, user_id):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('insert into company values(%s, %s, %s, %s, %s, %s, %s, %s)', \
            (int(id_), codName, fullName, shortName, address, bankDetals, specialization, user_id))    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def delite_company(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('DELETE FROM company WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def update_company(id_, changeOn, changePar):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE company SET ' + changePar + ' = ' + changeOn + ' WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

class CollectiveContract:  
    def __init__(self, id=0, date=None, limitation=None, paymentsForInsuredEvents=None, company_id=None, PaymentsFor1stCategory=None, PaymentsFor2stCategory=None, PaymentsFor3stCategory=None):   
        self.id = id   
        self.date = date    
        self.limitation = limitation    
        self.paymentsForInsuredEvents = paymentsForInsuredEvents
        self.PaymentsFor1stCategory = PaymentsFor1stCategory   
        self.PaymentsFor2stCategory = PaymentsFor2stCategory   
        self.PaymentsFor3stCategory = PaymentsFor3stCategory   
        self.company_id = company_id   

    @property  
    def info(self):    
        return f'{self.id} | {self.date} | {self.limitation} | {self.paymentsForInsuredEvents}| {self.company_id}| {self.PaymentsFor1stCategory}| {self.PaymentsFor2stCategory}| {self.PaymentsFor3stCategory}'
    
    @staticmethod  
    def get_collectiveContract():    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []    
        c.execute('select * from collectivecontract')
        for row in c :
            collectiveContract = CollectiveContract(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])      
            result.append(collectiveContract)
        c.close()    
        conn.close()    
        return result  

    @staticmethod  
    def add_collectiveContract(id_, limitation, paymentsForInsuredEvents, company_id, PaymentsFor1stCategory, PaymentsFor2stCategory, PaymentsFor3stCategory):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('insert into collectivecontract values(%s, %s, %s, %s, %s, %s, %s, %s)', \
            (int(id_), datetime.datetime.today(), limitation, paymentsForInsuredEvents, company_id, PaymentsFor1stCategory, PaymentsFor2stCategory, PaymentsFor3stCategory))    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def delite_collectiveContract(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('DELETE FROM collectivecontract WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def update_collectiveContract(id_, changeOn, changePar):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE collectivecontract SET ' + changePar + ' = "' + str(changeOn) + '" WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod 
    def prolong_collectiveContract(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE collectivecontract SET limitation = DATE_ADD(limitation, INTERVAL 1 YEAR) WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()
    
    @staticmethod 
    def search_collectiveContract(searchPar,searchOn):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []
        c.execute('SELECT * FROM collectiveContract WHERE ' + searchPar + " LIKE '" + searchOn + "'")    
        for row in c :
            collectiveContract = CollectiveContract(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])      
            result.append(collectiveContract)
        c.close()    
        conn.close()    
        return result   

class CompanyWorker :  
    def __init__(self, id=0, firstname=None, lastname=None, midname=None, age=None, riskcategory=None, collectiveContract_id=None):   
        self.id = id   
        self.firstname = firstname    
        self.lastname = lastname    
        self.midname = midname
        self.age = age   
        self.riskcategory = riskcategory   
        self.collectiveContract_id = collectiveContract_id   

    @property  
    def info(self):    
        return f'{self.id} | {self.firstname} | {self.lastname} | {self.midname}| {self.age}| {self.riskcategory}| {self.collectiveContract_id}'
    
    @staticmethod  
    def get_companyWorker():    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []    
        c.execute('select * from companyWorker')
        for row in c :
            companyWorker = CompanyWorker(row[0], row[1], row[2], row[3], row[4], row[5], row[6])      
            result.append(companyWorker)
        c.close()    
        conn.close()    
        return result  

    @staticmethod  
    def add_companyWorker(id_, firstname, lastname, midname, age, riskcategory, collectiveContract_id):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('insert into companyWorker values(%s, %s, %s, %s, %s, %s, %s)', \
            (int(id_), firstname, lastname, midname, age, riskcategory, collectiveContract_id))    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def delite_companyWorker(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('DELETE FROM companyWorker WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def update_companyWorker(id_, changeOn, changePar):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE companyWorker SET ' + changePar + ' = "' + str(changeOn) + '" WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

class Individual :  
    def __init__(self, id=0, firstname=None, lastname=None, midname=None, age=None, riskcategory=None, address=None, phonenumber=None, user_id=None):   
        self.id = id   
        self.firstname = firstname    
        self.lastname = lastname    
        self.midname = midname
        self.age = age   
        self.riskcategory = riskcategory   
        self.user_id = user_id   
        self.address = address   
        self.phonenumber = phonenumber   

    @property  
    def info(self):    
        return f'{self.id} | {self.firstname} | {self.lastname} | {self.midname}| {self.age}| {self.riskcategory}| {self.address}| {self.phonenumber}| {self.user_id}'
    
    @staticmethod  
    def get_individual():    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []    
        c.execute('select * from individual')
        for row in c :
            individual = Individual(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])      
            result.append(individual)
        c.close()    
        conn.close()    
        return result  

    @staticmethod  
    def add_individual(id_, firstname, lastname, midname, age, riskcategory, address, phonenumber, user_id):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('insert into individual values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', \
            (int(id_), firstname, lastname, midname, age, riskcategory, address, phonenumber, user_id))    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def delite_individual(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('DELETE FROM individual WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def update_individual(id_, changeOn, changePar):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE individual SET ' + changePar + ' = "' + str(changeOn) + '" WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

class IndividualContract:  
    def __init__(self, id=0, date=None, limitation=None, amountOfPayments=None, paymentsForInsuredEvents=None, individual_id=None):   
        self.id = id   
        self.date = date    
        self.limitation = limitation    
        self.paymentsForInsuredEvents = paymentsForInsuredEvents
        self.amountOfPayments = amountOfPayments   
        self.individual_id = individual_id   

    @property  
    def info(self):    
        return f'{self.id} | {self.date} | {self.limitation}| {self.amountOfPayments} | {self.paymentsForInsuredEvents}| {self.individual_id}'
    
    @staticmethod  
    def get_individualContract():    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []    
        c.execute('select * from individualContract')
        for row in c :
            individualContract = IndividualContract(row[0], row[1], row[2], row[3], row[4], row[5])      
            result.append(individualContract)
        c.close()    
        conn.close()    
        return result  

    @staticmethod  
    def add_individualContract(id_, limitation, amountOfPayments, paymentsForInsuredEvents, individual_id):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('insert into individualContract values(%s, %s, %s, %s, %s, %s)', \
            (int(id_), datetime.datetime.today(), limitation, amountOfPayments, paymentsForInsuredEvents, individual_id))    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def delite_individualContract(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('DELETE FROM individualContract WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod  
    def update_individualContract(id_, changeOn, changePar):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE individualContract SET ' + changePar + ' = "' + str(changeOn) + '" WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()

    @staticmethod 
    def prolong_individualContract(id_):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        c.execute('UPDATE individualContract SET limitation = DATE_ADD(limitation, INTERVAL 1 YEAR) WHERE id = ' + id_)    
        conn.commit()
        c.close()    
        conn.close()
    
    @staticmethod 
    def search_individualContract(searchPar,searchOn):    
        conn = mysql.connector.connect(user='root', password='usbw', host='localhost', database='mydb')    
        c = conn.cursor()    
        result = []
        c.execute('SELECT * FROM individualContract WHERE ' + searchPar + " LIKE '" + searchOn + "'")    
        for row in c :
            individualContract = IndividualContract(row[0], row[1], row[2], row[3], row[4], row[5])      
            result.append(individualContract)
        c.close()    
        conn.close()    
        return result   
