__author__ = 'www.xavigimenez.net'


import re

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

NAME_COLUMN_NUMBER = 0
NAME_COLUMN_NAME = 'Name'
DESCRIPTION_COLUMN_NUMBER = 1
HOMEPAGE_COLUMN_NUMBER = 2
TAG_COLUMN_NUMBER = 12
TAG_COLUMN_NAME = 'keywords'
ACTIVITY_COLUMN_NUMBER = 13
ACTIVITY_COLUMN_NAME = 'Type of activity'
ID_COLUMN_NUMBER = 20
ID_COLUMN_NAME = 'Nid'
CONNECTIONS_COLUMN_NUMBER = 21
FOLDER_DATA_SOURCE = 'data-source/'
FOLDER_DATA_DEPLOY = 'data-deploy/'
FILE_MASTER = '00-csv-master.csv'
FILE_TAGS_CLEANED = '01-csv-tags-cleaned.csv'
FILE_TAGS_ADDED = '02-csv-tags-added.csv'
FILE_TAGS_ADDED_2 = '03-csv-tags-added-2.csv'
FILE_CONNECTIONS_ADDED = '04-csv-tags-connections.csv'
FILE_TAG_NETWORK = '05-network-tag.gdf'
FILE_NETWORK = '05-network.gdf'
THRESHOLD_TAGS_OCCURRENCES = 3