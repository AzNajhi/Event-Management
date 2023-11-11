CREATE DATABASE iiumdb;

CREATE TABLE Faculties (
    faculty_id VARCHAR(10) PRIMARY KEY,
    faculty_name VARCHAR(50) NOT NULL,
    dean VARCHAR(50),
    contact VARCHAR(50)
);

INSERT INTO Faculties (faculty_id, faculty_name, dean, contact)
VALUES ('IIUMKOL', 'Kulliyyah of Laws', 'Dr Farid Sufian', '+603 6421 4252'),
		('IIUMKEN', 'Kulliyyah of Economics', 'Dr Gairuzazmi', '+603 6421 4255'),
        ('IIUMKOE', 'Kulliyyah of Engineering', 'Dr Sany Izan', '+603-6421 4485'),
        ('IIUMKICT', 'Kulliyyah of ICT', 'Dr Murni', '+603 6421 5601'),
        ('IIUMKHS', 'Kulliyyah of Human Sciences', 'Dr Shukran', '+603 6421 5051');

CREATE TABLE Programmes (
    program_id VARCHAR(10) PRIMARY KEY,
    program_name VARCHAR(50) NOT NULL,
    faculty_id VARCHAR(10),
    head_of_program VARCHAR(50),
    FOREIGN KEY (faculty_id) REFERENCES Faculties(faculty_id)
);

INSERT INTO Programmes (program_id, program_name, faculty_id, head_of_program)
VALUES ('KOLCIV', 'Bachelor of Civil Laws', 'IIUMKOL', 'Dr Rafidah'),
		('KOLSHAR', 'Bachelor of Shariah Laws', 'IIUMKOL', 'Dr Noraini'),
        ('KENECO', 'Bachelor of Economics', 'IIUMKEN', 'Dr Mohamed Asmy'),
        ('KENACC', 'Bachelor of Accounting', 'IIUMKEN', 'Dr Hazrani'),
        ('KOEECE', 'Bachelor of Electrical and Computer Engineering', 'IIUMKOE', 'Dr Nursyuhaiza'),
        ('KOEMEC', 'Bachelor of Mechanical Engineering', 'IIUMKOE', 'Dr Hanan'),
        ('KICTCS', 'Bachelor of Computer Sciences', 'IIUMKICT', 'Dr Amir Atiff'),
        ('KICTSE', 'Bachelor of Software Engineering', 'IIUMKICT', 'Dr Khairul Azmi'),
        ('KHSPSCH', 'Bachelor of Psychology', 'IIUMKHS', 'Dr Jusmawati'),
        ('KHSSOCA', 'Bachelor of Sociology Anthropology', 'IIUMKHS', 'Dr Rohaiza');

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender ENUM('Male', 'Female'),
    email VARCHAR(50),
    program_id VARCHAR(10),
    FOREIGN KEY (program_id) REFERENCES Programmes(program_id)
);

INSERT INTO Students (student_id, first_name, last_name, gender, email, program_id)
	VALUES (162000, 'Adhwa Fathullah', 'Harun Ar-Rasyid', 'Male', 'adhwas@iium.edu.my', 'KOLCIV'),
			(162001, 'Amirul Aidy', 'Amiruldin', 'Male', 'aidys@iium.edu.my', 'KOLSHAR'),
            (162002, 'Nur Syida', 'Hafizuddin', 'Female', 'nursyidas@iium.edu.my', 'KENECO'),
            (162003, 'Nur Fahmida', 'Mohd Saiful', 'Female', 'nurfahmidas@iium.edu.my', 'KENACC'),
            (162004, 'Ahmad Zun Najhi', 'Mohd Taam', 'Male', 'zunnajhis@iium.edu.my', 'KOEECE'),
			(162005, 'Zulhilmi', 'Sabri', 'Male', 'zulhilmis@iium.edu.my', 'KOEMEC'),
            (162006, 'Amir Ng', 'Firdaus Ng', 'Male', 'amirngs@iium.edu.my', 'KICTCS'),
            (162007, 'Amelia Wong', 'Izzudeen Wong', 'Female', 'amelias@iium.edu.my', 'KICTSE'),
            (162008, 'Yusof', 'Mohd Yasin', 'Male', 'yusofs@iium.edu.my', 'KHSPSCH'),
            (162009, 'Nurhanisah', 'Kamaruzaman', 'Female', 'nurhanisahs@iium.edu.my', 'KHSSOCA');
			
CREATE TABLE Lecturers (
    lecturer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender ENUM('Male', 'Female'),
    email VARCHAR(50),
    faculty_id VARCHAR(10),
    FOREIGN KEY (faculty_id) REFERENCES Faculties(faculty_id)
);

INSERT INTO Lecturers (lecturer_id, first_name, last_name, gender, email, faculty_id)
	VALUES (1000, 'Dr Rafidah', 'Sahar', 'Female', 'rafidah@iium.edu.my', 'IIUMKOL'),
			(1001, 'Dr Noraini', 'Hashim', 'Female', 'noraini@iium.edu.my', 'IIUMKOL'),
            (1002, 'Dr Mohamed Asmy', 'Mohd Thas Thaker', 'Male', 'asmy@iium.edu.my', 'IIUMKEN'),
            (1003, 'Dr Hazrani', 'Hassan Basri', 'Male', 'hazrani@iium.edu.my', 'IIUMKEN'),
            (1004, 'Dr Nursyuhaiza', 'Aziz', 'Female', 'syuhaiza@iium.edu.my', 'IIUMKOE'),
            (1005, 'Dr Hanan', 'Mokhtar', 'Female', 'syuhaiza@iium.edu.my', 'IIUMKOE'),
			(1006, 'Dr Amir Atiff', 'Amir Hussin', 'Male', 'syuhaiza@iium.edu.my', 'IIUMKICT'),
			(1007, 'Dr Khairul Azmi', 'Hassan', 'Male', 'syuhaiza@iium.edu.my', 'IIUMKICT'),
            (1008, 'Dr Jusmawati', 'Fauzaman', 'Female', 'syuhaiza@iium.edu.my', 'IIUMKHS'),
            (1009, 'Dr Rohaiza', 'Abd Rokis', 'Female', 'syuhaiza@iium.edu.my', 'IIUMKHS');

CREATE TABLE Subjects (
    subject_id VARCHAR(10) PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL,
    credit_hour INT,
    program_id VARCHAR(10),
    lecturer_id INT,
    FOREIGN KEY (program_id) REFERENCES Programmes(program_id),
    FOREIGN KEY (lecturer_id) REFERENCES Lecturers(lecturer_id)
);

INSERT INTO Subjects (subject_id, subject_name, credit_hour, program_id, lecturer_id)
		VALUES ('LAW101', 'Introduction to Civil Law', 3, 'KOLCIV', 1000),
				('LAW102', 'Introduction to Shariah Law', 3, 'KOLSHAR', 1001),
                ('KEN101', 'Introduction to Economics', 3, 'KENECO', 1002),
                ('KEN102', 'Introduction to Accounting', 3, 'KENACC', 1003),
                ('KOE101', 'Introduction to Electrical Engineering', 3, 'KOEECE', 1004),
                ('KOE102', 'Introduction to Mechanical Engineering', 3, 'KOEMEC', 1005),
                ('KICT101', 'Introduction to Computer Science', 3, 'KICTCS', 1006),
                ('KICT102', 'Introduction to Software Engineering', 3, 'KICTSE', 1007),
                ('KHS101', 'Introduction to Psychology', 3, 'KHSPSCH', 1008),
                ('KHS102', 'Introduction to Sociology Anthropology', 3, 'KHSSOCA', 1009);