#convert npr to inr,usd,euro
npr = int(input("Enter amount in Nepali Rupee: "))
#the conversion rates
inrConver = 1.6
usdConver = 134.61
euroConver = 148.34
#converting and rounding to 2 decimal places
inr = round(npr/inrConver,2)
usd = round(npr/usdConver,2)
euro = round(npr/euroConver,2)
print(f'The equivalent in INR = {inr}, USD = ${usd} and EURO = {euro}')