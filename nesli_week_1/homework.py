#question 2
# Take a number input from the user and write a Python program that prints even numbers up to this number on the screen.
#  Do this first with 'for' and then with 'while' loops.

#Kullanıcıdan bir sayı girdisi alın ve bu sayıya kadar olan çift sayıları ekrana yazdıran bir Python programı yazın.
# Bunu önce 'for' sonra 'while' döngüleriyle yapın.


"""
n = int(input("bir sayi girin: "))
for i in range(0, n+1):
    if i%2 == 0:
        print(i)
"""

""""

n = int(input("bir sayi giriniz: "))
i = 0
while i <= n:
    if i %2 == 0:
        print(i)
    i = i+1

"""

# Question 6: 
# Write a Python code that receives a number from the user and checks whether this number is prime.
## Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazın.
"""
sayi = int(input("Bir sayi girin: "))

if sayi < 2:
    print(f"{sayi} bir asal sayi degildir.")
else:
    for i in range(2, sayi):
        if sayi % i == 0:
                print(f"{sayi} asal sayi degildir")
                break
    else:
        print(f"{sayi} bir asal sayidir. ")

"""


#Question 10: Write the code that calculates the person's weight index and returns the result as underweight, 
#overweight or overweight according to the index value. (You can look on the internet for the weight index calculation) 
# To do this, ask the user for their weight and height measurements. weight index If it is below 25, it is weak, 
# Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight.



"""" #Soru 10: Kişinin kilo endeksini hesaplayan ve sonucu düşük kilolu olarak döndüren kodu yazın, 
Endeks değerine göre aşırı kilolu veya fazla kilolu. (Ağırlık endeksi hesaplaması için internete bakabilirsiniz) 
Bunu yapmak için kullanıcıdan kilo ve boy ölçümlerini isteyin. kilo endeksi 25'in altındaysa zayıf, 25-30 arası normal, 
30-40'ın üzerindeyse kilolusunuz. 40'ın üzerindeyseniz fazla kilolusunuz.
"""
boy = float(input("boyunuzu giriniz: "))
kilo = float(input("kilonuzu girniz: "))
vucut_kitle_indeksi = float(kilo / boy ** 2)
print("vucut kitle indeksiniz: ", vucut_kitle_indeksi)

if (vucut_kitle_indeksi <= 30):
    if (vucut_kitle_indeksi < 25):
        print("zayifsiniz")
    else:
        print("normal kilodasiniz.")
elif (vucut_kitle_indeksi >= 40):
    print ("asiri kilolusunuz")
else:
    print ("kilolusunuz")
    