
CREATE OR REPLACE FUNCTION changeEnding(Verb char(10), Ending char(4))
RETURNS char(20)
AS 
$body$
DECLARE  conjugation char(20);
DECLARE  step char(10);																   
DECLARE  l int;	
BEGIN 
	l = LENGTH(Verb);
	step = SUBSTRING(Verb, 1, l-2);
	conjugation = CONCAT(step, ending);
	RETURN conjugation;
END;
$body$											  
language plpgsql;

CREATE OR REPLACE FUNCTION verbConjugationGen(Verb(10))
RETURN int AS $$
DELCARE ending char(2);

DECLARE je char(20);
DECLARE	tu char(20);
DECLARE	il char(20);
DECLARE nous char(20);
DECLARE	vous char(20);
DECLARE	ils char(20);
BEGIN
		ending = SUBSTRING(Verb, 1, l-2);

		IF ending == 'ir' THEN
			/**/
		END IF;  
	IF ending == 'er' THEN
			/**/
		END IF;  
	IF ending == 're' THEN
			/**/
		END IF;  

END;
$$
/* 
CREATE OR REPLACE FUNCTION verbTableRE(Verb char(10))
RETURNS int									  
AS
$body$ 
DECLARE je char(20);
DECLARE	tu char(20);
DECLARE	il char(20);
DECLARE nous char(20);
DECLARE	vous char(20);
DECLARE	ils char(20);
BEGIN 
	je = changeEnding(Verb, 's'); 
	tu = changeEnding(Verb, 's');
	il = changeEnding(Verb, '');
	nous = changeEnding(Verb, 'ons');
	vous = changeEnding(Verb, 'ez');
	ils = changeEnding(Verb, 'ent');
	insert into verbConjPresent values (Verb, je, tu, il, nous, vous, ils);
	RETURN 0;
END;
$body$

CREATE OR REPLACE FUNCTION verbTableER(Verb char(10))
RETURNS int									  
AS
$body$ 
DECLARE je char(20);
DECLARE	tu char(20);
DECLARE	il char(20);
DECLARE nous char(20);
DECLARE	vous char(20);
DECLARE	ils char(20);
BEGIN 
	je = changeEnding(Verb, 'es'); 
	tu = changeEnding(Verb, 'es');
	il = changeEnding(Verb, '');
	nous = changeEnding(Verb, 'ons');
	vous = changeEnding(Verb, 'ez');
	ils = changeEnding(Verb, 'ent');
	insert into verbConjPresent values (Verb, je, tu, il, nous, vous, ils);
	RETURN 0;
END;
$body$

CREATE OR REPLACE FUNCTION verbTableIR(Verb char(10))
RETURNS int									  
AS
$body$ 
DECLARE je char(20);
DECLARE	tu char(20);
DECLARE	il char(20);
DECLARE nous char(20);
DECLARE	vous char(20);
DECLARE	ils char(20);
BEGIN 
	je = changeEnding(Verb, 'is'); 
	tu = changeEnding(Verb, 'is');
	il = changeEnding(Verb, '');
	nous = changeEnding(Verb, 'issons');
	vous = changeEnding(Verb, 'issez');
	ils = changeEnding(Verb, 'issent');
	insert into verbConjPresent values (Verb, je, tu, il, nous, vous, ils);
	RETURN 0;
END;
$body$
*/
CREATE OR REPLACE FUNCTION addWord(	ID int,	
									word char(20),	
									word_type wt,	
									def char(100))
RETURNS int	AS $$
BEGIN
	insert into dictionary values(ID, word,word_type, def);
	IF word_type=='verb' THEN
   	SELECT verbTableRE(word);
	END IF;										 
	RETURN 0;
END;
$$ LANGUAGE 'plpgsql'

