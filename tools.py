

def defaultVerbConjugation(conn, cur, verb):
	
	verbType = verb[-2:].upper()
	tenses = {"present"}#, "future", "perfect", "imperfect", "conditional"} #will add more 

	for tense in tenses:
		key = "'" + tense + "_" + verbType + "'" 

		cur.execute("SELECT * FROM verbendings WHERE tense_type="+key+";")

		endings = cur.fetchall()

		print(len(endings))
		if len(endings) == 0:
			print "ERROR: Verb conjugation enrty: ", key, " does not exist" 
			break
		elif len(endings) > 1:
			print "WARNING: Multiple versions of ", key, "Taking first"


		c = []
		
		for i in endings[0][1:]:
			c.append((verb[0:-2] + i).ljust(20))
		
#		print 'insert into verbConjPresent values ('+ verb.ljust(20)+ ','+c[0]+','+c[1]+','+c[2]+','+c[3]+','+c[4]+','+c[5] + ');'


		print "insert into verbConjPresent values ('"+ verb.ljust(20)+ "','"+c[0]+"','"+c[1]+"','"+c[2]+"','"+c[3]+"','"+c[4]+"','"+c[5] + "');"
		cur.execute("INSERT INTO verbConjPresent values ('"+ verb.ljust(20)+ "','"+c[0]+"','"+c[1]+"','"+c[2]+"','"+c[3]+"','"+c[4]+"','"+c[5] + "');")
#		cur.fetchall()		
		conn.commit()

def rootVerbConjugation(conn, cur, root, type,*tenses):

	if not tenses:
		tenses = "present", "future", "perfect", "imperfect", "conditional" #will add more 
	print tenses
	for i in tenses:
		print tenses
		key = "'" + tense + "_" + verbType + "'" 

		cur.execute("SELECT * FROM verbendings WHERE tense_type="+key+";")

		endings = cur.fetchall()

		if len(endings) == 0:
			print "ERROR: Verb conjugation enrty: ", key, " does not exist" 
			break
		elif len(endings) > 1:
			print "WARNING: Multiple versions of ", key, "Taking first"


		c = []
		
		for i in endings[0][1:]:
			c.append((root).ljust(20))
		
#		print 'insert into verbConjPresent values ('+ verb.ljust(20)+ ','+c[0]+','+c[1]+','+c[2]+','+c[3]+','+c[4]+','+c[5] + ');'


		print "insert into verbConjPresent values ('"+ verb.ljust(20)+ "','"+c[0]+"','"+c[1]+"','"+c[2]+"','"+c[3]+"','"+c[4]+"','"+c[5] + "');"
		cur.execute("INSERT INTO verbConjPresent values ('"+ verb.ljust(20)+ "','"+c[0]+"','"+c[1]+"','"+c[2]+"','"+c[3]+"','"+c[4]+"','"+c[5] + "');")
#		cur.fetchall()		
		conn.commit()	

def VerbConjugation(conn, cur, verb, **kwargs):
	#future_root = 'future_root'
	#imperfect_root = 'third_pers'
	#subjunctif_root = 'sub_root'
	verbType = verb[-2:].upper()
	verbRoot = verb[:-2].lower()
	Itenses = {"present", "future", "perfect", "imperfect", "conditional"} #will add more 

	#defaultVerbConjugation(conn, cur, verb)
	if kwargs is not None:
		if kwargs.get('fut_root'):
			print('things')
			rootVerbConjugation(conn, cur, kwargs['fut_root'], verbType, "future")
			del tenses["future"]
			#DO stuff
		if kwargs.get('imp_root'):
			print('things')
			rootVerbConjugation(conn, cur, kwargs['imp_root'], verbType, "imperfect")
			del tenses["imperfect"]

	rootVerbConjugation(conn, cur, verbRoot, verbType, tenses)
			#Do stuff
	'''	if kwargs.get('sub_root'):
						rootVerbConjugation(conn, cur, kwargs['sub_root'], verbType, "subjunctive")
			del tense[""]
			print('things')
			#Do stuff'''

