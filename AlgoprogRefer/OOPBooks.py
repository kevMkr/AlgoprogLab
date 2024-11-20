class Author():
    def __init__(self, name: str, email: str, gender: str):
        self.name=name
        self.email=email
        self.gender=gender
    def __str__(self)->str:
        return f"Author[name={self.name}, email={self.email},gender={self.gender}]"

class Book():
    author=[]
    def __init__(self,name: str, author: Author, price: float, qty:int=0) -> None:
        self.name=name
        self.author=author
        self.price=price
        self.qty=qty
        Book.author.append(author) if author not in Book.author else 1
    def getName(self) -> str:
        return self.name
    def getAuthor(self) -> Author:
        return self.author
    def getPrice(self) -> float:
        return self.price
    def getQty(self) -> int:
        return self.qty
    def setQty(self,qty: int) -> None:
        self.qty=qty
    def getAuthorNames() -> str:
        temp=""
        for i in Book.author: temp+=f"author={i.name},"
        return temp[:-1]

    def __str__(self) -> str:
        return f"Book[name={self.name},{str(self.author)},price={self.price},qty={self.qty}]"

testa=Author("a","a","a")
testc=Author("aa","a","a")
testd=Author("aa","a","a")
testb=Book("bb",testa,5)
Book("bb",testc,5)
Book("bbb",testd,5)
Book("bbbb",testd,5)

print(testa)
print(str(testb))

print("\n")
print(Book.getAuthorNames()) 