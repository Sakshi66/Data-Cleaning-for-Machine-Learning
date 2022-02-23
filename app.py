import sys
import os
import pandas as pd
import numpy as nu
import seaborn as sns

# importing project modules
import DataDescription as dd
import NullValues as nv
import Encoding as en
import FeatureScaling as fs
import Downloading as dw

def getTargetVariable():
    # getting the columns of the dataframe
    cols = list(df.columns)
    print("Columns:")
    #print(*cols)            # *cols to just print names without "," and "[]"
    print('   '.join(cols))

    while(True):
        var = str(input("\n What is the target variable? (-1 to exit): "))
        if var == "-1":
            sys.exit("BYE!")
        elif var in cols:
            break;
        else:
            print("Incorrect column name!")

    return var

def getTask():    
    print("\n\n Tasks (Preprocessing) \n")
    print("1. Data Description")
    print("2. Handling NULL Values")
    print("3. Encoding Categorical Data")
    print("4. Feature Scaling of the Dataset")
    print("5. Download the Modified Dataset")

    opt = 0
    while(True):
        try:
            val = input("\nWhat would you like to do? (Enter -1 to exit): ")
            opt = int(val)
        except:
            print(f"{val} is not a valid option!")
            continue
        
        if opt == -1:
            return opt 
        if (opt >= 1) and (opt <=5):
            return opt
        else:
            print(f"{opt} is not a valid option!")



def main():
    print("WELCOME TO MACHINE LEARNING PREPROCESSING CLI \n")

    # Getting the data file and checking if it is the right format.
    # only .csv extension files are allowed.
    # file should be in the same directory.
    try:
        file = sys.argv[1]
        x = file.split(".")
    except:
        sys.exit("No file passed!")  

    try:
        if(x[1] != "csv"):
        #    print("Accepted")
        #else:
            sys.exit("Only .csv extension files allowed!")
    except:
        sys.exit("Only .csv extension files allowed!")

    if not os.path.isfile(file):
        sys.exit(f"The file {file} not found!")


    # using the pandas library to convert the csv file to a dataframe
    # the data frame is stored in df variable
    # Encountered a unicode error so changed encoding from unicode(default) to unicode_escape
    global df
    df = pd.read_csv(file, sep='\t+', engine='python', encoding = 'unicode_escape')
    
    DescObj = dd.DataDescription()  # Data Description Object
    NullObj = nv.NullValues()   # NULL Values Handling Object
    EncObj = en.Encoding()    # Data Encoding Object
    ScObj = fs.FeatureScaling()      # Feature Scaling Object
    DwObj = dw.Downloading()     # Downloading Object

    # targetVar = getTargetVariable()
    

    while(True):
        task = getTask()
        if task == -1:
            break
        elif task == 1:
            df = DescObj.getOptions(df)
        elif task == 2:
            df = NullObj.getOptions(df)
        elif task == 3:
            df = EncObj.getOptions(df)
        elif task == 4:
            df = ScObj.getOptions(df)
        elif task == 5:
            pass
        else:
            pass

        """If the user has selected exit option here the while loop will terminate. For every
        option we will call the respective function. when in that function -1 is entered,
        control will return back to the while loop and getTask() function will be run again.
        This will continue until the user selects -1 in the getTask() function."""

    print(df.head(15))
    sys.exit("ENDGAME!")



if __name__ == "__main__":
    main()