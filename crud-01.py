data = [
    {
	    "id" : 1,
        "fullname" : "ratna putri",
        "address" : "jakarta",
        "salary" : 5000000,
        "phone" : '099903'
    },
    {
	    "id" : 2,
        "fullname" : "hamish daud",
        "address" : "jakarta",
        "salary" : 2000000,
        "phone" : '34232949'
    },
]

class Employee:
    def __init__(self, data):
        self.data = data
    
    
    def create(self,value):
        value = list(value.items())
        value.insert(0,("id",self.data[len(self.data) - 1]["id"] + 1))
        self.data.append(dict(value))
        return self.data
    
    
    def delete(self,id):
        for i, val in enumerate(self.data):
            if val['id'] == id:
                del self.data[i]
        return self.data
    
    
    def read(self):
        return self.data
    
    
    def update(self,id,value):
        for i, val in enumerate(self.data):
            if val['id'] == id:
                value = list(value.items()) 
                self.data[i] = dict(value)
        return self.data

employee = Employee(data)
# create data
print(employee.create({"fullname":"ratna putri", "address":"jakarta", "salary":5000000, "phone":"099903"}))

# delete data by id
print(employee.delete(2))

# read all data
print(employee.read())

# update data
print(employee.update(2,{"fullname":"raisa andriana", "address":"bekasi", "salary":1000000, "phone":"9939999"}))