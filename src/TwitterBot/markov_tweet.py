import numpy as np
import tweepy #update_status
import random

def generateWordDict(api):
    #Created a nested dictionary with the 1st Key = a word second key = possible words that come after and value = counter
    #Create a dictionary for every word encountered with the number of times that word occurs as its value
    with open("../../docs/markovChain.txt", 'r', encoding="utf-8") as f:
        #words_dic contains a dictionary with the following format
        #{word:{nextword:appearances, anotherwordthatcomesafter:appearances}}
        words_dic = {}
        words_occurences = {}
        words_list = []
        for line in f:
            line = line.replace("\n"," \n")
            words = line.split(" ")
            words_list.append(words)
            for index, word in enumerate(words):
                #Check if new word or not and add to occurences accordingly
                if (word in words_occurences):
                    words_occurences[word] += 1
                else:
                    words_occurences[word] = 1
                temp_kv_dic = {}
                #if we encounter a new line, move on to next line
                if word == "\n":
                    break
                #check if a word exists in the dictionary, if not intialize with the {currentword: {the next word:1}}
                elif word not in words_dic:
                    temp_kv_dic.update({words[index+1]:1})
                    words_dic.update({word:temp_kv_dic})
                #if word is in dictionary, check if the following word is a key, if not intialize it, if it is update value
                elif word in words_dic:
                    if words[index+1] in words_dic[word]:
                        words_dic[word][words[index+1]] += 1
                    else:
                        temp_kv_dic.update({words[index+1]:1})
                        words_dic[word].update(temp_kv_dic)
        #Normalize all potential next words so we can use the values as probabilities
        #The number of times we see a word is equal to the sum of all ooccurences of its next words
        #EG. "the fox is doing the dance" -> {the: {fox:1,dance:1},fox:{is:1},is:...}
            #We see "the" twice which is equal to [fox] + [dance] = 2
        for word in words_dic:
            for next_word in words_dic[word]:
                words_dic[word][next_word] = words_dic[word][next_word]/words_occurences[word]
    
    api.update_status(generateSentence(words_dic,words_list))
    
def generateSentence(words_dic, words_list):
    line = []
    while (len(line) <= 2):
        #Choose random line
        line = random.choice(words_list)
        #Take first word of that line
        start = line[0]
        #Get next word possibilities of word
        next_words = words_dic[start]
    sentence = start
    next_word = ""
    #End the line after \n is encountered
    while (next_word != '\n'):
        next_word = random.choice(list(next_words))
        if (next_word == '\n'):
            break
        next_words = words_dic[next_word]
        sentence = sentence + " " + next_word

    return sentence