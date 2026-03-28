CREATE TABLE profesor(
  profesorid VARCHAR(500) PRIMARY KEY,
  ime VARCHAR(100) NOT NULL,
  sredno_ime VARCHAR(100),
  prezime VARCHAR(100) NOT NULL,
  predmet VARCHAR(100) NOT NULL
  );
CREATE TABLE ucenik(
  ucenikid VARCHAR(500) PRIMARY KEY,
  ime VARCHAR(100) NOT NULL,
  sredno_ime VARCHAR(100),
  prezime VARCHAR(100) NOT NULL,
  godina_ili_oddelenie VARCHAR(100) NOT NULL
  );
CREATE TABLE predmet(
  predmetid VARCHAR(500) PRIMARY KEY,
  ime VARCHAR(100) NOT NULL,
  za_koe_oddelenie_ili_godina VARCHAR(100) NOT NULL,
  minimum_casa_vo_nedela INT(100) NOT NULL,
  profesorid VARCHAR(500) NOT NULL,
  ucenikid VARCHAR(500) NOT NULL,
  FOREIGN KEY (profesorid) REFERENCES
  profesor(profesorid),
  FOREIGN KEy (ucenikid) REFERENCES
  ucenik(ucenikid)
);
CREATE TABLE ocenka(
  ocenkaid VARCHAR(500) PRIMARY KEY,
  ocenka INT CHECK(ocenka>=1 AND ocenka<=5),
  datum DATE NOT NULL,
  profesorid VARCHAR(500) NOT NULL,
  predmetid VARCHAR(500) NOT NULL,
  ucenikid VARCHAR(500) NOT NULL,
  FOREIGN KEy (predmetid) REFERENCES
  predmet(predmetid),
  FOREIGN KEY (profesorid) REFERENCES
  profesor(profesorid),
  FOREIGN KEY (ucenikid) REFERENCES
  ucenik(ucenikid)
  );

INSERT INTO profesor (profesorid, ime, sredno_ime, prezime, predmet) VALUES
('P001', 'Петар', 'Николов', 'Петровски', 'Математика'),
('P002', 'Марија', 'Стефанова', 'Ангеловска', 'Програмирање'),
('P003', 'Игор', 'Ѓорѓиев', 'Стојанов', 'Физика');
INSERT INTO ucenik (ucenikid, ime, sredno_ime, prezime, godina_ili_oddelenie) VALUES
('U001', 'Марко', 'Зоран', 'Ристовски', 'III-4'),
('U002', 'Ана', 'Иван', 'Јовановска', 'III-4'),
('U003', 'Стефан', 'Драган', 'Костов', 'IV-2');
INSERT INTO predmet (predmetid, ime, za_koe_oddelenie_ili_godina, minimum_casa_vo_nedela, profesorid, ucenikid) VALUES
('PR01', 'Алгоритми', 'III-4', 4, 'P002', 'U001'),
('PR02', 'Алгоритми', 'III-4', 4, 'P002', 'U002'),
('PR03', 'Механика', 'IV-2', 3, 'P003', 'U002');
INSERT INTO ocenka (ocenkaid, ocenka, datum, profesorid, predmetid, ucenikid) VALUES
('O001', 5, '2026-03-20', 'P002', 'PR01', 'U001'),
('O002', 4, '2026-03-21', 'P002', 'PR02', 'U002'),
('O003', 3, '2026-03-22', 'P003', 'PR03', 'U003'),
('O004', 5, '2026-03-24', 'P002', 'PR01', 'U001');




--Прикажете ги сите ученици со нивните предмети.
SELECT ucenik.ime, predmet.ime
from ucenik
JOIN predmet ON ucenik.ucenikid=predmet.ucenikid;
--Прикажете ги сите оценки за еден конкретен ученик.
SELECT ucenik.ime, ocenka.ocenka
from ucenik
join ocenka ON ucenik.ucenikid=ocenka.ucenikid
ORDER BY ucenik.ime ASC;
--Пресметајте просечна оцена по предмет.
SELECT predmet.ime, AVG(ocenka.ocenka)
FROM predmet
JOIN ocenka ON predmet.predmetid = ocenka.predmetid
GROUP BY predmet.ime;
--Прикажете ги предметите со највисока просечна оцена.
SELECT predmet.ime, AVG(ocenka.ocenka)
FROM predmet
JOIN ocenka ON predmet.predmetid = ocenka.predmetid
GROUP BY predmet.ime
ORDER BY ocenka.ocenka DESC
LIMIT 1;
--Прикажете ги учениците со просек поголем од 4.0.
SELECT ucenik.ime, AVG(ocenka.ocenka)
FROM ucenik
JOIN ocenka ON ucenik.ucenikid = ocenka.ucenikid
GROUP BY ucenik.ucenikid
HAVING AVG(ocenka.ocenka) >= 4.0;
--Избројте колку ученици има секој наставник.
SELECT profesor.ime, profesor.prezime, COUNT(predmet.ucenikid)
FROM profesor
JOIN predmet ON profesor.profesorid = predmet.profesorid
GROUP BY profesor.profesorid;
--Прикажете ги учениците кои немаат ниту една оценка.
SELECT ucenik.ime, ocenka.ocenkaid
FROM ucenik
LEFT JOIN ocenka ON ucenik.ucenikid = ocenka.ucenikid
WHERE ocenka.ocenkaid IS NULL;
--Прикажете ги топ 3 ученици според просек.
SELECT ucenik.ime, AVG(ocenka.ocenka)
FROM ucenik
JOIN ocenka ON ucenik.ucenikid = ocenka.ucenikid
GROUP BY ucenik.ucenikid
ORDER BY AVG(ocenka.ocenka) desc
LIMIT 3;