
class Library:
   def __init__(self, name, address):
       self.name = name
       self.address = address
       
        
class Book:
   def __init__(self,author, book_name):
      self.author = author
      self.book_name = book_name
      self.is_available = True
    
class Person:
    def __init__(self,name, id):
        self.name = name
        self.id = id


class User(Person):
   def __init__(self,name,borrow_book):
    super().__init__(name)
    self.borrow_book = borrow_book


class employee(Person):
   def __init__(self,name):
    super().__init__(name)
    

    
