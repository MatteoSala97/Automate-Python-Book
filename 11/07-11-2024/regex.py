import re

''' 
https://regexr.com/

There was a young woman named Bright,
Whose speed was much faster than light.
She set out one day,
In a relative way,
And returned on the previous night. 

'''

lim = 'There was a young woman named Bright, Whose speed was much faster than light. She set out one day, In a relative way, And returned on the previous night. '

x = re.search("" , lim)




if x:
    print('Match trovato')
else:
    print('Match non trovato')
    

