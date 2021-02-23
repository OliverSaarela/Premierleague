import os
import pandas as pd
import re
import numpy as np
from datetime import date



def main():

    #os.system("cd plstats")
    #os.system("scrapy crawl alltime")
    #os.system("cd ..")

    data = pd.read_json(r'plstats/alltime.json')

    ## Having stat names in a list while manually adding 'Team'
    ## and automatically adding every other name of data
    ## E.G. Matches_played, Wins, Losses, ...
    ## Formating all text to be readable
    data_names = ['Team']
    for i in data['names'][0]:
        names = re.findall(r'\w+', i)
        names = '_'.join(names)
        if len(names) > 0 and names not in ['Attack', 'Team_Play', 'Defence', 'Discipline']:# Manually removing stat categories
            data_names.append(names)

    ## Taking all the data that matches the stat names
    ## and combining each teams list of data
    ## to a list (Lists inside a list)
    ## Also formating all text to be readable
    data_list = []
    for team in range(len(data)):
        team_data = []
        team_data.append(data['team'][team])
        for j in data['values'][team]:
            value = re.findall(r'\w+.+', j)
            value = ''.join(value)
            value = value.replace(',', '')
            if re.search(r'%$', value):
                value = float(value.strip('%')) / 100


            team_data.append(value)
        data_list.append(team_data)

    ## Truning the data into a pandas dataframe and filling empty slots
    ## also removing duplicated columns
    ## and saving it as a csv
    alldata_df = pd.DataFrame(np.array(data_list), columns=data_names)
    alldata_df.replace(to_replace='', value=0, inplace=True)
    alldata_df = alldata_df.loc[:,~alldata_df.columns.duplicated()]
    for column in alldata_df.columns:
        if not re.search(r'[a-zA-Z]|%$', alldata_df[column][0]):
            alldata_df[column] = pd.to_numeric(alldata_df[column])
    today = date.today()
    alldata_df.to_csv(path_or_buf='./Data/' + str(today) +'_team_data.csv', index=False)

if __name__ == '__main__':
    main()