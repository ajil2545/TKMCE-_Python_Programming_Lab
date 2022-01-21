class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)    
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        print(self.title)
        print(self.author)
class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        Book.__init__(self,name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Publisher: ",self.name) 
        print("Title: ",self.title)
        print("Author",self.author)   
        print("Price",self.price)
        print("No. of pages: ",self.no_of_pages)
obj=Python("xyz","abc","pqr",123,12)
obj.display()