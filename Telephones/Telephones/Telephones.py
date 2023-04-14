class Telephone:
    def __init__(self, model, price, number):
        self.model = model
        self.price = price
        self.number = number

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_number(self,number):
        self.number = number

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price 

    def get_number(self):
        return self.number

class Human:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age 
        self.money = money
        self.telephones = []
        self.max_telephones = 3
    
    def add_money(self, amount):
        self.money+=amount
        print(f'Added {amount} money. Total money: {self.money}.')

    def remove_money(self, amount):
        if self.money < amount:
            print('Not enough money to withdraw') 
        else:
            self.money -= amount 
            print(f'Withdrawn {amount} money. Total money: {self.money}.') 

    def add_age(self):
        self.age+=1
        print(f'Happy bithday! Your new age is: {self.age}.') 

    def add_telephone(self, telephone):
        if len(self.telephones) == self.max_telephones:
            print(f'Not possible to add {telephone.get_model()}, you have maximum amount of telephones') 
        elif self.money < telephone.get_price():
            print(f'Not possible to add {telephone.get_model()}, not enough money') 
        elif (self.age < 18) and (telephone.get_price() > 500):
            print(f'Not possible to add {telephone.get_model()}, you are too young to buy such telephone')
        else:
            self.telephones.append(telephone) 
            self.money -= telephone.get_price() 
            print(f'Telephone {telephone.get_model()} was added. Total money: {self.money}.') 

    def remove_telephone(self, telephone):
        self.telephones.remove(telephone) 
        self.money += telephone.get_price() 
        print(f'Telephone {telephone.get_model()} was removed. Total money: {self.money}.') 
         

def Print_Models(Models):
    for i in range(len(Models)):
        print(i+1, Models[i].model, Models[i].price, Models[i].number)  

def Print_People(People):
    for i in range(len(People)): 
        print(i+1, People[i].name, People[i].age, People[i].money)
        k=1
        for tlf in People[i].telephones:
            print('{', k, tlf.model, tlf.price, tlf.number, '}')
            k+=1
        print()
    

Models=[]
Models.append(Telephone("iPhone", 1000, "1234567"))
Models.append(Telephone("Samsung", 800, "7654321"))
Models.append(Telephone("Nokia", 200, "9876543")) 
Models.append(Telephone("Xiaomi", 500, "2468101"))
Print_Models(Models)

print()

Tlfnums = [int(tlf.get_number()) for tlf in Models] 

People=[] 
People.append(Human("Alice",25,700)) 
People.append(Human("Bob",30,1200))
People.append(Human("John",14,500)) 
Print_People(People)

print()

print("Choose option")
print("0. Exit")
print("1. Show models")
print("2. Show people")
print("3. Add new model")
print("4. Add new human")
print("5. Add telephone to human") 
print("6. Delete telephone from human") 
print("7. Add money to human") 
print("8. Remove money from human") 
print("9. Add age to human")
print()
while True:
    cmd = int(input("Enter option: "))
    if(cmd<0 or cmd>9):
        print("Incorrect command!") 
        print()
    if(cmd==0):
        break 
    if(cmd==1):
        Print_Models(Models)
        print()
    if(cmd==2):
        Print_People(People) 
        print()
    if(cmd==3):
        model=input("Enter model: ") 
        price=int(input("Enter price: ")) 
        number=int(input("Enter number: ")) 
        while((number in Tlfnums) or (len(str(number))!=7)):
            if(number in Tlfnums):
                print("Existing number! Enter another number:")
            else:
                print("Please enter correct number:")
            number = int(input())
        Models.append(Telephone(model, price, number)) 
        Tlfnums.append(number)
        print()
    if(cmd==4):
        name = input("Enter name: ") 
        age = int(input("Enter age: ")) 
        money = int(input("Enter money: ")) 
        People.append(Human(name,age,money)) 
        print()
    if(cmd==5):
        h = int(input("Enter human NUM: ")) 
        while((h-1<0) or (h-1>=len(People))): 
            print("Not existing human!") 
            h = int(input("Enter human NUM: ")) 
        
        t = int(input("Enter telephone NUM: ")) 
        while((t-1<0) or (t-1>=len(Models))): 
            print("Not existing telephone!") 
            t = int(input("Enter telephone NUM: ")) 

        l0 = len(People[h-1].telephones)
        People[h-1].add_telephone(Models[t-1]) 
        if(len(People[h-1].telephones) > l0):
            Models.remove(Models[t-1])
        
    if(cmd==6):
        h = int(input("Enter human NUM: ")) 
        while((h-1<0) or (h-1>=len(People))): 
            print("Not existing human!") 
            h = int(input("Enter human NUM: ")) 
        
        t = int(input("Enter human's telephone NUM: ")) 
        while((t-1<0) or (t-1>=len(People[h-1].telephones))): 
            print("Not existing telephone!") 
            t = int(input("Enter human's telephone NUM: ")) 
        tmp = People[h-1].telephones[t-1]
        People[h-1].remove_telephone(tmp) 
        Models.append(tmp)
    if(cmd == 7):
        h = int(input("Enter human NUM: ")) 
        while((h-1<0) or (h-1>=len(People))): 
            print("Not existing human!") 
            h = int(input("Enter human NUM: ")) 
        
        money = int(input("Enter money amount: "))
        while(money<=0):
            print("Please enter positive money amount:")
            money=int(input())
        People[h-1].add_money(money) 
    if(cmd == 8):
        h = int(input("Enter human NUM: ")) 
        while((h-1<0) or (h-1>=len(People))): 
            print("Not existing human!") 
            h = int(input("Enter human NUM: ")) 
        
        money = int(input("Enter money amount: "))
        while(money<=0):
            print("Please enter positive money amount:")
            money=int(input()) 
        People[h-1].remove_money(money)  
    if(cmd==9):
        h = int(input("Enter human NUM: ")) 
        while((h-1<0) or (h-1>=len(People))): 
            print("Not existing human!") 
            h = int(input("Enter human NUM: ")) 
        People[h-1].add_age()
















