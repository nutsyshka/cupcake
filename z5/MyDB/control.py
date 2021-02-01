#!/usr/bin/env python

from model import User
from model import Company
from model import CompanyWorker
from model import Individual
from model import CollectiveContract
from model import IndividualContract
from view import View

class Controller:  

    def show_user(self):   
        user = User.get_user()    
        return View.show_item(user) 

    def add_user(self):    
        id_ = View.get_data('id')    
        login = View.get_data('login')
        password = View.get_data('password') 
        levelOFPrioriti = View.get_data('levelOFPrioriti') 
        firstname = View.get_data('firstname') 
        lastname = View.get_data('lastname') 
        midname = View.get_data('midname') 
        passportId = View.get_data('passportId')       
        user = User.add_user(id_, firstname, lastname,  midname, passportId, login, password, levelOFPrioriti)  
        
    def delite_user(self):
        id_ = View.get_data('id') 
        User.delite_user(id_)
    
    def update_user(self):
        id_ = View.get_data('id') 
        changePar = View.get_data('changer Parameter')    
        changeOn = View.get_data('Change On')
        user = User.update_user(id_, changeOn, changePar)  


    def show_company(self):   
        company = Company.get_company()    
        return View.show_item(company) 

    def add_company(self):    
        id_ = View.get_data('id')    
        codName = View.get_data('codName')
        fullName = View.get_data('fullName') 
        shortName = View.get_data('shortName') 
        address = View.get_data('address')
        user_id = View.get_data('user_id')
        bankDetals = View.get_data('bankDetals') 
        specializatio = View.get_data('specializatio')       
        company = Company.add_company(id_, codName, fullName, shortName, address, bankDetals, specializatio, user_id)  
        
    def delite_company(self):
        id_ = View.get_data('id') 
        Company.delite_company(id_)
    
    def update_company(self):
        id_ = View.get_data('id') 
        changePar = View.get_data('changer Parameter')    
        changeOn = View.get_data('Change On')
        company = Company.update_company(id_, changeOn, changePar) 
    

    def show_collectiveContract(self):   
        collectiveContract = CollectiveContract.get_collectiveContract()    
        return View.show_item(collectiveContract) 

    def add_collectiveContract(self):    
        id_ = View.get_data('id')    
        limitation = View.get_data('limitation')
        paymentsForInsuredEvents = View.get_data('paymentsForInsuredEvents') 
        company_id = View.get_data('company_id') 
        PaymentsFor1stCategory = View.get_data('PaymentsFor1stCategory')
        PaymentsFor2stCategory = View.get_data('PaymentsFor2stCategory')
        PaymentsFor3stCategory = View.get_data('PaymentsFor3stCategory')      
        collectiveContract = CollectiveContract.add_collectiveContract(id_, limitation, paymentsForInsuredEvents, company_id, PaymentsFor1stCategory, PaymentsFor2stCategory, PaymentsFor3stCategory)  
        
    def delite_collectiveContract(self):
        id_ = View.get_data('id') 
        CollectiveContract.delite_collectiveContract(id_)
    
    def update_collectiveContract(self):
        id_ = View.get_data('id') 
        changePar = View.get_data('changer Parameter')    
        changeOn = View.get_data('Change On')
        collectiveContract = CollectiveContract.update_collectiveContract(id_, changeOn, changePar) 

    def prolong_collectiveContract(self):
        id_ = View.get_data('id') 
        collectiveContract = CollectiveContract.prolong_collectiveContract(id_) 

    def search_collectiveContract(self):
        searchPar = View.get_data('search Parametr')
        searhOn = View.get_data('search like') 
        collectiveContract = CollectiveContract.search_collectiveContract(searchPar, searhOn)
        return View.show_item(collectiveContract)


    def show_companyWorker(self):   
        companyWorker = CompanyWorker.get_companyWorker()    
        return View.show_item(companyWorker) 
 
    def add_companyWorker(self):    
        id_ = View.get_data('id')    
        firstname = View.get_data('firstname')
        lastname = View.get_data('lastname') 
        midname = View.get_data('midname') 
        age = View.get_data('age')
        riskcategory = View.get_data('riskcategory')
        collectiveContract_id = View.get_data('collectiveContract_id')      
        companyWorker = CompanyWorker.add_companyWorker(id_, firstname, lastname, midname, age, riskcategory, collectiveContract_id)  
        
    def delite_companyWorker(self):
        id_ = View.get_data('id') 
        CompanyWorker.delite_companyWorker(id_)
    
    def update_companyWorker(self):
        id_ = View.get_data('id') 
        changePar = View.get_data('changer Parameter')    
        changeOn = View.get_data('Change On')
        companyWorker = CompanyWorker.update_companyWorker(id_, changeOn, changePar) 


    def show_individual(self):   
        individual = Individual.get_individual()    
        return View.show_item(individual) 
 
    def add_individual(self):    
        id_ = View.get_data('id')    
        firstname = View.get_data('firstname')
        lastname = View.get_data('lastname') 
        midname = View.get_data('midname') 
        age = View.get_data('age')
        riskcategory = View.get_data('riskcategory')
        address = View.get_data('address')    
        phonenumber = View.get_data('phonenumber')      
        user_id = View.get_data('user_id')        
        individual = Individual.add_individual(id_, firstname, lastname, midname, age, riskcategory, address, phonenumber, user_id)  
        
    def delite_individual(self):
        id_ = View.get_data('id') 
        Individual.delite_individual(id_)
    
    def update_individual(self):
        id_ = View.get_data('id') 
        changePar = View.get_data('changer Parameter')    
        changeOn = View.get_data('Change On')
        individual = Individual.update_individual(id_, changeOn, changePar) 


    def show_individualContract(self):   
        individualContract = IndividualContract.get_individualContract()    
        return View.show_item(individualContract) 

    def add_individualContract(self):    
        id_ = View.get_data('id')    
        limitation = View.get_data('limitation')
        paymentsForInsuredEvents = View.get_data('paymentsForInsuredEvents') 
        amountOfPayments = View.get_data('amountOfPayments') 
        individual_id = View.get_data('individual_id') 
        individualContract = IndividualContract.add_individualContract(id_, limitation, amountOfPayments, paymentsForInsuredEvents, individual_id)  
        
    def delite_individualContract(self):
        id_ = View.get_data('id') 
        IndividualContract.delite_individualContract(id_)
    
    def update_individualContract(self):
        id_ = View.get_data('id') 
        changePar = View.get_data('changer Parameter')    
        changeOn = View.get_data('Change On')
        individualContract = IndividualContract.update_individualContract(id_, changeOn, changePar) 

    def prolong_individualContract(self):
        id_ = View.get_data('id') 
        individualContract = IndividualContract.prolong_individualContract(id_) 

    def search_individualContract(self):
        searchPar = View.get_data('search Parametr')
        searhOn = View.get_data('search like') 
        individualContract = IndividualContract.search_individualContract(searchPar, searhOn)
        return View.show_item(individualContract)

 
    def run(self):    
        choice = 0   
        choices = {      
            1 : lambda : self.show_user(),      
            2 : lambda : self.add_user(),
            3 : lambda : self.delite_user(),
            4 : lambda : self.update_user(),
            5 : lambda : self.show_company(),      
            6 : lambda : self.add_company(),
            7 : lambda : self.delite_company(),
            8 : lambda : self.update_company(),
            9 : lambda : self.show_collectiveContract(),      
            10 : lambda : self.add_collectiveContract(),
            11 : lambda : self.delite_collectiveContract(),
            12 : lambda : self.update_collectiveContract(),
            13 : lambda : self.prolong_collectiveContract(),
            14 : lambda : self.search_collectiveContract(),
            15 : lambda : self.show_companyWorker(),      
            16 : lambda : self.add_companyWorker(),
            17 : lambda : self.delite_companyWorker(),
            18 : lambda : self.update_companyWorker(),
            19 : lambda : self.show_individual(),      
            20 : lambda : self.add_individual(),
            21 : lambda : self.delite_individual(),
            22 : lambda : self.update_individual(),
            23 : lambda : self.show_individualContract(),      
            24 : lambda : self.add_individualContract(),
            25 : lambda : self.delite_individualContract(),
            26 : lambda : self.update_individualContract(),
            27 : lambda : self.prolong_individualContract(),
            28 : lambda : self.search_individualContract(),
            }    
        while (choice != 99):      
            View.show_menu()      
            choice = int(View.get_data('choice option'))      
            if choice in choices:        
                choices[choice]()

if __name__ == '__main__':  
    Controller().run()