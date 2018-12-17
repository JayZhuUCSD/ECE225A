def dt_extr(fname='df_city.csv'):
    import pandas as pd
    data4 = pd.read_csv(fname, index_col=0)

    data4 = data4.loc[data4['Crime_PTP_Rank'].isin(range(217))]
    data4.set_index('Crime_PTP_Rank')
    del data4['City']
    del data4['Population']
    del data4['Total_Officers']
    del data4['Total_Civilians']
    del data4['Employees_PTP']
    del data4['Officers_PTP']
    del data4['Civilians_PTP']
    del data4['Crime_PTP']
    del data4['Crime_PTP_Rank']
    # data4.rename(columns={"Total_Employees": "x", "Total_Crime": "y"}, inplace=True)

    data4.to_csv('dt_extr.csv',index=False)

dt_extr(fname='df_city.csv')
