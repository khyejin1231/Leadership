# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:48:09 2021

@author: USER
"""

from pybliometrics.scopus import ScopusSearch
import pandas as pd

# Scopus search
search_result = ScopusSearch("(TITLE-ABS-KEY(Corporate social responsibility) \
                             AND TITLE-ABS-KEY(strategic leadership)) \
                                 OR (TITLE-ABS-KEY(organizational learning)\
                                     AND TITLE-ABS-KEY(Corporate social responsibility))\
                                    OR (TITLE-ABS-KEY(Corporate social responsibility)\
                                      AND TITLE-ABS-KEY(dynamic environment))")
    

print("Documents found:", search_result.get_results_size())

data = pd.DataFrame(search_result.results)

#Conference Paper, Book and Article
df = data.loc[data['subtypeDescription'].isin(['Article'])]

#Date
data.coverDate = pd.to_datetime(data.coverDate)
df = df[df['coverDate']>="2000-01-01"]

#Journals
'''
df = df.loc[df['publicationName'].isin(['Academy of Management Journal','Academy of Management Review',\
    'Accounting, Organizations and Society', 'Administrative Science Quarterly','Entreprenership Theory and Practice',\
        'Harvard Business Review','Human Relations','Human Resource Management',\
     'Journal of Applied Psychology','Journal of Business Ethics',\
    'Journal of International Business Studies','Journal of Management','Jornal of Management Information Systems',\
   'Journal of Management Studies' 'Journal of Political Economy','Management Science',\
       'MIS Quarterly','Organization Studies','Organizational Behavior and Human Decision Processes',\
          'Research Policy','Sloan Management Review','Strategic Entrepreneurship Journal','Strateigic Management Journal'])]
'''


#Citation
df['citedby_count'] = pd.to_numeric(df['citedby_count'])

#Keep only those articles with at least one citation OR published after 2020-01-01
df = df[(df['citedby_count']>10) | (df['coverDate'] > "2021-01-01")]

df.to_excel(r'C:\Users\USER\Documents\Python\Leadership\leadership.xlsx', index = False)


