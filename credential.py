from random import choice
import string

class Credential:
    
    credential_list = []
    
    def _init_(self, user_password, credential_name, credential_password):
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password
        
    def save_credentials(self):
        Credential.credential_list.append(self)
        
@classmethod
def generate_passowrd(cls):
    """length of the password"""
    
    size = 8
    '''generate random alpha num'''
    alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase
    
    '''create password'''
    password = ''.join(choice(alphanum) for num in range(size))
    
    return password 
    
    
@classmethod
def display_credentials(cls, password):
    user_credential_list = []
    
    for credential in cls.credential_list:
        if credential.user_password == password:
            user_credential_list.append(credential)
    return user_credential_list

@classmethod
def credential_exist(cls, name):
    for credential in cls.credential_list:
        if credential.credential_name == name:
            return True
    return False

    