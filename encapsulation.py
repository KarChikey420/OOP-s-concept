class Bank:
    def __init__(self,id,name):
        self._id=id
        self._name=name
    
    def get_data(self):
        return f'my id is {self._id} and name is {self._name}'
    
    def set_data(self,id,name):
        self._id=id
        self._name=name

obj=Bank(1,'kartik')
print(obj.get_data())

obj.set_data(2,'data')
print(obj.get_data())