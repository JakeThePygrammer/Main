CREATE TABLE Profesor (
    ProfesorID INT PRIMARY KEY,
      Ime VARCHAR(50) NOT NULL,
      Prezime VARCHAR(50) not NULL,
      Email VARCHAR(70) NOT NULL
);


CREATE TABLE Student (
  StudentID INT PRIMARY KEY,
  Ime VARCHAR(50) NOT NULL,
  Prezime VARCHAR(50) NOT NULL,
  Indeks VARCHAR(20) UNIQUE,
  Godini INT CHECK (Godini >= 18),
  Email VARCHAR(100) DEFAULT 'nema@email.com'
);

CREATE TABLE Kurs (
   KursID INT PRIMARY KEY,
   ImeNaKurs VARCHAR(100) NOT NULL,
   Krediti INT CHECK (Krediti > 0),
   ProfesorID INT,
   FOREIGN KEY (ProfesorID) REFERENCES Profesor(ProfesorID)
);

INSERT INTO Profesor (profesorid, ime, prezime, email) VALUES
('23','Jovan','Stamatovski','jovanstamatovski@ukim.edu.mk'),
('46','Jana','Amarilova','janaaa___@ukim.edu.mk'),
('38','Gorazd','Andreevski','andreevskigorazd276@ukim.edu.mk'),
('12','Simon','Arangelov','simon.arangelov@ukim.edu.mk'),
('63','Bujar','Gashi','bujargashi@ukim.edu.mk');

INSERT INTO Kurs (kursid, imenakurs, krediti, profesorid) VALUES
('26', 'Opst marketing', '5', '23'),
('65', 'Statistika', '4', '46'),
('75', 'Bolesti od vid virusi', '2', '38'),
('21', 'Programirange vo C++/C', '6', '12'),
('77', 'Detska psihologija', '3', '63');

INSERT INTO Student (studentid, ime, prezime, indeks, godini, email) VALUES
('251','Petar','Ivanovic','531161','20','petar.ivanovic@student.edu.mk'),
('151','Ana','Bicevska','762166','22','bicevskaana512@student.edu.mk'),
('765','Marija','Radosavjev','987615','25','radimare@student.edu.mk'),
('762','Aleksandar','Dimovski','215646','19','dimceac@student.edu.mk'),
('654','Stefan','Bijovski','765211','21','stefcebice@student.edu.mk');

SELECT ime, indeks FROM Student;
SELECT * FROM Student WHERE godini > 20;
SELECT * FROM Student where ime = 'Stefan';
SELECT * FROM Student WHERE ime = 'Ana' OR ime = 'Marija';
SELECT * from Student where ime = 'Marija' and godini > 19;