class Book:

    def __init__(self,title):
        self.title = title


    def __str__(self):
        return f"Book title is: {self.title}"  

    def __len__(self):
        return len(self.title)

b = Book("My own Story")        
print(b)
print(len(b))