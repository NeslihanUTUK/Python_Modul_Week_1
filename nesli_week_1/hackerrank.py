# 1-  https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

# 2- https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
print(arr[-2])

# 3- https://www.hackerrank.com/challenges/python-print/problem

n = int(input().strip())
for i in range(1, n + 1):
    print(i, end='')

# 4- https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input())    
student_marks = {}
for _ in range(n):
       name, *line = input().split()
       scores = list(map(float, line))
       student_marks[name] = scores
query_name = input()
scores = student_marks[query_name]
average = sum(scores) / len(scores)
print(f"{average:.2f}") #virgulden sonra ii basamak icin

#n sayisi kadar for dongusu calisir
#ilk girdileri name yaparken digerleri line oldu.

#Girdileri hackerrank otomatik aliyor.
#ilk olarak kac ogrenci oldugunu n alir
#sozluk olusturur

#her ogrencinin ismini bir anahtar(key), notlarinin ise bir liste olarak student_marks sozlugune ekler
#sorgu calistirir:kullanicidan sorgulamak istedigi ogrencinin adini alir ve o ogrencinin notlarini bulur
#Notlarin ortalamasini hesaplar ve yazdirir :

#1ogrencileri ve notlari toplami:
#student_marks[name] = scores
#bu islem for dongusu icinde olur ve her ogrencinin adi(name)ile notlari(scores) sozluge eklenir

#2 kullanicinin sorgulanmasi:
#query_name = input()
#scores =students_marks[query_name]

#kullanicidan bir isim alinir ve bu ismi kullanarak solukten ilgili notlara ulasiriz
#numbers = ["1,"2","3","4"]

#map fonksiyonu kullanilir
#result = map(int, numbers) 
#print(result)
#print(list(result)) 