class baza:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.__c = 5
        self._d = 10
    
    def __str__(self) -> str:
        return f"To jest przykładowy tekst do printowania {self.a}"
    
    def __eq__(self, __o: object) -> bool:
        return __o.b == self.b
    
bz = baza(1,2)
print(bz.a, bz.b, bz._d)
print(bz)
az = baza(5,3)
print(bz == az)