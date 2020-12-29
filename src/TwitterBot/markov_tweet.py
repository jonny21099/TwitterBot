def markov_tweet():
    #Created a nested dictionary with the 1st Key = a word second key = possible words that come after and value = counter
    words_dic = {}
    #Create a dictionary for every word encountered with the number of times that word occurs as its value
    words_occurences = {}
    with open("prunedLyrics.txt", 'r', encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n"," \n")
            words_list = line.split(" ")
            for index, word in enumerate(words_list):
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
                    temp_kv_dic.update({words_list[index+1]:1})
                    words_dic.update({word:temp_kv_dic})
                #if word is in dictionary, check if the following word is a key, if not intialize it, if it is update value
                elif word in words_dic:
                    if words_list[index+1] in words_dic[word]:
                        words_dic[word][words_list[index+1]] += 1
                    else:
                        temp_kv_dic.update({words_list[index+1]:1})
                        words_dic[word].update(temp_kv_dic)
    #Normalize all potential next words so we can use the values as probabilities
    #The number of times we see a word is equal to the sum of all ooccurences of its next words
    #EG. "the fox is doing the dance" -> {the: {fox:1,dance:1},fox:{is:1},is:...}
        #We see "the" twice which is equal to [fox] + [dance] = 2
    for word in words_dic:
        for next_word in words_dic[word]:
            words_dic[word][next_word] = words_dic[word][next_word]/words_occurences[word]
    return(words_dic)

"""
Maybe we can split markov_tweet into multiple functions
"""
# def occurences():
#     with open("prunedLyrics.txt", 'r', encoding="utf-8") as f:
#         words_occurences = {}
#         for line in f:
#             line = line.replace("\n"," \n")
#             for word in line.split(" "):
#                 if (word in words_occurences):
#                     words_occurences[word] += 1
#                 else:
#                     words_occurences[word] = 1
#     return words_occurences

#words_dic contains a dictionary with the following format
#{word:{nextword:appearances, anotherwordthatcomesafter:appearances}}
words_dict = markov_tweet()


