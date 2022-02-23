import numpy as nu
class NullValues:
	df = None

	def __init__(self):
		pass

	def getOptions(self,df):
		self.df = df

		while(True):
			print("\n\n Options for Handling NULL Values \n")
			print("1. Show NULL Value info")
			print("2. Remove all rows with NULL Values")
			print("3. Fill NULL Values withe Mean")
			print("4. Fill NULL Values withe Mode")
			print("5. Fill NULL Values withe Median")
			print("6. Show the Dataset")

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
				self.showNull()
			elif opt == 2:
				self.rmNullCol()
			elif opt == 3:
				self.fillMean()
			elif opt == 4:
				self.fillMode()
			elif opt == 5:
				self.fillMedian()
			elif opt == 6:
				self.showDataset()
			else:
				print(f"{opt} is not a valid option!")

		return self.df

	def showNull(self):
		print(self.df.isnull())
		print(self.df.isnull().sum())

	def rmNullCol(self):
		while(True):
			colName = input("Which column to Remove: ")
			if colName in self.df:
				self.df = self.df.drop([colName], axis=1)
				break
			else:
				print("The column name is invalid!")
		

	def fillMean(self):
		while(True):
			colName = input("Which column to fill:")
			if colName in self.df.columns:
				if self.df.dtypes[colName] != 'object':
					mean_value = self.df[colName].mean()
					self.df[colName].fillna(value=mean_value, inplace=True)
				else:
					print("Cannot Replace with Mean")
				break
			else:
				print("invalid column name")

	def fillMode(self):
		while(True):
			colName = input("Which column to fill: ")
			if colName in self.df.columns:
				mode_value = df[colName].mode()
				df[colName].fillna(value=mode_value, inplace=True)
				break
			else:
				print("The column name is invalid!")

	def fillMedian(self):
		while(True):
			colName = input("Which column to fill: ")
			if colName in self.df.columns:
				if df.dtypes[colName] != 'object':
					median_value = df[colName].median()
					df[colName].fillna(value=median_value, inplace=True)
				elif df.dtypes[colName] == 'object':
					print("Cannot replace with Median")
				break
			else:
				print("The column name is invalid!")

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






