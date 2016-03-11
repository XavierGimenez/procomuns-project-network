#!/bin/bash

# if deploy data folder exists
#if [ -d "./data-deploy/" ]; then
 #remove existing deploy data folder
# echo "Delete data folder..."
# rm -rf ./data-deploy/*
#fi

#save excel file to tsv files. One tsv file for each worksheet
echo ""
echo "-------------------"
echo "[get_original_tags.py]"
echo "Get original tags from the original data source. For those projects without tags, find existing tags into its description in order to assign tags to the project"
python get_original_tags.py

echo ""
echo "-------------------"
echo "[set_links.py]"
echo "For each project, find other project that share tags."
python set_links.py

echo ""
echo "-------------------"
echo "[create_network.py]"
echo "Generate a gdf file based on the connections of each project."
python create_network.py