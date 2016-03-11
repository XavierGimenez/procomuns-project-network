__author__ = 'www.xavigimenez.net'

import constants as constants
from collections import Counter
import csv
from sets import Set





print 'Finding tags...'
#get a set of tags present in the data
tags = set()

with open(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAGS_CLEANED, 'w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter = ',')

    with open(constants.FOLDER_DATA_SOURCE + constants.FILE_MASTER, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')

        for row in csv_reader:

            #specific cases:
            # http://www.cyclestreets.net/photomap/ have its tags separated
            #by white spaced instead of commas
            if row[constants.HOMEPAGE_COLUMN_NUMBER] == 'http://www.cyclestreets.net/photomap/' or row[constants.HOMEPAGE_COLUMN_NUMBER] == 'http://freico.in/':
                row[constants.TAG_COLUMN_NUMBER].replace(' ', ',')

            #get list of tags
            tags_in_row = row[constants.TAG_COLUMN_NUMBER].lower().split(',')

            #remove leading and ending spaces and save to the set.
            #Also write the csv that tags as we are saving them into the set
            clean_tags = [tag.strip() for tag in tags_in_row if tag.strip() != '']
            tags |= set(clean_tags)

            row[constants.TAG_COLUMN_NUMBER] = ','.join(clean_tags)
            csv_writer.writerow(row)


print 'Tags found:'
#remove empty tag
#tags.remove('')
print tags





with open(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAGS_ADDED, 'w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter = ',')

    with open(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAGS_CLEANED, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')

        for row in csv_reader:

            #if the project has no tags, tried to extract them from the description
            if row[constants.TAG_COLUMN_NUMBER] == '':
                #print "[[[ " + row[0] + ' ]]] has no keywords'
                new_tags = []
                for tag in tags:
                    #if tag in row[DESCRIPTION_COLUMN_NUMBER]:
                    #this will find a sequence of characters, not the tag itself...
                    #this will lead to undesired matches
                    if constants.findWholeWord(tag)(row[constants.DESCRIPTION_COLUMN_NUMBER]) is not None:
                        #print (tag + " is a candidate")
                        new_tags.append(tag)
                #print 'Assigning tags to ' + row[0] + ": " + new_tags
                row[constants.TAG_COLUMN_NUMBER] = ','.join(new_tags)
            csv_writer.writerow(row)




#After checking which projects still have no tags, some of them have
#manually identified as candidates to have some tags collected from
#our initial search
with open(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAGS_ADDED_2, 'w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter = ',')

    with open(constants.FOLDER_DATA_DEPLOY + constants.FILE_TAGS_ADDED, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')

        for row in csv_reader:
            if row[constants.NAME_COLUMN_NUMBER] == 'Moovit':
                row[constants.TAG_COLUMN_NUMBER] = 'transport'
            if row[constants.NAME_COLUMN_NUMBER] == 'Wikihow':
                row[constants.TAG_COLUMN_NUMBER] = 'wiki'
            if row[constants.NAME_COLUMN_NUMBER] == 'Wikiprogress':
                row[constants.TAG_COLUMN_NUMBER] = 'open source'
            if row[constants.NAME_COLUMN_NUMBER] == 'Arduino':
                row[constants.TAG_COLUMN_NUMBER] = 'open source,arduino'
            if row[constants.NAME_COLUMN_NUMBER] == 'Safecast':
                row[constants.TAG_COLUMN_NUMBER] = 'open source,arduino'
            if row[constants.NAME_COLUMN_NUMBER] == 'Twine':
                row[constants.TAG_COLUMN_NUMBER] = 'open source'

            csv_writer.writerow(row)