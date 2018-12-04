from . import BaseGenerator
from random import random

class FounderGender(BaseGenerator):
    
    def generate(self):
        # citation needed
        if random() > 1/4:
            return 'male'
        else:
            return 'female'

