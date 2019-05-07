"""
Вхідні дані: рядок, передається в програму як аргумент командного рядка. Може містити пробіли та літери латинського алфавіту в будь-якому регістрі. Для передачі в якості одного аргументу рядок береться в подвійні лапки.

Результат роботи: рядок - дешифроване повідомлення.

Наприклад

Вхідні дані: I canT DAnCE i CANt TAlK Hey
видаляємо пробіли, розбиваємо на групи по 5 символів: IcanT DAnCE iCANt TAlKH ey
ey відкдається
символи нижнього регістру перетворюються в a, верхнього - в b: baaab bbabb abbba bbabb
декодуємо, використовуючи ключ:
baaab = w
bbabb = i
abbba = k
bbabb = i
Результат: wiki
Вхідні дані: Hot sUn BEATIng dOWN bURNINg mY FEet JuSt WalKIng arOUnD HOt suN mAkiNG me SWeat
видаляємо пробіли, розбиваємо на групи по 5 символів: HotsU nBEAT IngdO WNbUR NINgm YFEet JuStW alKIn garOU nDHOt suNmA kiNGm eSWea t
t відкдається
символи нижнього регістру перетворюються в a, верхнього - в b: baaab abbbb baaab bbabb bbbaa bbbaa babab aabba aaabb abbba aabab aabba abbaa
декодуємо, використовуючи ключ:
baaab = w
abbbb = e
baaab = w
bbabb = i
bbbaa = l
bbbaa = l
babab = r
aabba = o
aaabb = c
abbba = k
aabab = y
aabba = o
abbaa = u
Результат: wewillrockyou
"""

import sys
s_input = input("Enter:")
s_output=''
count=0
list=[]
dictonary={"aaaaa":'a', "aaaab":'b', "aaabb":'c',
	"aabbb":'d', "abbbb":'e', "bbbbb":'f',
	"bbbba":'g', "bbbab":'h', "bbabb":'i',
	"babbb":'j', "abbba":'k', "bbbaa":'l',
	"bbaab":'m', "baabb":'n', "aabba":'o',
	"abbab":'p', "bbaba":'q', "babab":'r',
	"ababb":'s', "babba":'t', "abbaa":'u',
	"bbaaa":'v', "baaab":'w', "aaaba":'x',
	"aabab":'y', "ababa":'z'}

for i in s_input:
	if i == " ":
		s_input=s_input.replace(i, '')
	elif i.islower() == True:
		s_input=s_input.replace(i, "a")

for i in s_input:
	if i.isupper() == True:
		s_input=s_input.replace(i, "b")

while count < len(s_input):
	list.append(s_input[count:count+5])
	count+=5
	for i in list:
		if len(i) < 5:
			del list[list.index(i)]

for a in list:
	for i in dictonary.keys():
		if i == a:
			s_output=s_output + dictonary.get(i)

print(s_output)
