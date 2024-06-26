class libraryitem:
    def __init__(self,itemid,title):
        self.itemid = itemid
        self.title = title
        self.available = True

    def __str__(self):
        return f"Item id : {self.itemid}, Title : {self.title} Available : {self.available}" 

    def check_out(self):
        if self.available:
            self.available = False
            print(f"{self.title} is succesfully checked out !")
        else :
            print(f"{self.title} is already been checked out")
    def check_in(self):
        if not self.available:
            self.available = True
            print(f"{self.title} is succesfully checked in !")
        else :
            print(f"{self.title} is already been checked in !")

class Book(libraryitem):
    def __init__(self,itemid,title,author,genre):
        super().__init__(itemid,title)
        # libraryitem.__init__(self, itemid, title)
        self.author = author
        self.genre = genre
    def __str__(self):
        return f"book-  {super().__str__()} ,author - {self.author}, Genre - {self.genre}"                            

class library_collection:
    def __init__(self):
        self.items = []
    def add_items(self,item):
        self.items.append(item)
    def view_collection(self):
        for item in self.items:
            print(item)
    def check_out(self,item):
        item.check_out()
    def check_in(self,item):
        item.check_in()

bible = Book("1121","bible","god","awa") 
superbook = Book("020","superbook","wakokahibaw","hawha") 
oks = Book("10182","awanw","wawa","wawajwia") 
library = library_collection()
library.add_items(bible)
library.add_items(superbook)
library.add_items(oks)
library.view_collection()       
library.check_in(bible)
library.check_out(bible)
library.check_in(bible)