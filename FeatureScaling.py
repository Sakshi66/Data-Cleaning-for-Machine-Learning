import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class FeatureScaling:
	df = None

	def __init__(self):
		pass

	def getOptions(self,df):
		self.df = df

		while(True):
			print("\n\n Feature Scaling Options \n")
			print("1. Perform Normalization(MinMax Scaler)")
			print("2. Perform Standardization(Standard Scaler)")
			print("3. Show the Dataset")

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
				self.norOne()
			elif opt == 2:
				self.stdOne()
			elif opt == 3:
				self.showDataset()
			else:
				print(f"{opt} is not a valid option!")

		return self.df

	def getNorOptions(self):
		while(True):
			print("\n\n Normalization Options \n")
			print("1. Perform Normalization on all Columns")
			print("2. Perform Normalization on a Specific Column ")
			print("3. Show the Dataset")

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
				self.norAll()
			elif opt == 2:
				self.norOne()
			elif opt == 3:
				self.showDataset()
			else:
				print(f"{opt} is not a valid option!")

	def getStdOptions(self):
		while(True):
			print("\n\n Standardization Options \n")
			print("1. Perform Standardization on all Columns")
			print("2. Perform Standardization on a Specific Column ")
			print("3. Show the Dataset")

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
				self.stdAll()
			elif opt == 2:
				self.stdOne()
			elif opt == 3:
				self.showDataset()
			else:
				print(f"{opt} is not a valid option!")

	def stdOne(self):
		dataTypeSeries = self.df.dtypes
		print('Data type of each column of Dataframe :')
		print(dataTypeSeries)
		print("")

		while(True):
			col = input("Enter column to Standardize: ")
			if col in self.df:
				dTypeCol = self.df.dtypes[col]
				if dTypeCol == "int64":
					self.df[col] = (self.df[col] - self.df[col].mean()) / self.df[col].std()
					break
				else:
					print("Cannot perform feacture encoding on {col} column")
			else:
				print("The column name is invalid!")

	def stdAll(self):
		pass

	def norOne(self):
		dataTypeSeries = self.df.dtypes
		print('Data type of each column of Dataframe :')
		print(dataTypeSeries)
		print("")

		while(True):
			col = input("Enter column to Normalize: ")
			if col in self.df:
				dTypeCol = self.df.dtypes[col]
				if dTypeCol == "int64":
					s = (self.df[col].max() - self.df[col].min()) 
					self.df[col] = (self.df[col] - self.df[col].min()) / s
					break;
				else:
					print("Cannot perform feacture encoding on {col} column")
			else:
				print("The column name is invalid!")

	def norAll(self):
		pass

	def showDataset(self):
		n = 1
		while(True):
			try:
				val = input("How many rows to print(>0): ")
				n = int(val)
				break;
			except:
				print(f"{val} is not a valid option!")

		print(self.df.head(n))

