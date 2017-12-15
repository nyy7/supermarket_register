#!/usr/bin/python
#########
# author: Yanyan Ni
# date: 12/15/17
# description: a function to calculate total price including tax
# input: Product Code
#########

class Calculator():
	def __init__(self, inputs):
		# cleanup input
		self.args = []
		for input in inputs.split(';'):
			self.args.append(input.strip())
		self.price_dict = {'A12T-4GH7-QPL9-3N4M':3.46, 'E5T6-9UI3-TH15-QR88':8.18, 'YRT6-72KAS-K736-L4AR':1.63, 'TQ4C-VV6T-75ZX-1RMR':6.78, '65P1-UDGM-XH2M-LQW2':5.89}
		self.name_dict = {'A12T-4GH7-QPL9-3N4M':'Cereal', 'E5T6-9UI3-TH15-QR88':'Chicken', 'YRT6-72KAS-K736-L4AR':'Pop', 'TQ4C-VV6T-75ZX-1RMR':'Pizza', '65P1-UDGM-XH2M-LQW2':'Tuna'}
		self.tax = 0.0875

	# function for input validation
	def input_validation(self):
		is_validate = True
		for arg in self.args:
			if len(arg) < 19:
				is_validate = False
			elif arg[:19].upper() not in self.price_dict:
				is_validate = False
		return is_validate

	# function for calculate total price
	def price_calculator(self):
		sum = 0.0
		for arg in self.args:
			sum = sum + self.price_dict[arg[:19].upper()]
		return sum

	# function for apply local tax
	def add_tax(self, price):
		return round(price * (1 + self.tax), 2)


