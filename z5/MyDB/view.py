#!/usr/bin/env python
class View:  
    @staticmethod  
    def show_item(list):    
        print(f'in database {len(list)} item. they are:')    
        for item in list:      
            print(item.info)  
    
    @staticmethod  
    def get_data(text):    
        return input('enter ' + text + ':')  
        
    @staticmethod  
    def show_menu():   
        print('what do you want:\n' + 
            '\t (1) show user\n' + 
            '\t (2) add user\n' + 
            '\t (3) delite user\n' + 
            '\t (4) update user\n' + 
            '\t (5) show company\n' + 
            '\t (6) add company\n' + 
            '\t (7) delite company\n' + 
            '\t (8) update company\n' + 
            '\t (9) show collectiveContract\n' + 
            '\t (10) add collectiveContract\n' + 
            '\t (11) delite collectiveContract\n' + 
            '\t (12) update collectiveContract\n' + 
            '\t (13) prolong collectiveContract\n' + 
            '\t (14) search collectiveContract\n' +
            '\t (15) show companyWorker\n' + 
            '\t (16) add companyWorker\n' + 
            '\t (17) delite companyWorker\n' + 
            '\t (18) update companyWorker\n' + 
            '\t (19) show individual\n' + 
            '\t (20) add individual\n' + 
            '\t (21) delite individual\n' + 
            '\t (22) update individual\n' + 
            '\t (23) show individualContract\n' + 
            '\t (24) add individualContract\n' + 
            '\t (25) delite individualContract\n' + 
            '\t (26) update individualContract\n' + 
            '\t (27) prolong individualContract\n' + 
            '\t (28) search individualContract\n' +
            '\t (99) exit\n')