import numpy
import json
import html

def main():
	uni_chars = ["\u2005","\u205f"]
	#Lyrics file from Genius.com
	with open("Lyrics_SelenaGomez.json", 'r', encoding='utf-8') as file:
		with open("prunedLyrics.txt", 'w', encoding='utf-8') as lyricsFile:
			json_data = json.load(file)
			for song in json_data['songs']:
				if song['lyrics'] is not None:
					for prunedLyrics in song['lyrics'].split('\n'):
						if prunedLyrics != "":
							if prunedLyrics[0].isalpha():
								if "lyrics" not in prunedLyrics.lower():
									for each in uni_chars:
										prunedLyrics = prunedLyrics.replace(each, " ")
									prunedLyrics = prunedLyrics.replace('(', "")
									prunedLyrics = prunedLyrics.replace(')', "")
									lyricsFile.write(html.unescape(prunedLyrics)+'\n')
	

main()
