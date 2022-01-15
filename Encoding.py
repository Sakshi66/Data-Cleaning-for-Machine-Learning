from numpy import asarray
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

class Encoding:
	df = None
	df_cat = None
	def __init__(self, df):
	    #self.data = []
	    self.df = df
	    self.df_cat = df.select_dtypes(include =['object'])

	    # getOptions()

	def getOptions(self,):
		x = 1
		while(x):
			print("\n\n Tasks \n")
			print("1. Show Categorical Columns")
			print("2. Perform Ordinal Encoding")
			print("3. Perform One Hot Encoding")
			print("4. Show the Dataset")

			try:
				val = input("\nWhat would you like to do? (Enter -1 to exit): ")
				opt = int(val)
				print("")
			except:
				print(f"{val} is not a valid option!")
				continue

			if opt == -1:
				break;
			elif opt == 1:
				self.showCatCols()
			elif opt == 2:
				self.ordinalEncoding()
			elif opt == 3:
				self.oneHotEncoding()
			elif opt == 4:
				self.showDataset()
			else:
				print(f"{opt} is not a valid option!")
		return self.df

	def showCatCols(self,):
		df_cat_unique = self.df_cat.nunique().to_frame().reset_index()
		df_cat_unique.columns = ['Variable','DistinctCount']
		print(df_cat_unique)

		# self.getOptions()

	def ordinalEncoding(self):
		pass

	def oneHotEncoding(self):
		x = 1
		while(x):
			colName = input("Which column to performe Ordinal Encoding on: ")
			if colName in self.df:
				x = 0

				# encoded_df = pd.get_dummies(self.df.colName)
				encoded_df = pd.get_dummies(self.df[[colName]])
				# This returns a new dataframe with a column for every unique value that exists,
				# along with either a 1 or 0 specifying the presence of that rating for a
				# given observation.

				# we want this to be part of the original dataframe. In this case, we attach our
				# new dummy coded frame onto the original frame using "column-binding.
				# pd.concat([df, encoded_df], axis=1)
				self.df = pd.concat([self.df, encoded_df], axis=1)

				# Dropping the original column
				self.df = self.df.drop([colName], axis=1)

			else:
				print("The column name is invalid!")

	def showDataset(self):
		n = 1
		while(1):
			try:
				val = input("How many rows to print(>0): ")
				n = int(val)
				break;
			except:
				print(f"{val} is not a valid option!")

		print(self.df.head(n))


