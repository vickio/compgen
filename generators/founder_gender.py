from . import BaseGenerator
from random import randint

class FounderGender(BaseGenerator):
    
    def generate(self):
        if randint(0, 1) == 0:
            return 'male'
        else:
            return 'female'

