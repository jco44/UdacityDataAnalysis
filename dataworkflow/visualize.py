import pandas as pd

def freq1_display(series):
    '''Displays freq tables for analyzing a categorical feature

    returns
    -----------
    1. Freq table w/ Counts
    2. Freq table w/ vals as a percent of total'''

    table = pd.crosstab(index=series,
                       columns='Count',
                       margins=True)

    print('\n-------------Counts------\n', table)
    print('\n--------%Total-----------\n',
         table/table.ix[:-1].sum())

def freq1_store(series):
    '''Creates freq tables for analyzing a categorical feature

    returns
    -----------
    list of 2 pandas DataFrames:
        pos0 = Freq table w/ Counts
        pos1 = Freq table w/ vals as a percent of total
    '''

    table = pd.crosstab(index=series,
                       columns='Count',
                       margins=True)

    return[table, table/table.ix[:-1].sum()]

def freq2_display(iSeries, cSeries):
    '''Displays freq tables and visualization for analyzing 2 categorical features

    params
    -------------
    iSeries: pandas series for use as row(index) & labels, dtype==Category
    cSeries: pandas series for use as column labels, dtype==Category

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

def freq2_store(iSeries, cSeries):
    '''Creates freq tables and visualization for analyzing 2 categorical features

    params
    -------------
    iSeries: pandas series for use as row(index) & labels, dtype==Category
    cSeries: pandas series for use as column labels, dtype==Category

    returns
    -----------
    List of 4 items:
        pos_0: 2-way freq table w/ counts
        pos_1: 2-way freq table w/ values as a percentage of row totals
        pos_2: 2-way freq table w/ values as a percentage of col totals
        pos_3: Table prepped for graph with counts from first table,
               must add .plot(kind='bar',stacked=True) for graph
    '''
    table = pd.crosstab(index=iSeries,
                       columns=cSeries,
                       margins=True)

    table.index = list(iSeries.cat.categories) + ['Totals']
    table.columns = list(cSeries.cat.categories) + ['RowTotals']
    iLen = len(table.index)


    return [table, table.div(table['RowTotals'], axis=0), table/table.ix['Totals'],
            table.ix[list(range(iLen-1)),table.columns[:-1]]]


def freq3_display(iSeries, cSeries1, cSeries2):
    '''Displays freq tables for analyzing 3 categorical features

    param
    ------------
    iSeries: pandas series for us as row(index) & labels, dtype==Category
    cSeries1: pandas series for first set of columns & labels, dtype==Category
    cSeries2: pandas series for 2nd set of columns & labels, dtype==Category

    returns
    ------------
    1: 3-way freq table w/ counts
    2: 3-way freq table w/ values as a percentage of col totals
    '''
    table = pd.crosstab(index=iSeries,
               columns=[cSeries1,
                       cSeries2],
               margins=True)

    print('\n------------Counts----------\n', table)
    print('\n-----------Col%--------------\n', table/table.ix['All'])

def freq3_store(iSeries, cSeries1, cSeries2):
    '''Creates freq tables for analyzing 3 categorical features

    param
    ------------
    iSeries: pandas series for us as row(index) & labels, dtype==Category
    cSeries1: pandas series for 1st set of columns & labels, dtype==Category
    cSeries2: pandas series for 2nd set of columns & labels, dtype==Category

    returns
    ------------
    List of 2 pandas DataFrames:
        pos_1 = 3-way freq table w/ counts
        pos_2 = 3-way freq table w/ values as a percentage of col totals
    '''
    table = pd.crosstab(index=iSeries,
               columns=[cSeries1,
                       cSeries2],
               margins=True)

    return [table, table/table.ix['All']]

def freq4_display(iSeries, cSeries1, cSeries2, cSeries3):
    '''Creates freq tables for analyzing 4 categorical features

       params
       ------------
       iSeries: pandas series for us as row(index) & labels, dtype==Category
       cSeries1: pandas series for 1st set of columns & labels, dtype==Category
       cSeries2: pandas series for 2nd set of columns & labels, dtype==Category
       cSeries2: pandas series for 3rd set of columns & labels, dtype==Category

       returns
       ------------
       1. 4-way freq table w/ counts
       2. 4-way freq table w/ values as a percentage of col totals

    '''
    data = pd.crosstab(index=iSeries,
                   columns=[cSeries1,
                           cSeries2,
                           cSeries3],
                   margins=True)

    print('\n----------Counts---------\n\n', data)
    print('\n---------------Col%----------\n', data/data.ix['All'])


def freq4_store(iSeries, cSeries1, cSeries2, cSeries3):
    '''Stores freq tables for analyzing 4 categorical features

       params
       ------------
       iSeries: pandas series for us as row(index) & labels, dtype==Category
       cSeries1: pandas series for 1st set of columns & labels, dtype==Category
       cSeries2: pandas series for 2nd set of columns & labels, dtype==Category
       cSeries2: pandas series for 3rd set of columns & labels, dtype==Category

       returns
       ------------
       List of 2 pandas DataFrames:
           pos_1 = 4-way freq table w/ counts
           pos_2 = 4-way freq table w/ values as a percentage of col totals

    '''
    data = pd.crosstab(index=iSeries,
                   columns=[cSeries1,
                           cSeries2,
                           cSeries3],
                   margins=True)

    return [data,data/data.ix['All']]


def ez_graph1(pclass):
    '''Display stacked bar graph of Male, Female, Total survival rates for specified class'''
    from matplotlib.pyplot import ylabel
    from dataworkflow.data import get_data
    #get data
    titanic = get_data()
    #create graph data
    data = freq3_store(titanic['Sex'],titanic['Pclass'], titanic['Survived'])[0][pclass]
    data['Totals'] = data.sum(axis=1)
    graph_data = data.div(data['Totals'], axis=0)
    #create graph & labels
    graph = (graph_data[['Died','Lived']]
            .plot(kind='bar', stacked=True, title='{} Class Survival Rates'.format(pclass))
            .legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            )
    ylabel("% of Total")

    return graph
