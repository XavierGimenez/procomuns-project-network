from igraph._igraph import InternalError

__author__ = 'xavi'

from collections import Counter
import constants
import igraph
import itertools
import pandas as pd
import pyUtils


class Project(object):
    def __init__(self, id, name, activity_type):
        self.id, self.name, self.activity_type = id, name, activity_type
        self.name = self.name.replace("'", "")
        self.name = self.name.replace(".", " ")

    def __hash__(self):
        return hash(self.name)


if __name__ == '__main__':

    df = pd.read_csv(constants.FOLDER_DATA_DEPLOY + constants.FILE_CONNECTIONS_ADDED, header = False)
    df = df.fillna('')

    #list of Projects objects
    projects = []

    #list collaborations (list of tuples)
    connections = []

    for index, row in df.iterrows():
        print 'project is ' + row[constants.NAME_COLUMN_NUMBER]
        projects.append(Project(row[constants.ID_COLUMN_NUMBER], row[constants.NAME_COLUMN_NUMBER], row[constants.ACTIVITY_COLUMN_NUMBER]))

        #split ids and clean null values
        if row[constants.CONNECTIONS_COLUMN_NUMBER] == '':
            continue

        connected = row[constants.CONNECTIONS_COLUMN_NUMBER].split(',')
        connected = [connexion for connexion in connected if connexion != '']
        connections.extend(list(itertools.product([row[constants.NAME_COLUMN_NUMBER]], connected)))
        print list(itertools.product([int(row[constants.ID_COLUMN_NUMBER])], connected))
        print ''

    #start creating the graph structure

    output_file = pyUtils.openFile(constants.FOLDER_DATA_DEPLOY + constants.FILE_NETWORK + "-tagthreshold-" + str(constants.THRESHOLD_TAGS_OCCURRENCES) + '.gdf')
    output_file.write("nodedef>name VARCHAR, activity VARCHAR\n")

    for project in projects:
        output_file.write('\'' + project.name + '\'' + ',' + '\'' + project.activity_type + '\'' + "\n")


    # print('edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE')
    output_file.write("edgedef>node1 INT,node2 INT\n")
    counter = Counter(connections)
    for key, count in counter.iteritems():
        output_file.write('\'' + key[0] + '\'' + ',' + '\'' + key[1] + '\'' + "\n")

    output_file.close()


'''
    #create the nodes. Each lab is a node
    graph = igraph.Graph()
    for idx, project in enumerate(projects):
        graph.add_vertex(project.id)

        graph.vs[len(graph.vs)-1]['label'] = project.id
        #replace " ' " character which breaks the creation of the node
        graph.vs[len(graph.vs)-1]['title'] = project.name
        print ('add node: ' + str(project.id) + project.name)

    #create the edges. Each connection is an edge. Attribute 'weight' will be the number of collaborations
    counter = Counter(connections)
    for key, count in counter.iteritems():
        try:
            graph.add_edge(key[0], key[1])
        except InternalError as e:
            print e

    #write the graph as an gml file
    graph.write_gml(constants.FOLDER_DATA_DEPLOY + constants.FILE_NETWORK)
'''
