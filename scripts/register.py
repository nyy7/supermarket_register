#!/usr/bin/python
#########
# author: Yanyan Ni
# date: 12/15/17
# description: a function to run calculator and print proper output
# e.g. ./register.py "a12t-4gh7-qpl9-3n4ma"
#########
from calculator import Calculator
import sys, os

def run(sku):
	register = Calculator(sku)
	if register.input_validation():
		total_price = register.price_calculator()
		#print('Total amount of sale: %s' %total_price)
		price_with_tax = register.add_tax(total_price)
		#print('Taxes: %s' %(register.tax))
		#print('Final cost: %s' %(price_with_tax))
		print('%s' %(price_with_tax))
		return True 
	else:
		print("input is not valid")
		return False

if __name__=='__main__':
	if len(sys.argv) == 1:
		if 'SKU' in os.environ:
			sku = os.environ['SKU']
		else:
			print 'please set SKU in environmental variable'
			sys.exit()
	elif len(sys.argv) == 2:
		sku = sys.argv[1]
	else:
		print 'Wrong parameters, please input SKU of the product'
		sys.exit()

	run(sku)
