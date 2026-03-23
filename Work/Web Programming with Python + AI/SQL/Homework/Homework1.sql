CREATE TABLE User (
     UserId INT PRIMARY KEY,
     Name VARCHAR(100) NOT NULL,
     Surname VARCHAR(100) NOT NULL,
     Email VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE Timeslot (
    TimeSlotID INT PRIMARY KEY,
    Dateandtime DATETIME NOT NULL UNIQUE,
    Hall INT NOT NULL UNIQUE,
    MovieID INT NOT NULL,
    MovieName VARCHAR(100) NOT NULL,
    FOREIGN KEY (MovieID, MovieName) REFERENCES Movie(MovieID, MovieName)
);

CREATE TABLE Movie (
    MovieID INT PRIMARY KEY,
    MovieName VARCHAR(100) NOT NULL,
    Genre VARCHAR(100) NOT NULL,
    AgeRating VARCHAR(100) NOT NULL,
    Price INT NOT NULL
);

CREATE TABLE Sale (
    SaleID INT PRIMARY KEY,
    Dateandtime DATETIME NOT NULL,
    NumberOfTickets INT NOT NULL,
    TimeslotBoughtID INT NOT NULL,
    UserSoldToID INT NOT NULL,
    MoneySpent INT NOT NULL,
    FOREIGN KEY (TimeSlotBoughtID) REFERENCES Timeslot(TimeSlotID),
    FOREIGN KEY (UserSoldToID) REFERENCES User(UserID)
);

SELECT MovieName from Movie;
SELECT MovieName from Movie where Price >= 300;
SELECT MovieName from Movie where MovieName LIKE '%A%';
SELECT MovieName from Movie where MovieName LIKE '%Bad%';
SELECT MovieName from Movie order by Price;
SELECT MovieName, Hall, Dateandtime from Timeslot where Dateandtime > '2026-3-25 12:30:00';
SELECT * from User where Surname = 'Nestorovski';
SELECT * from Sale where Dateandtime > '2026-3-25 12:30:00';
SELECT * from Sale order by Dateandtime DESC;
SELECT * from Sale where NumberOfTickets > 5;
SELECT * from User order by Surname;
