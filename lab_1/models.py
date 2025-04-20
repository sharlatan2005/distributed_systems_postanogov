class App:
    def __init__(self, name):
        self.name = name
    
    def to_dict(self):
        return {
            'application': {
                'name': self.name
            }   
        }