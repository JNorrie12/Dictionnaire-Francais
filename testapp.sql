SELECT verbTableRE('perdre');

insert into dictionary values (1, 'aller', 'verb', 'go to');


insert into verbEndings values ('present_RE', 's', 's', '', 'ons', 'ez', 'ent');
insert into verbEndings values ('present_ER', 'es', 'es', 'e', 'ons', 'ez', 'ent');
insert into verbEndings values ('present_IR', 'is', 'is', 'i', 'issons', 'issez', 'issent');

insert into verbEndings values ('future_RE', 'rai', 'ras', 'ra', 'rons', 'rez', 'ont');
insert into verbEndings values ('future_ER', 'erai', 'eras', 'era', 'erons', 'erez', 'eront');
insert into verbEndings values ('future_IR', 'irai', 'iras', 'ira', 'irons', 'irez', 'iront');

insert into verbEndings values ('perfect_RE', 'é', '', '', '', '', '');
insert into verbEndings values ('perfect_ER', 'ré', '', '', '', '', '');
insert into verbEndings values ('perfect_IR', 'i', '', '', '', '', '');
#Imperfect needs work as is based on3rd person participle
insert into verbEndings values ('imperfect_RE', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
insert into verbEndings values ('imperfect_ER', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
insert into verbEndings values ('imperfect_IR', 'issais', 'issais', 'issait', 'issions', 'issiez', 'issaient');

insert into verbEndings values ('conditional_RE', 'rais', 'rais', 'rait', 'rions', 'riez', 'raient');
insert into verbEndings values ('conditional_ER', 'erais', 'erais', 'erait', 'erions', 'eriez', 'eraient');
insert into verbEndings values ('conditional_IR', 'irais', 'irais', 'irait', 'irions', 'iriez', 'iraient');

SELECT tu
FROM verbEndings
WHERE id = 'present_IR'
