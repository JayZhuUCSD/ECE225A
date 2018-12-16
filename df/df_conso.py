def df_conso(fname1='ca_law_enforcement_by_city.csv',fname2='ca_offenses_by_city.csv'):
    import pandas as pd
    data1 = pd.read_csv(fname1)
    data2 = pd.read_csv(fname2)

    for index2, row2 in data2.iterrows():
        data2.loc[index2, 'Total_Crime'] = int(row2['Violent crime'].replace(',',''))+int(row2['Property crime'].replace(',',''))
    data2_dict = dict(zip(data2['City'], data2['Total_Crime']))

    for index1, row1 in data1.iterrows():
        data1.loc[index1, 'Population'] = int(row1['Population'].replace(',',''))
        data1.loc[index1, 'Total_Employees'] = int(row1['Total law\renforcement\remployees'].replace(',',''))
        data1.loc[index1, 'Total_Officers'] = int(row1['Total \rofficers'].replace(',',''))
        data1.loc[index1, 'Total_Civilians'] = int(row1['Total \rcivilians'].replace(',',''))
        if row1['City'] in data2_dict.keys():
            data1.loc[index1, 'Total_Crime'] = data2_dict[row1['City']]
        else:
            data1.loc[index1, 'Total_Crime'] = None

    del data1['Total law\renforcement\remployees']
    del data1['Total \rofficers']
    del data1['Total \rcivilians']

    data1.to_csv('df_conso.csv')

df_conso(fname1='ca_law_enforcement_by_city.csv',fname2='ca_offenses_by_city.csv')
