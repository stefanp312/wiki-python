import wikipedia
import string

#functions

def searchWikipedia(query):
    myReply = ", ".join(wikipedia.search(query, results=3))
    myReply = myReply + ". Type the name of the page you want to view."
    return myReply



#main code
search_term = raw_input("What would you like to search? ")

search_results = searchWikipedia(query=search_term)

print search_results

summary=""

while summary=="":	
	search_term = raw_input("Which page do you want? ")
	try:
		summary = wikipedia.summary(search_term , sentences = 2)
	except wikipedia.exceptions.DisambiguationError as e:
		print "That can refer to multiple things. Which did you mean? " + ", ".join(e.options)

print "Summary: " + summary

