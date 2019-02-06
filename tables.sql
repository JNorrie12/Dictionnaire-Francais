/*ALL OF MY TABLE INITS*/


/*Dictionary- does what it says on the tin*/
CREATE TABLE dictionary(
	ID int,
	word char(20),
	word_type wt,
	def char(100),
	/*TODO DD RELATED WORDS NETWORK*/ 
	primary key (ID)
)


/*verbConjPresent- If the word is a Verb, show all conjugations*/
CREATE TABLE verbConjPresent (
	word char(20) UNIQUE,
	je char(20) ,
	tu char(20),
	il char(20),
	nous char(20),
	vous char(20),
	ils char(20),
	primary key (word)
)

CREATE TABLE verbEndings (
	tense_type char(20) UNIQUE,   /*of format "present_RE"*/
	je char(20) ,
	tu char(20),
	il char(20),
	nous char(20),
	vous char(20),
	ils char(20),
	primary key (tense_type)
)

