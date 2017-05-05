from dataworkflow.data import get_data
import pandas as pd

def test_data():

    data = get_data()

    assert all(data.columns == ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',
       'Embarked', 'FamilyTot', 'FamStatus', 'age_group'])

    assert all([len(data[col]) == 891
                for col in ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Fare', 'FamilyTot', 'FamStatus']])

    assert all([str(data[col].dtype) == 'category'
                for col in ['Survived', 'Pclass', 'Sex','Embarked','FamStatus', 'age_group']])
