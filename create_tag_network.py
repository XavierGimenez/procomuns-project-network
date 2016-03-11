__author__ = 'xavi'


from collections import Counter
import constants as constants
import itertools
import pandas as pd
import pyUtils

df = pd.read_csv(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAGS_ADDED_2)
df = df.fillna('')

set_tags = set()

#list of possible connections between topics
connections = []

for index, row in df.iterrows():
    #get list of tags of the inspected row. We look for these tags through the subset of data frame
    #not inspected yet when iterating the rows
    tags = row[constants.TAG_COLUMN_NUMBER].split(',')

    set_tags |= set(tags)

    #get rows not being inspected yet
    df2 = df[index+1:]



    for index2, row2 in df2.iterrows():
        tags2 = row2[constants.TAG_COLUMN_NUMBER].split(',')
        connections = connections + list(itertools.combinations(sorted(tags + tags2), 2) )

#start creating the graph structure
output_file = pyUtils.openFile(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAG_NETWORK)
output_file.write("nodedef>name INT, name VARCHAR, activity VARCHAR\n")

for tag in set_tags:
    output_file.write('\'' + tag + '\'' + "\n")


# print('edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE')
output_file.write("edgedef>node1 INT,node2 INT, weight DOUBLE\n")
counter = Counter(connections)
for key, count in counter.iteritems():
    output_file.write('\'' + key[0] + '\'' + ',' + '\'' + key[1] + '\'' + ',' + str(count) + "\n")

output_file.close()