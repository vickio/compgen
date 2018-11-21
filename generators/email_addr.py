from . import BaseGenerator

class EmailAddr(BaseGenerator):
    
    def __init__(self, company):
        self.company = company
        self.account = self._load_json('email_addr.json')['account']
    
    def generate(self):
        fname = self.company.founder.split(' ')[0]
        if self.company.name.startswith(fname):
            weight = sum([account[1] for account in self.account])
            self.account.append([fname.lower(), weight])
        return '@'.join([
            self._choose(self.account),
            self.company.url])
