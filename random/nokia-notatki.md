# Typy w C++ -> są i to jak! (prezentacja 1)

## 1

C++ ma typy, pozwalają decydować jakie operacje są możliwe na danych zmiennych.

## 2  
### **Bity a bajty.**  

Bity mogą mieć wartość albo 1, albo 0. Natomiast bajt to po prostu 8 bitów.

## 3
### **Int - integer - liczba całkowita**  

Pokrywa liczby z przedziału od -2147483648 do + 2147483647  
**INTMAX_MAX** podaje maksymalną wielkość inta na naszej maszynie. Różne komputery będą miały różne. Oczywiście można sprecyzować rodzaj inta, np *int16*, *int32*, *int64*.

## 4  
### **Inne typy liczbowe**

*short* - zapewnia, że będzie 16 bitowy  
*long* - zapewnia, że będzie 32 bitowy  
*long long* - zapewnia, że będzie 64 bitowy  
Trzeba dopisywać typ zmiennej, np. *short int*, *short float*. Jeżeli nie dodamy co to jest to kompilator założy, że chodziło nam o *int*.  
  
*Unsigned* - pozwala tylko na 0 i wartości dodatnie.
*Signed* - liczby ze znakiem  

Przykłady:  
- *signed 16bit int* jest od -32768 do 32767  
- *unsigned 16bit int* jest od 0 do 65535  

## 5
### **Overflow i underflow**

Jeżeli zrobimy tak:  
- *unsigned int a = 0; a -= 1;*
To a będzie równe maksymalnej wartości unsigned inta. Licznik się *"przekręci"*.

*Underflow* jeżeli przeskoczymy od dołu.  
*Overflow* jeżeli od góry.

## 6
### **Char - podstępny typ numeryczny (znak)**  

Char to również liczba. Typ liczbowy oznaczający pojedynczy znak.  
Chary w C++ otaczamy pojedynczym apostrofem:
  - *'a', 'k', 'p', '\*', ']'*  

Chary też mogą być signed in unsigned.

## 7
## **Foating numbers - liczby zmiennoprzecinkowe**

*float, double i long double*  

Różnice między nimi dotyczą precyzji czyli jak daleko po przecinku to co zapisaliśmy jest dokładne.  
Trzeba uważać wykonując porównania między floatami, bo może się okazać, że coś najoczywistszego na świecie będzie się źle porównywało

Liczby składają się ze *znaku*, *eksponenty* i *mantysy*.  
**Wszystko jest na prezentacjach z *Podstaw informatyki* z pierwszego semestru** - warto powtórzyć i mieć zapisane.  

Jeżeli musimy porównać ze sobą dwa floaty to odejmujemy od siebie i porównujemy z **bardzo** niewielką liczbą.

## 8
### **Boolean - prawda/falłsz**  

Wszystko co jest inną wartością niż 0 jest uznawane za prawdę przy konwersji na *bool*.

Co ciekawe nie zajmuje jednego bita tylko więcej, ale nie było powiedziane dlaczego.

**SPRAWDZIĆ ^**  void

## 9
## **Wskaźniki! To on!**

Wskaźniki wskazują na jakąś zmienną czyli zawierają adres pamięci pod którym znajduje się zmienna.  

Wskaźniki puste inicjuje się jako *nullptr*.  

Wskaźnikowi trzeba powiedzieć na jaki typ wskazuje, żeby wiedział o ile się iterować i ogólnie ile miejsca zajmuje jedna taka zmienna. Np. wiadomo, że int będzie zajmował 32 bity (o ile dobrze pamiętam XD).

``` cpp
int a = 5;
int* pointer = &a;
std::cout << pointer << std::endl;
std::cout << *pointer;
```
Gwiazdki stawiamy po prostu przy nazwie typu przy inicjalizacji, a przy nazwie zmiennej przy dereferencji.

## 10
### **Referencje**  

Muszą mieć od razu przypisaną wartość.
``` cpp
int a = 5;
int& ref;
```
Zwróci błąd, bo ref nie będzie miało przypisanej wartości.  

```cpp
int a = 5;
int& ref = a;
std::cout << ref << std::endl;
++ref;
std::cout << ref << std::endl;
std::cout << a << std::endl;
```
wypisze:
```
5
6
6
```
Trzeba pamiętać, że to jest referencja, a nie kopia! Zmieniając zmienną *ref* zmieniamy również zmienną *a*.

Teraz słowo kluczowe ***const***.

Nie będzie można zmieniać jeżeli zainicjujemy coś *const*.

## 11
### **THE VOID** 

***void*** to typ *pusty* zwany również *niepełnym*, *empty*.  
Pozwala napisać funkcję, która nic nie zwraca.

```cpp
void returnsNothing()
{
    int a = 1;
    a += 1;
    return;
}
```

Istnieją wskaźniki typu pustego, ale jest to szara strefa i raczej jej nie będziemy używać. Takie wskaźniki operują na pamięci bez potrzeby wiedzenia co jest zapisane tam w pamięci.

# Wskaźniki i *const* rzeczy na które wskaźnik wskazuje (prezentacja 2)

## 1
### Od razu cyk myk gdzie się wywali kompilacja w tym

```cpp
#include <iostream>
union un 
{ 
    float f; int i[4]; 
}; 
int main() 
{ 
    float x = 70; 
    float* fp = &x;
    const float* cf = &x;
    float* const fc = &x; 
    x += 0.5; 
    std::cout << x << std::endl; 
    cf += 0.5;
    fc += 0.5; 
    fp += 0.5; 
    std::cout << x << std::endl; 
    float a = x;
    cf = a; 
    *fc = a; 
    cf++; 
    fc++; 
}
```
## 2
### **C type arrays**  

Tablica przechowuje kilka wartości tego samego typu.  
Trzeba przy jej tworzeniu zadeklarować ile takich elementów będzie w tablicy, bo C++ musi sobie zaznaczyć gdzie będzie koniec tablicy.  
Ten znak to:
```
    \0
```
Tablice w pewnym sensie są wskaźnikami, a w pewnym sensie nie.  
Zawsze kiedy są przekazywane do funkcji to są przekazywane jako wskaźniki.  

Jest funkcja `sizeof()`, która zwraca **wielkość (rozmiar w pamięci)** tablicy.

**Długość** tablicy można policzyć przez podzielenie sizeof() tablicy przez sizeof() jednego elementu.

**Do zmiennej tablicowej nie można przypisać adresu innej zmiennej**  

Poruszanie się po tablicy wygląda w ten sposób, że pobierany jest wskaźnik na pierwszy element i jest on inkrementowany odpowiednią liczbę razy.  

## 3
### **Różnice arr vs pointer**

array zawsze ma jeden więcej rozmiaru, bo musi mieć ten znak końcowy.

Jeżeli sprawdzić rozmiar wskaźnika to będzie miał tyle ile ma rzeczy tablica. Jeżeli tablicy to ma jeden więcej, a nawet dwa, ale nie ogarniam dlaczego - trzeba jeszcze raz obejrzeć.  

---

W tablicy możemy zwyczajnie podmienić wartości pod dowolnym indeksem.  

Modyfikowanie przy wskazaniu jest niemożliwe:
```cpp
*(char_ptr+1) = 'b';
```
Ten kod wywali błąd.

---

Trzeciej różnicy nie zdążyłem przeczytać :)

## 4
### **Strong typed language**

C++ jest silnie ztypizowanym językiem. Kompilacja jest w nim znacznie bardziej skomplikowana niż w językach, które nie zwracają uwagi na typy.  

Wiele problemów można wykryć w czasie kompilacji (statycznie), dzięki czemu nie mogą się wydarzyć w czasie wykonania programu (dynamicznie).  

Jeżeli ktoś uważa, że C++ jest bardzo restrykcyjny jeżeli chodzi o typy, to zaleca się zobaczenie *Rust*, który momentalnie ma poprawić ten pogląd - udowadniając, że C++ prawie nie narzuca na programistę żadnych restrykcji :).

## 5
### **Konwersja typów**

Type conversion. 

W nowoczesnym C++ używa się `auto`, ale w pewnym momencie zawsze napotyka się na sytuację, w której trzeba mieć dwie zmienne tego samego typu. Stąd konwersja typów.  

Można to robić na sposób `impicit` (jawny) i `explicit` (niejawny). Oczywiście bezpieczniejszy jest jawny (`implicit`). Jeżeli czegoś nie sprecyzujemy to kompilator to sobie zrobi sam i zrobi to najpewniej źle, albo po macoszemu. Najczęściej przy konwersji typów potrzebujemy jednak, żeby być pewnym niektórych rzeczy.  

