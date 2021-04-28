import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


class RFTest:

    def __init__(self):
        self.filename = '/Users/aakas/CollegeProject/VirtualClinic/VirtualClinic/RF_disease.sav'
        # self.df = pd.read_csv('/Users/mac/Desktop/LOC3.0_Scam-2021/Scam2021/Scam2021/Symptom-severity.csv')
        self.df = pd.read_csv("/Users/aakas/CollegeProject/VirtualClinic/VirtualClinic/Symptom-severity.csv")
        # self.load_model()

    def load_model(self):
        cols = self.df.columns
        data = self.df[cols].values.flatten()

        s = pd.Series(data)
        s = s.str.strip()
        s = s.values.reshape(self.df.shape)

        self.df = pd.DataFrame(s, columns=self.df.columns)

        self.df = self.df.fillna(0)

        df1 = pd.read_csv("/Users/aakas/CollegeProject/VirtualClinic/VirtualClinic/Symptom-severity.csv")

        vals = self.df.values
        symptoms = df1['Symptom'].unique()

        for i in range(len(symptoms)):
            vals[vals == symptoms[i]] = df1[df1['Symptom'] == symptoms[i]]['weight'].values[0]

        d = pd.DataFrame(vals, columns=cols)

        d = d.replace('dischromic _patches', 0)
        d = d.replace('spotting_ urination', 0)
        self.df = d.replace('foul_smell_of urine', 0)

        (self.df[cols] == 0).all()
        # print(self.df)

    def RF_Predict(self, a):
        model = joblib.load(self.filename)
        preds = model.predict([a])
        return preds
        

    def get_dis(self):
        new2 = self.df
        dis = []
        dis = self.df['Symptom'].unique()
        a = list(dis)
        d = {}
        for i in range(len(a)):
            d[a[i]] = i
        return d

if __name__ == "__main__":
    a = []
    model = RFTest()
    # a = [2,8,5,3]
    df1 = pd.read_csv("/Users/aakas/CollegeProject/VirtualClinic/VirtualClinic/Symptom-severity.csv")

    symptoms = df1['Symptom'].unique()
    for x,i in  enumerate(symptoms) :
        print(x,i,end="//")
    print("\nEnter Symptoms by their respective numbers")
    a = list(map(int, input().split()))
    x = len(a)
    for i in  range(x,17):
        a.append(0)
    result = model.RF_Predict(a)
    # print(result[0])
    # print("Disease Severity")

