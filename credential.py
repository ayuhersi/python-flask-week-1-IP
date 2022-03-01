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
        
''''''
        