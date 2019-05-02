Вхідні дані: рядок, передається в програму як аргумент командного рядка. Може містити пробіли, літери латинського алфавіту в будь-якому регістрі та цифри. Для передачі одним значенням рядок, що містить пробіли, береться в подвійні лапки.

Результат роботи: рядок "YES", якщо отриманий рядок є паліндромом, або "NO" - якщо ні. Рядок вважається паліндромом, якщо він однаково читається як зліва направо, так і справа наліво. Відмінністю регістрів та пробілами знехтувати.

Наприклад
Вхідні дані: 0
Приклад виклику: python lab4_1.py 0
Результат: YES
Вхідні дані: puppy
Приклад виклику: python lab4_1.py puppy
Результат: NO
Вхідні дані: "mystring1Gni rts ym"
Приклад виклику: python lab4_1.py "mystring1Gni rts ym"
Результат: YES

import sys

# function to check string is  
# palindrome or not 
def isPalindrome(s):
    # Using predefined function to
    # reverse to string print(s) 
    rev = ''.join(reversed(s))

    # Checking if both string are  
    # equal or not 
    if (s == rev):
        return True
    return False


# main function
s = sys.argv[-1]
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No") 
