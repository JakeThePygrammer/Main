CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Ime VARCHAR(50),
    Prezime VARCHAR(50),
    Grad VARCHAR(50)
);

CREATE TABLE Kurs (
    KursID INT PRIMARY KEY,
    ImeNaKurs VARCHAR(100),
    ProfesorID INT
);

CREATE TABLE Upisi (
    UpisID INT PRIMARY KEY,
    StudentID INT,
    KursID INT,
    Ocenka INT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (KursID) REFERENCES Kurs(KursID)
);



INSERT INTO Student (StudentID, Ime, Prezime, Grad) VALUES
(1, 'Ана', 'Петрова', 'Skopje'),
(2, 'Марко', 'Илиев', 'Bitola'),
(3, 'Јана', 'Стојанова', 'Skopje'),
(4, 'Петар', 'Наумов', 'Ohrid'),
(5, 'Тамара', 'Крстева', 'Tetovo');

INSERT INTO Kurs (KursID, ImeNaKurs, ProfesorID) VALUES
(5, 'Бази на податоци', 4),
(7, 'Програмирање', 5);

INSERT INTO Upisi (UpisID, StudentID, KursID, Ocenka) VALUES
(10, 1, 5, 8),
(11, 2, 7, 7),
(12, 1, 7, 10),
(13, 3, 5, 6),
(14, 5, 5, 9);

SELECT  s.Ime, s.Prezime, s.Grad, u.KursID, u.Ocenka
FROM Student s
JOIN Upisi u ON s.StudentID = u.StudentID
WHERE u.Ocenka <= 8;

SELECT  s.Ime, s.Prezime, s.Grad, u.KursID, u.Ocenka
FROM Student s
JOIN Upisi u ON s.StudentID = u.StudentID
WHERE u.Ocenka BETWEEN 7 and 9;

SELECT   s.Ime, s.Prezime, s.Grad, k.ImeNaKurs, u.Ocenka
FROM Student s
JOIN Upisi u ON s.StudentID = u.StudentID
JOIN Kurs k ON u.KursID = k.KursID
WHERE k.ProfesorID = 4;

SELECT  s.Ime, s.Prezime, s.Grad, u.KursID, u.Ocenka
FROM Student s
JOIN Upisi u ON s.StudentID = u.StudentID
WHERE u.Ocenka >= 8 and s.Grad != 'Skopje';

SELECT   s.Ime, s.Prezime, s.Grad, k.ImeNaKurs, u.Ocenka
FROM Student s
JOIN Upisi u ON s.StudentID = u.StudentID
JOIN Kurs k ON u.KursID = k.KursID
ORDER BY u.Ocenka desc;