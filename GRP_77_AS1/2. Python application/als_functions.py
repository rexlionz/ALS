import pandas as pd
import sqlalchemy as db
import datetime as dt

engine = db.create_engine('mysql+mysqlconnector://root:Ivanchin26@localhost/als')
# database is called “als”. A user account “root” and a database “als” has earlier 
# been created in the MySQL server. User is root and password is 1234qwer.
# MySQL server is running at localhost.

connection = engine.connect()
metadata = db.MetaData()
alsMembers = db.Table('alsMember', metadata, autoload_with=engine)
books = db.Table('Book', metadata, autoload_with=engine)
bookAuthors = db.Table('bookAuthor', metadata, autoload_with=engine)
reserves = db.Table('Reserve', metadata, autoload_with=engine)
payments = db.Table('Payment', metadata, autoload_with=engine)
fines = db.Table('Fine', metadata, autoload_with=engine)

# CHECKING FUNCTIONS
def numLoans(idx):
    query = db.select(books.columns.accNo).where(books.columns.loanID == idx)
    loans = connection.execute(query).all()
    return len(loans)

def numReservations(idx):
    query = db.select(reserves.columns.accNo).where(reserves.columns.memberID == idx)
    reservations = connection.execute(query).all()
    return len(reservations)

def paymentDue(idx):
    query = db.select(payments.columns.paymentAmount).where(payments.columns.memberID == idx)
    return connection.execute(query).first()[0]

def hasFines(idx):
    return paymentDue(idx) > 0

def onLoan(acc_num):
    query = db.select(books.columns.loanID).where(books.columns.accNo == acc_num)
    return connection.execute(query).first()[0] is not None

def onReservation(acc_num):
    query = db.select(reserves.columns.memberID).where(reserves.columns.accNo == acc_num)
    return connection.execute(query).first() is not None

def memberExists(idx):
    query = db.select(alsMembers.columns.memberID).where(alsMembers.columns.memberID == idx)
    return connection.execute(query).first() is not None

def getMemberInfo(idx):
    query = db.select(alsMembers).where(alsMembers.columns.memberID == idx)
    return connection.execute(query).first()

def bookExists(acc_no):
    query = db.select(books).where(books.columns.accNo == acc_no)
    return connection.execute(query).first() is not None

def getBookInfo(acc_no):
    query = db.select(books).where(books.columns.accNo == acc_no)
    return connection.execute(query).first()

def getBookDueDate(acc_no):
    query = db.select(books.columns.loanBorrowDate).where(books.columns.accNo == acc_no)
    borrow_date = connection.execute(query).first()[0]
    due_date = borrow_date + dt.timedelta(days=14)
    return due_date

def getPaymentInfo(idx):
    query = db.select(payments).where(payments.columns.memberID == idx)
    return connection.execute(query).first()

def getEarliestReservation(acc_no):
    query = db.select(reserves.columns.memberID).where(reserves.columns.accNo == acc_no).order_by(reserves.columns.reserveDate.asc())
    return connection.execute(query).first()[0]

def reservationExists(acc_no, idx):
    query = db.select(reserves).where(reserves.columns.accNo == acc_no, reserves.columns.memberID == idx)
    return connection.execute(query).first() is not None

def validDate(date):
    try:
        dt.datetime.strptime(date, "%d/%m/%Y")
        return True
    except:
        return False

def validNumber(num):
    try:
        int(num) 
        return True
    except:
        return False

# ALSMEMBER FUNCTIONS
def canCreateMember(idx, name, fac, phone, email):
    try:
        # insert into alsMembers
        query = db.insert(alsMembers).values(memberID = idx,
                                    memberName = name, 
                                    faculty = fac, 
                                    phoneNum = phone, 
                                    emailAddress = email)
        results = connection.execute(query)
        # insert into payments
        query = db.insert(payments).values(memberID = idx,
                                    paymentAmount = 0)
        results = connection.execute(query)
        return True
    except:
        return False

def canDeleteMember(idx):
    # check if member has loans, reservations or outstanding fines
    return numLoans(idx) == 0 and numReservations(idx) == 0 and hasFines(idx) == False

def deleteMember(idx):
    query = db.delete(alsMembers).where(alsMembers.columns.memberID == idx)
    results = connection.execute(query)
    query = db.delete(payments).where(payments.columns.memberID == idx)
    results = connection.execute(query)

def updateMember(idx, name, fac, phone, email):
    query = db.update(alsMembers).values(memberName = name, 
                                        faculty = fac, 
                                        phoneNum = phone, 
                                        emailAddress = email)
    query = query.where(alsMembers.columns.memberID == idx)
    results = connection.execute(query)

# BOOK FUNCTIONS
def borrowBook(acc_no, idx):
    query = db.update(books).values(loanID = idx,
                                    loanBorrowDate = dt.date.today())
    query = query.where(books.columns.accNo == acc_no)
    results = connection.execute(query)
    
def returnBook(acc_no):
    # update books
    query = db.update(books).values(loanID = None,
                                    loanBorrowDate = None).where(books.columns.accNo == acc_no)
    results = connection.execute(query)

# FINE / PAYMENT FUNCTIONS
def calculateFine(acc_no, return_date):
    due_date = getBookDueDate(acc_no)
    return_date = dt.datetime.strptime(return_date, '%d/%m/%Y').date()
    duration = return_date - due_date
    duration_in_s = duration.total_seconds()
    if duration_in_s > 0:
        days = duration.days
        amt = divmod(duration_in_s, 86400)[0]
        return int(amt)
    else:
        return 0

def createFine(idx, date, amt):
    # update fine
    if hasFines(idx):
        query = db.select(fines.columns.fineAmount).where(fines.columns.memberID == idx)
        new_fine_amount = connection.execute(query).first()[0] + amt
        query = db.update(fines).values(fineAmount = new_fine_amount, fineDate = date).where(fines.columns.memberID == idx)
        ResultProxy = connection.execute(query)
    else:
        query = db.insert(fines).values(memberID = idx,
                                           fineAmount = amt,
                                           fineDate = date)
        ResultProxy = connection.execute(query)
        
    # update payment
    query = db.select(payments.columns.paymentAmount).where(payments.columns.memberID == idx)
    new_payment_amount = connection.execute(query).first()[0] + amt
    query = db.update(payments).values(paymentAmount = new_payment_amount).where(payments.columns.memberID == idx)
    ResultProxy = connection.execute(query)

def checkPaymentAmount(idx, amt):
    # check if amt != paymentAmount
    query = db.select(payments.columns.paymentAmount).where(payments.columns.memberID == idx)
    paymentAmount = connection.execute(query).first()[0]
    return amt == paymentAmount
    
def payFine(idx, date, amt):
    datetime_object = dt.datetime.strptime(date, '%d/%m/%Y')
    # update fine
    query = db.delete(fines).where(fines.columns.memberID == idx)
    results = connection.execute(query)
    # update payment
    query = db.update(payments).values(paymentAmount = 0, paymentDate = datetime_object).where(payments.columns.memberID == idx)
    results = connection.execute(query)

def canCreateBook(acc_num, tt, authors, isbn, pub, pub_yr):
    try:
        # update Book 
        query = db.insert(books).values(accNo = acc_num,
                                        title = tt,
                                        ISBN = isbn,
                                        publisher = pub,
                                        publicationYear = pub_yr)
        results = connection.execute(query)
        
        # update BookAuthor
        authors_list = authors.split(",")
        for a in authors_list:
            if a == "":
                continue
            query = db.insert(bookAuthors).values(accNo = acc_num, author = a)
            results = connection.execute(query)
        return True
        
    except:
        return False

def deleteBook(acc_num):
    # delete from books
    query = db.delete(books).where(books.columns.accNo == acc_num)
    results = connection.execute(query)
    
    # delete from booksauthor
    query = db.delete(bookAuthors).where(bookAuthors.columns.accNo == acc_num)
    results = connection.execute(query)

def createReservation(acc_no, idx, reserve_date):
    # create reservation
    datetime_object = dt.datetime.strptime(reserve_date, '%d/%m/%Y')
    query = db.insert(reserves).values(memberID = idx, accNo = acc_no, reserveDate = datetime_object)
    results = connection.execute(query)
    
def deleteReservation(acc_no, idx):
    # delete from reservation
    query = db.delete(reserves).where(reserves.columns.memberID == idx, reserves.columns.accNo == acc_no)
    results = connection.execute(query)

# BOOK SEARCH
def bookSearch(search_title, search_authors, search_isbn, search_pub, search_yr):
    query = db.select(books)
    df = pd.read_sql(query, engine)
    authors = []
    for acc_no in df["accNo"]:
        authors.append(getAuthors(acc_no))
    df["authors"] = authors
    df = df[["accNo", "title", "authors", "ISBN", "publisher", "publicationYear"]]
    
    # use regex to filter df
    if search_title:
        df = df[df.title.str.contains(f"(?:^|\W){search_title}(?:$|\W)")]
    if search_authors:
        df = df[df.authors.str.contains(f"(?:^|\W){search_authors}(?:$|\W)")]
    if search_isbn:
        df = df[df.ISBN.str.contains(f"(?:^|\W){search_isbn}(?:$|\W)")]
    if search_pub:    
        df = df[df.publisher.str.contains(f"(?:^|\W){search_pub}(?:$|\W)")]
    if search_yr:
        df = df[df.publicationYear.str.contains(f"(?:^|\W){search_yr}(?:$|\W)")]
    
    return df

# DISPLAY FUNCTIONS
def getAuthors(acc_no):
    query = db.select(bookAuthors.columns.author).where(bookAuthors.columns.accNo == acc_no)
    authors = connection.execute(query).all()
    s = ""
    for a in authors:
        s += a[0] + ", "
    return s[:-2]

def displayBookLoans():
    query = db.select(books).where(books.columns.loanID != None)
    df = pd.read_sql(query, engine)
    authors = []
    for acc_no in df["accNo"]:
        authors.append(getAuthors(acc_no))
    df["authors"] = authors
    return df[["accNo", "title", "authors", "ISBN", "publisher", "publicationYear"]]

def displayReservations():
    query = db.select(reserves.join(alsMembers,
                                    alsMembers.columns.memberID == reserves.columns.memberID).join(books,
                                    books.columns.accNo == reserves.columns.accNo))
    df = pd.read_sql(query, engine)
    return df[["accNo", "title", "memberID", "memberName"]]

def displayMemberFines():
    query = db.select(fines.join(alsMembers, alsMembers.columns.memberID == fines.columns.memberID))
    df = pd.read_sql(query, engine)
    return df[["memberID", "memberName", "faculty", "phoneNum", "emailAddress"]]

def displayMemberLoans(idx):
    query = db.select(books).where(books.columns.loanID == idx)
    df = pd.read_sql(query, engine)
    authors = []
    for acc_no in df["accNo"]:
        authors.append(getAuthors(acc_no))
    df["authors"] = authors
    return df[["accNo", "title", "authors", "ISBN", "publisher", "publicationYear"]]

'''
pd.read_sql('alsMember', engine)
pd.read_sql('Book', engine)
pd.read_sql('BookAuthor', engine)
pd.read_sql('Reserve', engine)
pd.read_sql('Payment', engine)
pd.read_sql('Fine', engine)
'''
