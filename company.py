import importlib
import random
import faker

class Company:
    
    proc_attrs = ['seed', 'name', 'suffix', 'founded', 'founder', 'city', 'state', 'state_name', 'street_address', 'url', 'email_addr', 'phone']
    
    def __init__(self, seed=None):
        if seed != None: self._seed = seed
        self._fake = faker.Factory.create()
        random.seed(self.seed)
        self._fake.seed(self.seed)
        
        for attr in self.proc_attrs:
            getattr(self, attr)
    
    def __getattr__(self, name):
        if name in self.proc_attrs:
            return self._cached_proc_attr(name)
        else:
            return super(Company, self).__getattr__(name)
    
    def _cached_proc_attr(self, attr):
        if not hasattr(self, f'_{attr}'):
            mod = importlib.import_module('generators.' + attr)
            proc_cls = getattr(mod, attr.title().replace('_', ''))
            proc = proc_cls(self)
            setattr(self, f'_{attr}', proc.generate())
        return getattr(self, f'_{attr}')
