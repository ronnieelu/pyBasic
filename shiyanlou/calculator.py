import sys
# 挑战一
# 知识点：
# 1. 函数
# 2. sys.argv ，参数类型
# 3. 抛出异常
# 4. Raise异常
# 5. {：.2f}.format(para)  format数字格式化输出


base = 3500

def RealSal(sal,taxSal):
	if taxSal <= 1500:
		rate, ofee = 0.03, 0
	elif taxSal > 1500 and taxSal <= 4500:
		rate, ofee = 0.1, 105
	elif taxSal > 4500 and taxSal <= 9000:
		rate, ofee = 0.2, 555
	elif taxSal > 9000 and taxSal <= 35000:
		rate, ofee = 0.25, 1005
	elif taxSal > 35000 and taxSal <= 55000:
		rate, ofee = 0.3, 2755
	elif taxSal > 55000 and taxSal <= 80000:
		rate, ofee = 0.35, 5505
	elif taxSal > 80000:
		rate, ofee = 0.45, 13305

	real_tax = taxSal * rate - ofee
	return real_tax

if __name__ == '__main__':
		try:
			if len(sys.argv) > 2:
				raise Exception("Parameter Error1")	
			elif isinstance(sys.argv[1],int) == 'false':
				raise Exception("Parameter Error2")

			sal = int(sys.argv[1])
			taxSal = sal - base
			pay_tax = RealSal(sal, taxSal)

			print('{:.2f}'.format(pay_tax))
		except Exception as e:
			print("Parameter Error3",e)