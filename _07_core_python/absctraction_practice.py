#abstraction
'''
1)Abstraction is used to hide the internal functionality of the function from the users.
 The users only interact with the basic implementation of the function, but inner working is hidden
2)In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
 It also enhances the application efficiency
3)A class that consists of one or more abstract method is called the abstract class.
 Abstract methods do not contain their implementation. Abstract class can be inherited by the subclass and
 abstract method gets its definition in the subclass. Abstraction classes are meant to be the blueprint of the other class.
4)An abstract class can be useful when we are designing large functions.
An abstract class is also helpful to provide the standard interface for different implementations of components
'''


from abc import ABC,abstractmethod

class BankStatement(ABC):
    @abstractmethod
    def debit(self):
        pass
    def amount(self):
        pass
    def credit(self):
        pass
class display(BankStatement):
    def debit(self):
        print("2000 is debited")
    def amount(self):
        print("5000 is total amount")
    def credit(self):
        print("2000 is credited")
obj = display()
obj.debit()
obj.amount()
obj.credit()


class User(ABC):
    def __init__(self, name, num_of_months):
        self.name = name
        self.num_of_months = num_of_months
    @abstractmethod
    def process_fee(self):
        pass
class first(User):
    first_class_price = 2200

    def process_fee(self):
        return first.first_class_price*self.num_of_months


class second(User):
    second_class_price = 1500

    def process_fee(self):
        return second.second_class_price*self.num_of_months

obj =first("jhon",1)
print(obj.first_class_price)
obi2 = second("sam",1)
print(second.second_class_price)


