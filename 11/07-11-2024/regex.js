// https://regexr.com/

/* 
There was a young woman named Bright,
Whose speed was much faster than light.
She set out one day,
In a relative way,
And returned on the previous night.

22 . à#ù ○•ÈÐ£Ô ↑↓7Œ WJ├ó╩Á±b} ↓3z½x¬3      

*/


let lim = 'There was a young woman named Bright, Whose speed was much faster than light. She set out one day, In a relative way, And returned on the previous night. '

let x = re.search("" , lim)



// if x:
//     print('Match trovato')
// else:
//     print('Match non trovato')
    
/*
\d = esc solo numeri
\D = esc tutto tranne i numeri

\w = esc solo words
\W = esc tutto quello che non è words (spazi, virgole, punti, etc) - non i numeri

\s = esc spazi
\S = esc i non spazi - (numeri sì - caratteri speciali sì)
*/

/*

NUMERI DA MATCHARE:

+39 3338887777
+39 333 888 7777
39 3338887777
(+39) 3338887777
(+39) 333-888-7777

BOSS FINALE DELLA REGEX LIVELLO 9000:

\(?\+?39\)?[ -]?(\d{3})[ -]?(\d{3})[ -]?(\d{4})




REGEX PER TROVARE UN'EMAIL: 

MAIL DA MATCHARE: 

aloha123@gmail.com
alooo22@net.it

[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}


*/