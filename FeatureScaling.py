
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
				self.standardization()
			elif opt == 2:
				self.normalization()
			elif opt == 3:
				self.showDataset()
			else:
				print(f"{opt} is not a valid option!")

		return self.df

	def getNorOptions(self):
		pass

	def getStdOptions(self):
		pass

	def standardization(self):
		pass

	def normalization(self):
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

