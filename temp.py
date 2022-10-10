import pandas as p
import numpy as np
df_app = p.read_csv('./data_files/application_record.csv')
df_credit = p.read_csv('./data_files/credit_record.csv')

#credit card application: 
#print(df_app.head(5))




a = df_credit['STATUS'].value_counts()
print(a)


















#will not be used, going with method twoLF will be replaced by CRLF the next time Git touches it

#this function compares the id of df_app_rec & cred_id to see if they were approved
#saves who was approved and returns an array of boolean values. 
#the index represent the specific row's boolean value
# def get_passed_app():
#     cred_id = df_credit['ID'].unique().copy()
    
#     app_id = df_app["ID"].copy()
    
#     bool_arr = np.isin(app_id, cred_id)
#     return np.array(bool_arr)
# classes = get_passed_app()
# app_length = len(classes)
# app_length


# with open('test2.csv', 'r') as f:          # Read lines separately
#     reader = csv.reader(f, delimiter='t')
#     for i, line in enumerate(reader):
#         print(i, line)













# def classify():
#     df_app_rec['approved'] =''
#     cred_id = df_cred_rec['ID'].unique().copy()
#     app_id = df_cred_rec['ID'].copy()
#     for row in cred_id:
#         print(row)
#         print(df_cred_rec.where(df_cred_rec["ID"] == row) == True)
# classify()