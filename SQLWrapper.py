#SQL wrapper for the dictionary



import psycopg2

from tools import *


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
		self.conn = psycopg2.connect(command)
		self.cur = self.conn.cursor()
		self.connected = True
		#except:
		#	print("Cannot connect to database")


	def addWord():
		print("add word")

	def searchWord():
		print("search word")



def main():
	SQLWrapper= CSQLWrapper();
	#SQLWrapper.getInstance()
	SQLWrapper.connect("Dictionary", "postgres", "localhost", "1234", "5433")
	SQLWrapper.cur.execute("""SELECT * FROM verbendings""")
	
	rows = SQLWrapper.cur.fetchall()
	
	for row in rows:
		print(row[1])

	VerbConjugation(SQLWrapper.conn, SQLWrapper.cur, 'perdre')
	
	#SQLWrapper.conn.commit()

if __name__ == '__main__':
	main()





