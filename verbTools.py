
def rootVerbConjugation(conn, cur, root, verbType ,*tenses):
	verb = root + verbType.lower()
	if not tenses:
		tenses = "present", "future", "perfect", "imperfect", "conditional" #will add more 

	for tense in tenses:

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
			c.append((root) + i)

		print c
		#print "insert into verbConjPresent values ('"+ verb.ljust(20)+ "','"+c[0]+"','"+c[1]+"','"+c[2]+"','"+c[3]+"','"+c[4]+"','"+c[5] + "');"
		##cur.execute('''INSERT INTO verbConjPresent values ('{}','{}','{}','{}','{}','{}','{}')
		#				ON CONFLICT (word)
		#				DO 
		#				UPDATE	
		#				SET 
		#				je = '{}'
		#				WHERE verbConjPresent.word = {}'''.format(verb.ljust(20), c[0], c[1], c[2], c[3], c[4], c[5], c[0], verb.ljust(20),c[1], c[2], c[3], c[4], c[5]))
		#
		# 
		cur.execute("insert into verbConj_{} values ('{}','{}','{}','{}','{}','{}','{}');".format(tense, verb, *c))		
		conn.commit()	

def VerbConjugation(conn, cur, verb, **kwargs):
	#kwargs: 
	#future_root = 'future_root'
	#imperfect_root = 'imp_root'
	##Add subjunctive at some time.
	verbType = verb[-2:].upper()
	verbRoot = verb[:-2].lower()
	tenses = {"present", "future", "perfect", "imperfect", "conditional"} #will add more 

	#defaultVerbConjugation(conn, cur, verb)
	if kwargs is not None:
		if kwargs.get('fut_root'):
			rootVerbConjugation(conn, cur, kwargs['fut_root'], "RE" ,"future")
			tenses.remove("future")

		if kwargs.get('imp_root'):
			rootVerbConjugation(conn, cur, kwargs['imp_root'], "RE", "imperfect")
			tenses.remove("imperfect")

	rootVerbConjugation(conn, cur, verbRoot, verbType, *tenses)
