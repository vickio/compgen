from . import BaseGenerator

class StreetAddress(BaseGenerator):
    
    def generate(self):
        return self.company._fake.street_address()
