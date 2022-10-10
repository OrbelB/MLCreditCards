import pandas as p
import csv
test =  p.read_csv('./data_files/test.csv')
test2 = p.read_csv('./data_files/test2.csv')
test.head(8)
test2.head()
test["app"] = ""

with open('test2.csv', 'r') as f:          # Read lines separately
    reader = csv.reader(f, delimiter='t')
    for i, line in enumerate(reader):
        print(i, line)










def classify():
    df_app_rec['approved'] =''
    cred_id = df_cred_rec['ID'].unique().copy()
    app_id = df_cred_rec['ID'].copy()
    for row in cred_id:
        print(row)
        print(df_cred_rec.where(df_cred_rec["ID"] == row) == True)
classify()