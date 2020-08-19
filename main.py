#!/usr/bin/python3
import sys
from tool import remove_charset,get_query,get_knowledge,get_propositions

#check arguments
if len(sys.argv) != 2:
    print("Please only provide one file!")
    exit()

#read file into list of lines
rule_file = open(sys.argv[1], 'r')
lines = rule_file.readlines()
rule_file.close

for i in range(len(lines)):
    #remove newlines
    lines[i] = lines[i] [:len(lines[i]) - 1]
    #find comment and remove it
    comment_idx = lines[i].find('#')
    if comment_idx != -1:
        lines[i] = lines[i] [:comment_idx]
    #remove_whitespaces
    lines[i] = remove_charset(lines[i], " \t")
    print(lines[i])

#extract query
query = get_query(lines)

#extract knowledge
knowledge = get_knowledge(lines)

#get_propositions
