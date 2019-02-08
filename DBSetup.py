from SQLWrapper import CSQLWrapper

tables = '''
DROP TABLE IF EXISTS dictionary;
CREATE TABLE dictionary(
	ID int,
	word char(20),
	word_type wt,
	def char(100),
	/*TODO DD RELATED WORDS NETWORK*/ 
	primary key (ID)
);


/*verbConjPresent- If the word is a Verb, show all conjugations*/
DROP TABLE IF EXISTS verbConj CASCADE;
CREATE  TABLE verbConj (
	word char(20) UNIQUE,
	je char(20) ,
	tu char(20),
	il char(20),
	nous char(20),
	vous char(20),
	ils char(20),
	primary key (word)
);

DROP TABLE IF EXISTS verbEndings;
CREATE TABLE verbEndings (
	tense_type char(20) UNIQUE,   /*of format "present_RE"*/
	je char(20) ,
	tu char(20),
	il char(20),
	nous char(20),
	vous char(20),
	ils char(20),
	primary key (tense_type)
);

DROP TABLE IF EXISTS verbConj_Present;
CREATE  TABLE verbConj_Present (
) INHERITS (verbConj);

DROP TABLE IF EXISTS verbConj_Future;
CREATE  TABLE verbConj_Future (
) INHERITS (verbConj);

DROP TABLE IF EXISTS verbConj_Perfect;
CREATE  TABLE verbConj_Perfect (
) INHERITS (verbConj);

DROP TABLE IF EXISTS verbConj_Imperfect;
CREATE  TABLE verbConj_Imperfect (
) INHERITS (verbConj);

DROP TABLE IF EXISTS verbConj_Conditional;
CREATE  TABLE verbConj_Conditional (
) INHERITS (verbConj);

'''

verbEndings = '''
INSERT INTO verbEndings
  ( tense_type, je, tu, il, nous, vous, ils )
VALUES
  ('imperfect_RE', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient'), 
  ('imperfect_ER', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient'), 
  ('imperfect_IR', 'issais', 'issais', 'issait', 'issions', 'issiez', 'issaient'),
  ('conditional_RE', 'rais', 'rais', 'rait', 'rions', 'riez', 'raient'),
  ('conditional_ER', 'erais', 'erais', 'erait', 'erions', 'eriez', 'eraient'),
  ('conditional_IR', 'irais', 'irais', 'irait', 'irions', 'iriez', 'iraient'),
  ('present_RE', 's', 's', '', 'ons', 'ez', 'ent'),
  ('present_ER', 'es', 'es', 'e', 'ons', 'ez', 'ent'),
  ('present_IR', 'is', 'is', 'i', 'issons', 'issez', 'issent'),
  ('future_RE', 'rai', 'ras', 'ra', 'rons', 'rez', 'ont'),
  ('future_ER', 'erai', 'eras', 'era', 'erons', 'erez', 'eront'),
  ('future_IR', 'irai', 'iras', 'ira', 'irons', 'irez', 'iront'),
  ('perfect_RE', 'e/', '', '', '', '', ''),
  ('perfect_ER', 're/', '', '', '', '', ''),
  ('perfect_IR', 'i', '', '', '', '', '');

'''

def main():
    SQLWrapper= CSQLWrapper()
    SQLWrapper.connect("Dictionary", "postgres", "localhost", "1234", "5433")
    SQLWrapper.cur.execute(tables)
    print "Tables reset"
    SQLWrapper.cur.execute(verbEndings)
    SQLWrapper.conn.commit()
    print "Verb Endings set"
    print "Done"




if __name__ == '__main__':
	main()

