import frappe, os
import pandas as pd

class by_zipcode:
	def __init__(self, zipcode):
		self.zipcode = int(str(zipcode).strip())
		self.csv_input = pd.read_csv(frappe.get_pymodule_path("autofill_indiazipcode", "dataset", "all_india_zipcode.csv"), encoding ='latin1',  sep=',', \
							engine='python', quotechar = '"', skipinitialspace=True )
	
	def is_valid(self):
		if self.zipcode in csv_input['pincode'].tolist(): 
			return True
		else:
			return False
		
	def values(self):	   
		self.csv_input.set_index('officename', inplace=True)
		mask = self.csv_input.loc[self.csv_input['pincode'] == self.zipcode]
		return (mask)
	
	def values_dict(self):	   
		self.csv_input.set_index('officename', inplace=True)
		mask = self.csv_input.loc[self.csv_input['pincode'] == self.zipcode]
		return (mask).to_dict()
	
	def to_json(self):
		return self.values().to_json()
	
	def to_dict(self):
		return self.values().to_dict()