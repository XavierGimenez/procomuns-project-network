from constants import FILE_CONNECTIONS_ADDED

__author__ = 'www.xavigimenez.net'

from collections import Counter
import constants as constants
import pandas as pd


df = pd.read_csv(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAGS_ADDED_2)
df = df.fillna('')

for index, row in df.iterrows():
    #get list of tags of the inspected row. We look for these tags through the subset of data frame
    #not inspected yet when iterating the rows
    tags = row[constants.TAG_COLUMN_NUMBER].split(',')

    #get rows not being inspected yet
    df2 = df[index+1:]

    #list of possible connections
    connections = []

    for tag in tags:
        subset = df2[ df[constants.TAG_COLUMN_NAME].str.contains(tag, na = False) ]
        connections = connections + subset[constants.NAME_COLUMN_NAME].tolist()

    #remove duplicates and save ids as a string
    #df.loc[index, 'connections'] = ','.join([str(x) for x in list(set(connections))])

    #only those projects that share more than a certain number of tags will be
    #considered as connections.
    counter = Counter(connections)
    valid_connections = [key for key, count in counter.iteritems() if count >= constants.THRESHOLD_TAGS_OCCURRENCES]
    df.loc[index, 'connections'] = ','.join([str(x) for x in valid_connections])

df.to_csv(constants.FOLDER_DATA_DEPLOY + constants.FILE_CONNECTIONS_ADDED, sep=',', index=False)