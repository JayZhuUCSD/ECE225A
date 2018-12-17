def df_county(fname1='ca_law_enforcement_by_county.csv',fname2='ca_offenses_by_county.csv'):
    import pandas as pd
    import math
    data1 = pd.read_csv(fname1)
    data2 = pd.read_csv(fname2)

    for index2, row2 in data2.iterrows():
        if math.isnan(float(str(row2['Violent crime']).replace(',',''))) or math.isnan(float(str(row2['Property crime']).replace(',',''))):
            data2.loc[index2, 'Total_Crime']=None
        else:
            data2.loc[index2, 'Total_Crime'] = float(str(row2['Violent crime']).replace(',',''))+float(str(row2['Property crime']).replace(',',''))
    data2_dict = dict(zip(data2['County'], data2['Total_Crime']))

    for index1, row1 in data1.iterrows():
        data1.loc[index1, 'Total_Employees'] = int(row1['Total law\renforcement\remployees'].replace(',',''))
        data1.loc[index1, 'Total_Officers'] = int(row1['Total\rofficers'].replace(',',''))
        data1.loc[index1, 'Total_Civilians'] = int(row1['Total\rcivilians'].replace(',',''))
        if row1['County'] in data2_dict.keys():
            data1.loc[index1, 'Total_Crime'] = data2_dict[row1['County']]
        else:
            data1.loc[index1, 'Total_Crime'] = None

    del data1['Total law\renforcement\remployees']
    del data1['Total\rofficers']
    del data1['Total\rcivilians']

    data3 = data1
    data3['Total_Crime_Rank'] = data3['Total_Crime'].rank(ascending=True, method='max', na_option='bottom')
    data3 = data3.sort_values(by = ['Total_Crime_Rank'])

    data3.to_csv('df_county.csv')

df_county(fname1='ca_law_enforcement_by_county.csv',fname2='ca_offenses_by_county.csv')
