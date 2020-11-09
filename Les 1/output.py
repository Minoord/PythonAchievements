Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Michelle')
Mijn naam is Michelle
>>> naam = 'Michelle'
>>> print(naam)
Michelle
>>> print(naam.upper())
MICHELLE
>>> print (naam[0:2])
Mi
>>> print(naam {::-1])
SyntaxError: invalid syntax
>>> print (naam [::-1])
ellehciM
>>> leeftijd = 15
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Michelle ben je al 15 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> leeftijd = leeftijd - 1
>>> leeftijd
15
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print ('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    elif leeftijd > 18:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print ('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	elif leeftijd > 18:
		
SyntaxError: invalid syntax
>>> if leeftijd < 18:
        hoelang_tot18jaar = 18 - leeftijd
        print ('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('het is alweer ' + str(leeftijd) + 'jaar')
else: print ('je bent precies
	     
SyntaxError: EOL while scanning string literal
>>>  if leeftijd < 18:
	 
SyntaxError: unexpected indent
>>> if leeftijd < 18:
        hoelang_tot18jaar = 18 - leeftijd
        print ('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('het is alweer ' + str(leeftijd) + 'jaar')
else:
        print ('je bent precies	' + str(leeftijd) + ' jaar')

Over 3 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
686
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
780
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 780
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-16 11:40:12.770307
>>> datum.strftime('%A %d %B %Y')
'Wednesday 16 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 16 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 16 settembre 2020'
#Einde opdracht