#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 10:02:05 2025

@author: chasecantrell
"""

# File: uniqueWords.py
# 
# Purpose: Opens a file whose contents will be read in
#          and printed.  Extract all of the words from 
#          the text to create a list and print it.  A
#          set is created from this list to obtain all
#          of the unique words and print them out each
#          per line.
#
# Programmer: 

def main():
    # hard code the name of the file for an
    # academic example
    fileInput = "myWords.txt"
    # read in the entire and then print it
    inputFile = open(fileInput, 'r')
    text = inputFile.read()
    
    #print(text, "\n")
    
    # close the file
    inputFile.close()
    # extract out all of the words of the words that
    # were read in and print them out
    allWords = text.split()
    print('All of the words:\n', allWords, '\n')
    
    totalWords = len(allWords)
    print('There are', totalWords, "Words that were read in from the file.")
    # using a set, obtain all the unique words
    # that were read in from the file
    uniqueWords = set(allWords)
    num = len(uniqueWords)
    
    for word in uniqueWords:
        print(word)
        
        
    print('\nThere were', num, "Unique words out of a total of", totalWords, "words.")
    # call function goodBye() to end program       
    goodbye()
# end function main

# end function goodBye
def goodbye():
    print('\nThis program was written by chase')
    print('end of program')
# invoke/call the function main()
main()