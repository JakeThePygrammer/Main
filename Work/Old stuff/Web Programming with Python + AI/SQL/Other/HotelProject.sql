CREATE TABLE User(
    userid INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Reservation (
    reservationid INT PRIMARY KEY,
    dateandtimestart DATETIME NOT NULL,
    dateandtimeend DATETIME NOT NULL,
    userid INT NOT NULL,
    roomid INT NOT NULL,
    price INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES User(userid),
    FOREIGN KEY (roomid) REFERENCES Room(roomid)
);

CREATE TABLE Room (
    roomid INT PRIMARY KEY,
    roomtype VARCHAR(100) NOT NULL
);

INSERT INTO User (userid, name, surname, mail) VALUES
    (1, 'Jonas', 'Ramirez', 'jonas.ramirez@gmail.com'),
    (2, 'Maria', 'Miller', 'MariaMiller321@outlook.com'),
    (3, 'Cortana', 'Simmons', 'alexiscortana@business.com'),
    (4, 'Phillip', 'Smith', 'phillipsmith@yahoo.com');

INSERT INTO Reservation (reservationid, dateandtimestart, dateandtimeend, userid, roomid, price) VALUES
    (1, '2026-03-29 10:00:00', '2026-03-31 12:00:00', 1, 103, 85),
    (2, '2026-03-31 14:30:00', '2026-04-02 16:00:00', 2, 104, 120),
    (3, '2026-04-01 09:00:00', '2026-04-03 11:00:00', 4, 105, 160),
    (4, '2026-04-10 18:00:00', '2026-04-15 21:00:00', 4, 102, 50),
    (5, '2026-04-18 09:00:00', '2026-04-23 15:00:00', 1, 101, 50),
    (6, '2026-04-28 08:30:00', '2026-04-30 10:30:00', 3, 101, 50);

INSERT INTO Room (roomid, roomtype) VALUES
    (101, 'Single'),
    (102, 'Single'),
    (103, 'Double'),
    (104, 'Suite'),
    (105, 'Deluxe'),
    (106, 'Ultra Deluxe');

SELECT roomtype, roomid from Room;

SELECT room.roomid, room.roomtype
FROM Room
JOIN Reservation on room.roomid = reservation.roomid
WHERE dateandtimestart LIKE '2026-03-29 %';

SELECT room.roomid, reservation.reservationid, room.roomtype, reservation.price, reservation.dateandtimestart, reservation.dateandtimeend
FROM Room
JOIN Reservation on room.roomid = reservation.roomid;

SELECT room.roomid, room.roomtype, COUNT(reservation.roomid)
FROM Room
JOIN Reservation on room.roomid = reservation.roomid
GROUP BY room.roomid;

SELECT *
FROM Room
JOIN Reservation on room.roomid = reservation.roomid
WHERE '2026-04-18 12:00:00' BETWEEN dateandtimestart AND dateandtimeend;

SELECT * FROM Room
LEFT JOIN Reservation ON Room.roomid = Reservation.roomid
WHERE Reservation.reservationid IS NULL;

SELECT room.roomid, room.roomtype, SUM(Reservation.price)
FROM Room
JOIN Reservation on room.roomid = reservation.roomid
GROUP BY room.roomid;

SELECT SUM(Reservation.price)
FROM Room
JOIN Reservation on room.roomid = reservation.roomid;

SELECT SUM(Reservation.price)
FROM Room
JOIN Reservation on room.roomid = reservation.roomid
WHERE dateandtimestart BETWEEN '2026-04-01 00:00:01' AND '2026-05-01 00:00:01';

SELECT User.userid, User.name, COUNT(reservation.roomid)
FROM User
JOIN Reservation ON User.userid = reservation.userid
GROUP BY User.userid
HAVING COUNT(reservation.roomid) > 1;

SELECT COUNT(reservation.roomid)
FROM Room
JOIN Reservation on room.roomid = reservation.roomid
WHERE dateandtimestart BETWEEN '2026-04-01 00:00:01' AND '2026-05-01 00:00:01';


