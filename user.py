from credential import Credential




class User:
    
    user_list = []
    
    def __init__(self,user_name, user_password):
        self.username = user_name
        self.password = user_password
        
    def save_user(self):
        pass
          
    @classmethod 
    def find_credential(cls, name):
        pass 
    
    @classmethod 
    def log_in(cls, name, password):
        pass  
    
    @classmethod
    def display_user(cls, name, password ):
        pass
      
    @classmethod
    def user_exist(cls, name):
        pass 

    