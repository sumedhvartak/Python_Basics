def balance(str):

	poscount = 0
	negcount = 0
	y = list(str)
	for i in y:
		if i in ['(']:
			poscount+=1
			print('Positive count ',count)
		elif i in [')']:
			negcount-=1
			print('Negative count ',count)
		else:
			return "imbalance"
	if count % 2 == 0:
		return "balance"
	else:
		return "imbalance"


val = balance('(((((()()()(')
print(val)