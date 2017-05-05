import pandas as pd

def freq1(series):
    '''Creates freq tables for analyzing a categorical feature

    returns
    -----------
    1. Freq table w/ Counts
    2. Freq table w/ vals as a percent of total'''

    table = pd.crosstab(index=series,
                       columns='Count',
                       margins=True)

    print('\n-------------Counts------\n', table)
    print('\n--------%Total-----------\n',
         table/table.sum())


def freq2(iSeries, cSeries):
    '''Creates freq tables and visualization for analyzing 2 categorical features

    params
    -------------
    iSeries: pandas series for use as row(index) & labels, dtype==Category
    :param cSeries: pandas series for use as column labels, dtype==Category

    returns
    -----------
    1: 2-way freq table w/ counts
    2: 2-way freq table w/ values as a percentage of row totals
    3: 2-way freq table w/ values as a percentage of col totals
    4: Stacked bar graph of counts from first table
    '''
    table = pd.crosstab(index=iSeries,
                       columns=cSeries,
                       margins=True)

    table.index = list(iSeries.cat.categories) + ['ColTotals']
    table.columns = list(cSeries.cat.categories) + ['RowTotals']
    iLen = len(table.index)

    #freq tables
    print('\n-------Counts-------\n', table)
    print('\n-------Row%--------\n',
         table.div(table['RowTotals'], axis=0))
    print('\n-------Col%---------\n\n',
         table/table.ix['ColTotals'])

    #bar graph
    print('\n------Stacked Bar Graph------\n',
         table.ix[list(range(iLen-1)),
                 table.columns[:-1]].plot(kind='bar',stacked=True))

def freq3(iSeries, cSeries1, cSeries2):
    '''Creates freq tables for analyzing 3 categorical features

    param
    ------------
    iSeries: pandas series for us as row(index) & labels, dtype==Category
    cSeries1: pandas series for first set of columns & labels, dtype==Category
    cSeries2: pandas series for 2nd set of columns & labels, dtype==Category

    returns
    ------------
    1: 3-way freq table w/ counts
    2: 3-way freq table w/ values as a percentage of row totals
    '''

    table = pd.crosstab(index=iSeries,
               columns=[cSeries1,
                       cSeries2],
               margins=True)

    print('\n------------Counts----------\n', table)
    print('\n-----------Col%--------------\n', table/table.ix['All'])
