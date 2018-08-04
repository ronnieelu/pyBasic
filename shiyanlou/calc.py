import sys

base = 3500

def RealSal(sal,taxSal):
	if taxSal <= 1500:
		rate = 0.03
		ofee = 0
		real_tax = taxSal*rate - ofee
	elif taxSal > 1500 and taxSal <= 4500:
		rate = 0.1
		ofee = 105
		real_tax = taxSal*rate - ofee
	elif taxSal > 4500 and taxSal <= 9000:
		rate = 0.2
		ofee = 555
		real_tax = taxSal*rate - ofee
	elif taxSal > 9000 and taxSal <= 35000:
		rate = 0.25
		ofee = 1005
		real_tax = taxSal*rate - ofee
	elif taxSal > 35000 and taxSal <= 55000:
		rate = 0.3
		ofee = 2755
		real_tax = taxSal*rate - ofee
	elif taxSal > 55000 and taxSal <= 80000:
		rate = 0.35
		ofee = 5505
		real_tax = taxSal*rate - ofee
	elif taxSal > 80000:
		rate = 0.45
		ofee = 13505
		real_tax = taxSal*rate - ofee			
	else: 
		print("More")	

	return real_tax

# taxSal = sal - fee - base
# real_tax = taxSal*rate - ofee

if __name__ == '__main__':
	try:
		if len(sys.argv) >2:
# Here raise Exception and with ur own error message			
			raise Exception("Parameter Error")
		elif isinstance(sys.argv[1],int) == 'false':
			raise Exception("Parameter Error")
## First arg is file name, and then use 1		
		sal = sys.argv[1]
		taxSal = sal - base	
		pay_tax = RealSal(sal,taxSal)
		print(pay_tax)
## Here should use "as e"
	except Exception:
		print("Parameter Error")

		

