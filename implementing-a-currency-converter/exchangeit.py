"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: MUHANNAD BANI ALMARJE
Date:   12/25/2020
"""
import currency

src=input('3-letter code for original currency: ')
dst=input('3-letter code for the new currency: ')
amt=input('Amount of the original currency: ')
result= currency.exchange(src,dst,amt)
result=round(result,3)

print('You can exchange '+str(amt)+' ' +src+ ' for '+str(result)+' '+dst+'.')