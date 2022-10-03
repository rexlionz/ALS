CREATE TABLE alsMember(  
	memberID VARCHAR(6) UNIQUE NOT NULL,
	memberName  VARCHAR(256) NOT NULL,
	faculty VARCHAR(256) NOT NULL,
	phoneNum INT NOT NULL,
	emailAddress VARCHAR(256) NOT NULL,
	PRIMARY KEY (memberID));
  
CREATE TABLE Book(
	accNo VARCHAR(20) UNIQUE NOT NULL,
	title VARCHAR(256) NOT NULL,
	ISBN VARCHAR(13) NOT NULL,
    publisher VARCHAR(256) NOT NULL,
    publicationYear VARCHAR(4) NOT NULL,
	loanID VARCHAR(5) DEFAULT NULL,
    loanBorrowDate DATE DEFAULT NULL,
	PRIMARY KEY (accNo),
    FOREIGN KEY (loanID) REFERENCES alsMember(memberID));

CREATE TABLE Reserve(
	memberID  VARCHAR(6) NOT NULL,
	accNo VARCHAR(20) NOT NULL,
	reserveDate DATE NOT NULL,
	PRIMARY KEY (memberID, accNo),
	FOREIGN KEY (memberID) references alsMember(memberID),
	FOREIGN KEY (accNo) references Book(accNo));
     
CREATE TABLE BookAuthor(
	accNo VARCHAR(20) NOT NULL,
    author VARCHAR(256) NOT NULL,
    PRIMARY KEY (accNo, author));
     
CREATE TABLE Fine(
	memberID VARCHAR(6) UNIQUE NOT NULL,
	fineDate DATE,
	fineAmount INT,
	PRIMARY KEY (memberID, fineAmount),
	FOREIGN KEY (memberID) references alsMember(memberID));
    
CREATE TABLE Payment(
	memberID VARCHAR(6) UNIQUE NOT NULL,
	paymentDate DATE,
	paymentAmount INT DEFAULT 0,
	PRIMARY KEY (memberID),
	FOREIGN KEY (memberID) references alsMember(memberID));
    