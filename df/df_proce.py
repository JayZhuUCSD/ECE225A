def df_proce(fname='df_conso.csv'):
    import pandas as pd
    data3 = pd.read_csv(fname)

    for index3, row3 in data3.iterrows():
        data3.loc[index3, 'Employees_PTP'] = format((row3['Total_Employees']/row3['Population']*1000),'.2f')
        data3.loc[index3, 'Officers_PTP'] = format((row3['Total_Officers']/row3['Population']*1000),'.2f')
        data3.loc[index3, 'Civilians_PTP'] = format((row3['Total_Civilians']/row3['Population']*1000),'.2f')
        data3.loc[index3, 'Crime_PTP'] = format((row3['Total_Crime']/row3['Population']*1000),'.2f')

    data3['Crime_PTP_Rank'] = data3['Crime_PTP'].rank(ascending=0,method='min').fillna(218)
    data3 = data3.sort_values(by = ['Crime_PTP_Rank'])

    data3.to_csv('df_proce.csv')

df_proce(fname='df_conso.csv')
