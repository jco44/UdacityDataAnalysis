import os
from urllib.request import urlretrieve

import numpy as np
import pandas as pd

URL = 'https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57e9a84c_titanic-data/titanic-data.csv'

def get_data(filename='train.csv', url=URL, force_download=False):
    '''Download and cache the titanic data

    Params
    ---------------
    filename : string (optional)
        location to save data
    url : string (optional)
        web location of data
    force_download : bool (optional)
        if True, force redownload of data

    Returns
    ----------
    data : pandas.DataFrame
        Titanic passanger data
    '''
    if force_download or not os.path.exists(filename):
        urlretrieve(filename,url)

    data = pd.read_csv(filename, dtype={'Sex':'category',
                                       'Embarked':'category'})

    #replace existing data with categorical data
    new_survived = pd.Categorical(data['Survived'])
    new_survived = new_survived.rename_categories(['Died', 'Lived'])
    data['Survived'] = new_survived

    new_pclass = pd.Categorical(data['Pclass'], ordered=True)
    new_pclass = new_pclass.rename_categories(['1st','2nd','3rd'])
    data['Pclass'] = new_pclass

    #Add new variables
    data['FamilyTot'] = data['SibSp'] + data['Parch'] #FamilyTot

    bins = [-1, 0, np.inf] #FamStatus
    labels = ['Single', 'Family']
    fam_status = pd.cut(data['FamilyTot'], bins, labels=labels)
    data['FamStatus'] = fam_status

    bins = [0,17,1000, np.inf] #age_group
    labels = ['Child', 'Adult', 'Unknown']
    age_groups = pd.cut(data['Age'], bins, labels=labels)
    data['age_group'] = age_groups

    #remove uneccesary variables
    data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

    #ASK WHY CODE BELOW TO UPDATE DTYPES CAUSED ERROR IN JUPYTER:
    #TypeError: __init__() got an unexpected keyword argument 'dtype'

    #Correct dtypes
    #data['Sex'] = pd.Series(data['Sex'], dtype='category')
    #data['Embarked'] = pd.Series(data['Embarked'], dytpe ='category')

    return data
