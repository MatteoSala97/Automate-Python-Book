import logging
import random


# Esercizio sull'utilizzo di logging

'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total)) 
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5)) 
logging.debug('End of program')


'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''

# Esercizio sull'utilizzo di random per lanciare una moneta

heads= 0 

for i in range( 1, 1001): 
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print("halfway done")
        
    print("heads came up " + str(heads) + "times") 
    
'''

# Esercizio per trovare i palindromi secondo user input

def find_palindromes(words):
    palindromes = []
    for i in words: 
        if i == i[::-1]:
            palindromes.append(i)
    return palindromes

# Raccogliere le parole dall'utente
words = []
while True:
    userInput = input("Input a word ").lower()
    if userInput == "quit":
        break
    words.append(userInput)

# Trovare e stampare le parole palindrome
palindromes = find_palindromes(words)
print("Palindromes:", *palindromes, sep='\n')
