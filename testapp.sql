SELECT verbTableRE('perdre');

insert into dictionary values (1, 'aller', 'verb', 'go to');


insert into verbEndings values ('present_RE', 's', 's', '', 'ons', 'ez', 'ent');
insert into verbEndings values ('present_ER', 'es', 'es', 'e', 'ons', 'ez', 'ent');
insert into verbEndings values ('present_IR', 'is', 'is', 'i', 'issons', 'issez', 'issent');

SELECT tu
FROM verbEndings
WHERE id = 'present_IR'