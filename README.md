# **TwitterBot**

## **About**
This is a twitterbot that posts on a user's account using random selection or markov chaining.

## **Requirements**
1. Must have a developer twitter account, and enter your consumer key and consumer secret key into the APIKEY.env file.

2. Must include either a "tweets.json" to perform random tweeting or "prunedLyrics.txt" to perform markov chaining

## **Usage**
### **Installation**
1. Download or clone the repo.

2. ```cd src/TwitterBot```

3. Open APIKEY.env and fill in your developer account information for twitter.

4. Option 1 or Option 2.

Option 1
To use random selection, copy a twitter .json file into the directory and rename it as randomSelection.json

Option 2
To use markov chaining, copy .txt file into the doc directory and rename it as markovChain.txt

5. To run the program use ```python3 main.py```
### **Example**

For example purposes, the repo comes with the required files, randomSelection.json and markovChain.txt

randomSelection.json is a random database containing tweets located on [twitter archive](archive.org)

markovChain.txt is a pruned lyrics textfile obtained using a [lyricsGenius API](https://github.com/johnwmillr/LyricsGenius) first, and then parsing the .json into a text file using dataparser.py provided

**NOTE**: *dataparser.py will only work on data extrapulated using the lyricsGenius API above.*



