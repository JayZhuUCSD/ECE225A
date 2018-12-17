def mp_gc(fname1='free-zipcode-database.csv',fname2='df_city.csv'):
    import pandas as pd

    df1 = pd.read_csv(fname1,dtype={'WorldRegion': str})
    df2 = df1[['City','State','Lat','Long']].copy()

    df2 = df2.loc[df2['State']=='CA']
    del df2['State']
    df2['City']=[x.title() for x in df2['City'].tolist()]
    # cl1=list(set(df2['City']))
    # df2 = df2.loc[df2['City'].isin(cl1)]
    a = df2['Lat'].tolist()
    b = df2['Long'].tolist()
    c = list(zip(a,b))
    df2['GC']=c
    df2.drop_duplicates(subset=['City'], keep='first')
    mp_dict = dict(zip(df2['City'], df2['GC']))
    mp_dict1 = dict(zip(df2['City'], df2['Lat']))
    mp_dict2 = dict(zip(df2['City'], df2['Long']))

    df3 = pd.read_csv(fname2, index_col=0)
    df3.set_index('Crime_PTP_Rank')
    del df3['Population']
    del df3['Total_Employees']
    del df3['Total_Officers']
    del df3['Total_Civilians']
    del df3['Total_Crime']
    del df3['Employees_PTP']
    del df3['Officers_PTP']
    del df3['Civilians_PTP']
    del df3['Crime_PTP_Rank']
    for index, row in df3.iterrows():
        if row['City'] in mp_dict1.keys():
            df3.loc[index, 'Lat'] = mp_dict1[row['City']]
            df3.loc[index, 'Long'] = mp_dict2[row['City']]
        else:
            df3.loc[index, 'Lat'] = None
            df3.loc[index, 'Long'] = None

    df3.to_csv('mp_gc.csv',index=False)

mp_gc(fname1='free-zipcode-database.csv',fname2='df_city.csv')
