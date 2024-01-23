# Soru 1 : 1'den 10'a kadar olan sayıları ekrana yazdıran bir Python kodu yazınız.

for i in range(1,11):
   print(i)

# Soru 2 : Kullanıcıdan bir sayı girişi alın ve bu sayıya kadar olan 
# çift sayıları ekrana yazdıran bir Python programı yazın. 
# Bunu once 'for' ile sonra 'while' donguleri ile yapiniz.
    
number = int(input("Please enter a number that you want to check even or odd:  "))

if number % 2 == 0:
    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number. ")
