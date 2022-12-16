card=input('Enter YES or NO if you have HDFC card')
card=card.upper()
membership=input('Enter YES or NO if you have membership')
membership=membership.upper()
price=int(input('Enter amount'))
if card=='YES' and membership=='YES':
    price=price-.05*price-50
elif card=='YES' or membership=='YES':
    price=price-50
print('Amount which you have to pay is',price)