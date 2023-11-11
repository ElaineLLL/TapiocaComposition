class CafeService():
    def __init__(self, name, cafemanagement, ordermanagement, customerservice):
        self.name = name
        self.cafemanagement = cafemanagement
        self.customerservice = customerservice
        self.ordermanagement = ordermanagement
        self.subordianries = []

    def add(self, service):
        self.subordianries.append(service)

    def remove(self, service):
        self.subordianries.remove(service)

    def getServices(self):
        return self.subordianries

    def setCafeManagement(self, service):
       self.cafemanagement = service

    def setCustomerService(self, service):
        self.customerservice = service

    def setOrderManagement(self, service):
        self.ordermanagement = service

    def getCafeManagement(self):
        return self.cafemanagement

    def getCustomerService(self):
        return self.customerservice

    def getOrderManagement(self):
        return self.ordermanagement

    def display(self):
        print({
            "Cafe Name": self.name,
            "Cafe Management": self.cafemanagement,
            "Order Management":self.ordermanagement,
            "Customer Service":self.customerservice}
        )