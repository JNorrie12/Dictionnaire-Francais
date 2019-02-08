from SQLWrapper import *
from verbTools import VerbConjugation

#Test app showing the the usability 
def main():
	#Set UP SQL class
	SQLWrapper= CSQLWrapper()
	SQLWrapper.connect("Dictionary", "postgres", "localhost", "1234", "5433")
	
	#~~Verbs~~
	SQLWrapper.addWord("perdre", "Verb", "to lose")
	print "perdre added"
	#~~Irregualr Verb~~
	SQLWrapper.addWord("aller", "Verb", "to go", fut_root = "i")
	print "aller added"



if __name__ == '__main__':
	main()

