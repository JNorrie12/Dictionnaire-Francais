#SQL wrapper for the dictionary



import psycopg2

from verbTools import *


class CSQLWrapper:

	instance = None


	def getInstance():
		if CSQLWrapper.instance == None:
			CSQLWrapper()
		return CSQLWrapper.instance

	def __init__(self, connected = False):
		if CSQLWrapper.instance != None:
			raise Exception("Class already created")
		else:
			CSQLWrapper.instance = self
			self.connected = connected	

	def connect(self, dbname, user, host, password, port):
		
		command = "dbname="+dbname+" user="+user+" host="+host +" password="+password+" port="+port +" connect_timeout=10"
		print(command)
		try:
			self.conn = psycopg2.connect(command)
			self.cur = self.conn.cursor()
			self.connected = True
		except:
			print("Cannot connect to database")	


	def addWord(self, word, wordType, meaning, **kwargs):
		if wordType == 'Verb':
			VerbConjugation(self.conn, self.cur, word, **kwargs)


	def searchWord():
		print("search word")




