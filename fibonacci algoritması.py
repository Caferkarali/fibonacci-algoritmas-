# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:44:35 2023

@author: Cafer Karali
"""
def fibonacci(n):
    fib_sequence = [0, 1]

    # Fibonacci sayılarının hesaplanması
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)

    # İstenen sayı kadar Fibonacci sayısının döndürülmesi
    return fib_sequence[:n]
# Kullanıcıdan bir sayı alınması
num = int(input("Bir sayı girin: "))

# Fibonacci sayılarının hesaplanması ve ekrana yazdırılması
result = fibonacci(num)
print(result)