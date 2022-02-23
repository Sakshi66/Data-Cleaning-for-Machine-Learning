import pandas as pd
import numpy as np

df = pd.read_csv("sample1.csv")


def numberOfNullValue():
    print(df.isnull().sum())


def removeColumn():
    colName = input("Which column:")
    if colName in df.columns:
        df.pop(colName)


def fillWithMean():
    colName = input("Which column:")
    if colName in df.columns:
        if df.dtypes[colName] != 'object':
            mean_value = df[colName].mean()
            df[colName].fillna(value=mean_value, inplace=True)
        elif df.dtypes[colName] == 'object':
            print("invalid column name")


def fillWithMode():
    colName = input("Which column:")
    if colName in df.columns:
        if df.dtypes[colName] != 'object':
            mode_value = df[colName].mode()
            df[colName].fillna(value=mode_value, inplace=True)
        elif df.dtypes[colName] == 'object':
            print("invalid column name")


def fillWithMedian():
    colName = input("Which column:")
    if colName in df.columns:
        if df.dtypes[colName] != 'object':
            median_value = df[colName].median()
            df[colName].fillna(value=median_value, inplace=True)
        elif df.dtypes[colName] == 'object':
            print("invalid column name")
