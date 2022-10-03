import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font
from PIL import ImageTk, Image

class ALS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.main_title_font = font.Font(family='Helvetica', size=30, weight="bold")
        self.headings_font = font.Font(family='Helvetica', size=18, weight="bold")
        self.headings_font2 = font.Font(family='Helvetica', size=18)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MembershipPage, BooksPage, 
        LoansPage, BorrowBookPage, ReturnBookPage, 
        ReservationsPage, BookReservationPage, BookCancellationPage, 
        FinesPage, FinePaymentPage, ReportsPage, 
        CreateMemberPage, DeleteMemberPage, UpdateMemberPage, UpdateMemberPageTwo,
        BookAcquisitionPage, BookWithdrawalPage, 
        BookSearchPage, BooksOnLoanPage, BooksOnReservationPage, OutstandingFinesPage, LoansToMemberPage):
            page_name = F.__name__
            frame = F(parent=container, navigator=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
    
    def show_frame(self, page_name, *args):
        frame = self.frames[page_name]
        param = args[0] if args else None
        if param != None:
            frame.membershipID = param
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent, background= "#e6f9ff")
        self.navigator = navigator

        mainLabel = tk.Label(self, text = "ALS", font = navigator.main_title_font, bg = "#b3f0ff")
        mainLabel.config(width = 39)

        mainLabel.config(font = (navigator.main_title_font, 60))


        #initialise images
        membershipPhoto = Image.open("images/membershipPhoto.jpeg").resize((400,280))
        membershipPhoto= ImageTk.PhotoImage(membershipPhoto)
        
        bookPhoto = Image.open("images/book.png").resize((400,280))
        bookPhoto = ImageTk.PhotoImage(bookPhoto)
        
        loansPhoto = Image.open("images/loan.png").resize((400,280))
        loansPhoto = ImageTk.PhotoImage(loansPhoto)
        
        reservationsPhoto = Image.open("images/booking.png").resize((400,280))
        reservationsPhoto = ImageTk.PhotoImage(reservationsPhoto)
        
        finesPhoto = Image.open("images/money.png").resize((400,280))
        finesPhoto = ImageTk.PhotoImage(finesPhoto)
        
        reportsPhoto = Image.open("images/monitor.png").resize((400,280))
        reportsPhoto = ImageTk.PhotoImage(reportsPhoto)        

        #initialise buttons
        membershipButton = tk.Button(self, text = "Membership", image = membershipPhoto, compound = "top", command = lambda: navigator.show_frame("MembershipPage"), font = navigator.headings_font)
        membershipButton.image = membershipPhoto
        
        booksButton = tk.Button(self, text = "Books", image = bookPhoto, compound = "top", width = 40, height = 20,command = lambda: navigator.show_frame("BooksPage"), font = navigator.headings_font)
        booksButton.image = bookPhoto
        
        loansButton = tk.Button(self, text = "Loans", image = loansPhoto, compound = "top", width = 40, height = 20, command = lambda: navigator.show_frame("LoansPage"), font = navigator.headings_font)
        loansButton.image = loansPhoto
        
        reservationsButton = tk.Button(self, text = "Reservations", image = reservationsPhoto, compound = "top", width = 40, height = 20, command = lambda: navigator.show_frame("ReservationsPage"), font = navigator.headings_font)
        reservationsButton.image = reservationsPhoto
        
        finesButton = tk.Button(self, text = "Fines", image = finesPhoto, compound = "top", width = 40, height = 20, command = lambda: navigator.show_frame("FinesPage"), font = navigator.headings_font)
        finesButton.image = finesPhoto
        
        reportsButton = tk.Button(self, text = "Reports", image = reportsPhoto, compound = "top", width = 40, height = 20, command = lambda: navigator.show_frame("ReportsPage"), font = navigator.headings_font)
        reportsButton.image = reportsPhoto
        
        #show on screen
        mainLabel.grid(row=0, column=1, columnspan = 3, sticky=tk.NSEW)
        membershipButton.grid(row=1, column= 1, padx = 20, pady = 20)
        booksButton.grid(row = 1, column= 2, padx = 20, pady = 20)
        loansButton.grid(row = 1, column = 3, padx = 20, pady = 20)
        reservationsButton.grid(row = 2, column = 1, padx = 20, pady = 20)
        finesButton.grid(row = 2, column = 2, padx = 20, pady = 20)
        reportsButton.grid(row = 2, column = 3, padx = 20, pady = 20)

class MembershipPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent, background= "#e6f9ff")
        self.navigator = navigator
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame2a = tk.Frame(frame2)
        frame2a.pack(side = 'left')
        frame2b = tk.Frame(frame2)
        frame2b.pack(side = 'left', fill='both')
        frame2c = tk.Frame(frame2)
        frame2c.pack(side = 'left', fill='both')
        frame3 = tk.Frame(self)
        frame3.pack(fill='both')
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Select one of the options below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        "Frame 2"
        membershipPhoto =  ImageTk.PhotoImage(Image.open("images/membershipPhoto.jpeg"))
        membershipIcon = Label(frame2a, text = "Membership", compound = tk.TOP, image = membershipPhoto, font = navigator.headings_font)
        membershipIcon.pack(side = "left")
        membershipIcon.image = membershipPhoto

        membershipCreation = tk.Button(frame2b, text = "Creation", command = lambda: navigator.show_frame("CreateMemberPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE', width = 30)
        membershipDeletion = tk.Button(frame2b, text = "Deletion", command = lambda: navigator.show_frame("DeleteMemberPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE', width = 30)
        membershipUpdate = tk.Button(frame2b, text = "Update", command = lambda: navigator.show_frame("UpdateMemberPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE', width = 30)

        membershipCreation.pack(side = "top", fill = "both", expand= True, ipadx = 150)
        membershipDeletion.pack(side = "top", fill = "both", expand= True)
        membershipUpdate.pack(side = "top", fill = "both", expand= True)

        "Frame 3"
        emptySpace = tk.Label(frame3, background= "#e6f9ff")
        mainMenuButton = tk.Button(frame3, text= "Back to Main Menu", command = lambda: navigator.show_frame("StartPage"), pady = 40, relief= tk.SUNKEN, highlightbackground = '#FFAAA6', font = navigator.headings_font2)

        emptySpace.pack(fill = 'x', ipady= 20)
        mainMenuButton.pack(fill= 'x', ipady=10)

        membershipCreationInfo = tk.Label(frame2c, text = "To Create Member", font = self.navigator.headings_font2, bg = '#ebf9f4')
        membershipDeletionInfo = tk.Label(frame2c, text = "To Delete Member", font = self.navigator.headings_font2, bg = '#ebf9f4')
        membershipUpdateInfo = tk.Label(frame2c, text = "To Update Member", font = self.navigator.headings_font2, bg = '#ebf9f4')

        membershipCreationInfo.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        membershipDeletionInfo.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        membershipUpdateInfo.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)

class CreateMemberPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.membershipID = None
        self.name = None
        self.faculty = None
        self.phoneNum = None
        self.email = None

        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()

        "top"
        "Frame 1"
        topLabel = tk.Label(frame1, text = "To Create Member, Please Enter Requested Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        "middle"
        def getMembershipID(ID):
            ID = entryBox1.get()
            self.membershipID = ID

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Membership ID :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getMembershipID)
        entryBox1.pack(side = 'left')
        frame2a.pack()

        def getName(name):
            name = entryBox2.get()
            self.name = name

        frame2b = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2b, text = "Name :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2b, width = 30)
        entryBox2.bind("<Return>", getName)
        entryBox2.pack(side = 'left')
        frame2b.pack()

        def getFaculty(faculty):
            faculty = entryBox3.get()
            self.faculty = faculty

        frame2c = tk.Frame(frame2)
        entryLabel3 = tk.Label(frame2c, text = "Faculty :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel3.pack(side = 'left')
        entryBox3 = tk.Entry(frame2c, width = 30)
        entryBox3.bind("<Return>", getFaculty)
        entryBox3.pack(side = 'left')
        frame2c.pack()

        def getPhoneNum(num):
            num = entryBox4.get()
            self.phoneNum = num

        frame2d = tk.Frame(frame2)
        entryLabel4 = tk.Label(frame2d, text = "Phone Number :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel4.pack(side = 'left')
        entryBox4 = tk.Entry(frame2d, width = 30)
        entryBox4.bind("<Return>", getPhoneNum)
        entryBox4.pack(side = 'left')
        frame2d.pack()

        def getEmail(email):
            email = entryBox5.get()
            self.email = email

        frame2e = tk.Frame(frame2)
        entryLabel5 = tk.Label(frame2e, text = "Email :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel5.pack(side = 'left')
        entryBox5 = tk.Entry(frame2e, width = 30)
        entryBox5.bind("<Return>", getEmail)
        entryBox5.pack(side = 'left')
        frame2e.pack()

        "bottom"
        createMemberButton = tk.Button(frame3, text= "Create Member", width= 60, height = 5, command = self.create_member, highlightbackground = '#A8E6CE')
        createMemberButton.pack(side = 'left')

        membershipMenuButton = tk.Button(frame3, text= "Back to Membership Menu", width= 60, height = 5, command = lambda: navigator.show_frame("MembershipPage"), highlightbackground = '#FFAAA6')
        membershipMenuButton.pack(side = 'left')
    
    def create_member(self):
        # create member popup
        if canCreateMember(self.membershipID, self.name, self.faculty, self.phoneNum, self.email):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
            label2 = tk.Label(self.top, text = "ALS Member Created", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Create Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")

        # error popup
        else:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member already exists; Missing or Incomplete fields.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Create Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class DeleteMemberPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.membershipID = None

        topLabel = tk.Label(self, text = "To Delete Member, Please Enter Membership ID", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        "middle"
        def getMembershipID(ID):
            ID = entryBox.get()
            self.membershipID = ID
        
        frame1 = tk.Frame(self)
        entryLabel = tk.Label(frame1, text = "Membership ID :", width = 15, height = 15, font = navigator.headings_font)
        entryLabel.pack(side = 'left')
        entryBox = tk.Entry(frame1)
        entryBox.bind("<Return>", getMembershipID)
        entryBox.pack(side = 'left')
        frame1.pack()
        

        "bottom"
        frame2 = tk.Frame(self)
        deleteButton = tk.Button(frame2, text= "Delete Member", width= 60, height = 5, command= self.confirm_deletion, highlightbackground = '#A8E6CE')

        membershipMenuButton = tk.Button(frame2, text= "Back to Membership Menu", width= 60, height = 5, command = lambda: navigator.show_frame("MembershipPage"), highlightbackground = '#FFAAA6')
        deleteButton.pack(side = 'left')
        membershipMenuButton.pack(side = 'left')
        frame2.pack(pady = 100)
        
    def confirm_deletion(self):
        # error popup - member does not exist 
        if not memberExists(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Delete Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # confirmation popup
        else:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            
            idx, fname, fac, phone, email = getMemberInfo(self.membershipID)

            mainLabel = tk.Label(self.top, text = "Please Confirm\nDetails To Be Correct", font = (self.navigator.main_title_font, 40, font.BOLD))
            memberID = tk.Label(self.top, text = "Member ID : " + self.membershipID, font = self.navigator.headings_font)
            name = tk.Label(self.top, text = "Name : " + fname, font = self.navigator.headings_font)
            faculty = tk.Label(self.top, text = "Faculty : " + fac, font = self.navigator.headings_font)
            phoneNum = tk.Label(self.top, text = "Phone Number : " + str(phone), font = self.navigator.headings_font)
            email = tk.Label(self.top, text = "Email Address : " + email, font = self.navigator.headings_font)
            confirmDeletion = tk.Button(self.top, text = "Confirm Deletion", font = self.navigator.headings_font, command = self.delete_member, width = 24, height = 3, highlightbackground = '#A8E6CE')
            escapeDeletion = tk.Button(self.top, text = "Back to Delete Function", font = self.navigator.headings_font, command = self.close_popup, width = 24, height = 3, highlightbackground =  '#FFAAA6')

            mainLabel.pack(ipady = 20)
            memberID.pack(ipady = 20)
            name.pack(ipady = 20)
            faculty.pack(ipady = 20)
            phoneNum.pack(ipady = 20)
            email.pack(ipady = 20)
            confirmDeletion.pack(side = "left", fill = "x", expand=True)
            escapeDeletion.pack(side = "left", fill = "x", expand=True)

    def delete_member(self):
        self.top.grab_release()
        self.top.destroy()
        
        if canDeleteMember(self.membershipID):
            deleteMember(self.membershipID)
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
            label2 = tk.Label(self.top, text = "ALS Member Deleted.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Delete Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")

        # error popup - member does not exist 
        else:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member has loans, reservations or outstanding fines.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Delete Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class UpdateMemberPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.membershipID = None
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "To Update a Member, Please Enter Membership ID:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        
        def getMembershipID(ID):
            ID = entryBox1.get()
            self.membershipID = ID
            
        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Membership ID :", width = 15, height = 20, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getMembershipID)
        entryBox1.pack(side = 'left')
        frame2a.pack()
        
        updateButton = tk.Button(frame3, text= "Update Member", width= 60, height = 5, command = lambda: navigator.show_frame("UpdateMemberPageTwo", self.membershipID),  highlightbackground = '#A8E6CE')
        updateButton.config(font = (navigator.headings_font, 14))
        membershipMenuButton = tk.Button(frame3, text= "Back to Membership Menu", width= 60, height = 5, command = lambda: navigator.show_frame("MembershipPage"), highlightbackground = '#FFAAA6')
        membershipMenuButton.config(font = (navigator.headings_font, 14))
        updateButton.pack(side = 'left')
        membershipMenuButton.pack(side = 'left')
        
class UpdateMemberPageTwo(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.name = None
        self.membershipID = None
        self.faculty = None
        self.phoneNum = None
        self.email = None

        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()

        topLabel = tk.Label(frame1, text = "Please Enter Requested Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        frame2a = tk.Frame(frame2)
        
        entryLabel1 = tk.Label(frame2a, text = "Membership ID :", width = 12, height = 5, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        memLabel = tk.Label(frame2a, text = "Previously Filled",  font = navigator.headings_font, width = 30)
        memLabel.pack(side = 'left')
        frame2a.pack()
        

        def getName(name):
            name = entryBox2.get()
            self.name = name

        frame2b = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2b, text = "Name :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2b, width = 30)
        entryBox2.bind("<Return>", getName)
        entryBox2.pack(side = 'left')
        frame2b.pack()

        def getFaculty(faculty):
            faculty = entryBox3.get()
            self.faculty = faculty

        frame2c = tk.Frame(frame2)
        entryLabel3 = tk.Label(frame2c, text = "Faculty :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel3.pack(side = 'left')
        entryBox3 = tk.Entry(frame2c, width = 30)
        entryBox3.bind("<Return>", getFaculty)
        entryBox3.pack(side = 'left')
        frame2c.pack()

        def getPhoneNum(num):
            num = entryBox4.get()
            self.phoneNum = num

        frame2d = tk.Frame(frame2)
        entryLabel4 = tk.Label(frame2d, text = "Phone Number :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel4.pack(side = 'left')
        entryBox4 = tk.Entry(frame2d, width = 30)
        entryBox4.bind("<Return>", getPhoneNum)
        entryBox4.pack(side = 'left')
        frame2d.pack()

        def getEmail(email):
            email = entryBox5.get()
            self.email = email

        frame2e = tk.Frame(frame2)
        entryLabel5 = tk.Label(frame2e, text = "Email :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel5.pack(side = 'left')
        entryBox5 = tk.Entry(frame2e, width = 30)
        entryBox5.bind("<Return>", getEmail)
        entryBox5.pack(side = 'left')
        frame2e.pack()

        "bottom"
        createMemberButton = tk.Button(frame3, text= "Update Member", width= 60, height = 5, command = self.confirmationPage, highlightbackground='#A8E6CE')
        createMemberButton.pack(side = 'left')

        membershipMenuButton = tk.Button(frame3, text= "Back to Membership Menu", width= 60, height = 5, command = lambda: navigator.show_frame("MembershipPage"), highlightbackground='#FFAAA6')
        membershipMenuButton.pack(side = 'left')

    def confirmationPage(self):
        # error popup - member does not exist 
        if not memberExists(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Update Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - incorrect date format
        if not validNumber(self.phoneNum):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Invalid phone number format.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Update Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error - Missing or Incomplete fields
        if not (self.membershipID and self.name and self.faculty and self.phoneNum and self.email):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = self.navigator.main_title_font)
            label = tk.Label(self.top, text = "Missing or\nIncomplete fields.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Update Function", command = self.close_popup, width= 60, height = 5)
            mainLabel.pack(ipady = 100)
            label.pack(ipady = 40)
            backButton.pack(side = "bottom")
            return

        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")
        
        mainLabel = tk.Label(self.top, text = "Please Confirm Updated\nDetails To Be Correct", font = (self.navigator.main_title_font, 40, font.BOLD))
        memberID = tk.Label(self.top, text = "Member ID : " + self.membershipID, font = self.navigator.headings_font)
        name = tk.Label(self.top, text = "Name : " + self.name, font = self.navigator.headings_font)
        faculty = tk.Label(self.top, text = "Faculty : " + self.faculty, font = self.navigator.headings_font)
        phoneNum = tk.Label(self.top, text = "Phone Number : " + str(self.phoneNum), font = self.navigator.headings_font)
        email = tk.Label(self.top, text = "Email Address : " + self.email, font = self.navigator.headings_font)
        confirmUpdate = tk.Button(self.top, text = "Confirm Update", font = self.navigator.headings_font, command = self.confirm_update, height = 3, highlightbackground = '#A8E6CE')
        getBack = tk.Button(self.top, text = "Back to Update Function", font = self.navigator.headings_font, command = self.close_popup, height = 3, highlightbackground =  '#FFAAA6')

        mainLabel.pack(ipady = 20)
        memberID.pack(ipady = 20)
        name.pack(ipady = 20)
        faculty.pack(ipady = 20)
        phoneNum.pack(ipady = 20)
        email.pack(ipady = 20)
        confirmUpdate.pack(side = "left", fill='x', expand= True)
        getBack.pack(side = "right", fill='x', expand= True)

    def confirm_update(self):
        self.top.grab_release()
        self.top.destroy()

        #Update success page
        updateMember(self.membershipID, self.name, self.faculty, self.phoneNum, self.email)
        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")
        mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
        label = tk.Label(self.top, text = "ALS Membership Updated", font = self.navigator.headings_font)
        anotherOne = tk.Button(self.top, text = "Update Another Member", font = self.navigator.headings_font, command = self.close_popup2, width = 24, height = 3, highlightbackground = '#A8E6CE')
        getback = tk.Button(self.top, text = "Back to Membership Menu", font = self.navigator.headings_font, command = self.close_popup3, width = 24, height = 3, highlightbackground = '#FFAAA6')
        
        mainLabel.pack(pady = 50)
        label.pack(pady = 50)
        anotherOne.pack(pady = 50, side = "left", fill = "x", expand=True)
        getback.pack(pady = 50,side = "left", fill = "x", expand=True)

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()
    
    def close_popup2(self):
        self.top.grab_release()
        self.top.destroy()
        self.navigator.show_frame("UpdateMemberPage")

    def close_popup3(self):
        self.top.grab_release()
        self.top.destroy()
        self.navigator.show_frame("MembershipPage")

class BooksPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame2a = tk.Frame(frame2)
        frame2a.pack(side = 'left')
        frame2b = tk.Frame(frame2)
        frame2b.pack(side = 'left', fill='both')
        frame2c = tk.Frame(frame2)
        frame2c.pack(side = 'left', fill='both')
        frame3 = tk.Frame(self)
        frame3.pack(fill='both')
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Select one of the options below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(ipady = 50, fill = "x")

        "Frame 2"
        bookPhoto = Image.open("images/book.png").resize((400,400))
        bookPhoto = ImageTk.PhotoImage(bookPhoto)
        bookIcon = Label(frame2a, text = "Books", compound = "top", image = bookPhoto, font = navigator.headings_font)
        bookIcon.pack(side = "left")
        bookIcon.image = bookPhoto
        acquisition = tk.Button(frame2b, text = "Acquisition", command = lambda: navigator.show_frame("BookAcquisitionPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE', width = 30)
        withdrawal = tk.Button(frame2b, text = "Withdrawal", command = lambda: navigator.show_frame("BookWithdrawalPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE', width = 30)

        acquisition.pack(side = "top", fill = "both", expand= True, ipadx = 150)
        withdrawal.pack(side = "top", fill = "both", expand= True)
        
        "Frame 3"
        emptySpace = tk.Label(frame3, background= "#e6f9ff")
        mainMenuButton = tk.Button(frame3, text= "Back to Main Menu", command = lambda: navigator.show_frame("StartPage"), pady = 40, relief= tk.SUNKEN, highlightbackground = '#FFAAA6', font = navigator.headings_font2)
        emptySpace.pack(fill = 'x', ipady= 40)
        mainMenuButton.pack(fill= 'x')
        
        acquisitionText = tk.Label(frame2c, text = "Book Acquisition", font = self.navigator.headings_font2, bg = '#ebf9f4')
        withdrawalText = tk.Label(frame2c, text = "Book Withdrawal", font = self.navigator.headings_font2, bg = '#ebf9f4')
        
        acquisitionText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        withdrawalText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)

class BookAcquisitionPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.accNo = None
        self.title = None
        self.authors = None 
        self.isbn = None 
        self.publisher = None 
        self.publicationYear = None
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "For New Book Acquisition, Please Enter Required Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        def getAccessionNum(accNo):
            accNo = entryBox1.get()
            self.accNo = accNo

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Accession Number :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getAccessionNum)
        entryBox1.pack(side = 'left')
        frame2a.pack()

        def getTitle(title):
            title = entryBox2.get()
            self.title = title

        frame2a = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2a, text = "Title :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2a, width = 30)
        entryBox2.bind("<Return>", getTitle)
        entryBox2.pack(side = 'left')
        frame2a.pack()        

        def getAuthor(authors):
            authors = entryBox3.get()
            self.authors = authors

        frame2a = tk.Frame(frame2)
        entryLabel3 = tk.Label(frame2a, text = "Authors :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel3.pack(side = 'left')
        entryBox3 = tk.Entry(frame2a, width = 30)
        entryBox3.bind("<Return>", getAuthor)
        entryBox3.pack(side = 'left')
        frame2a.pack()          

        def getISBN(isbn):
            isbn = entryBox4.get()
            self.isbn = isbn

        frame2a = tk.Frame(frame2)
        entryLabel4 = tk.Label(frame2a, text = "ISBN :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel4.pack(side = 'left')
        entryBox4 = tk.Entry(frame2a, width = 30)
        entryBox4.bind("<Return>", getISBN)
        entryBox4.pack(side = 'left')
        frame2a.pack()

        def getPublisher(publisher):
            publisher = entryBox5.get()
            self.publisher = publisher

        frame2a = tk.Frame(frame2)
        entryLabel5 = tk.Label(frame2a, text = "Publisher :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel5.pack(side = 'left')
        entryBox5 = tk.Entry(frame2a, width = 30)
        entryBox5.bind("<Return>", getPublisher)
        entryBox5.pack(side = 'left')
        frame2a.pack()
        
        def getPublicationYear(year):
            year = entryBox6.get()
            self.publicationYear = year

        frame2a = tk.Frame(frame2)
        entryLabel6 = tk.Label(frame2a, text = "Publication Year :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel6.pack(side = 'left')
        entryBox6 = tk.Entry(frame2a, width = 30)
        entryBox6.bind("<Return>", getPublicationYear)
        entryBox6.pack(side = 'left')
        frame2a.pack()

        addNewBook = tk.Button(frame3, text= "Add New Book", width= 60, height = 5, command = self.confirm_create_book, highlightbackground = "#91DDF2")
        addNewBook.config(font = (navigator.headings_font, 14))
        addNewBook.pack(side = 'left')

        bookMenuButton = tk.Button(frame3, text= "Back to Books Menu", width= 60, height = 5, command = lambda: navigator.show_frame("BooksPage"), highlightbackground = '#FFAAA6')
        bookMenuButton.config(font = (navigator.headings_font, 14))
        bookMenuButton.pack(side = 'left')
    
    def confirm_create_book(self):
        # create member popup
        if canCreateBook(self.accNo, self.title, self.authors, self.isbn, self.publisher, self.publicationYear):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
            label2 = tk.Label(self.top, text = "New Book added in Library.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Acquisition Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")

        # error popup
        else:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book already added; Duplicate, Missing or Incomplete fields.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Acquisition Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class BookWithdrawalPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.accNo = None
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        topLabel = tk.Label(frame1, text = "To Remove Outdated Books From System, Please Enter Required Information Below", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        
        def getAccessionNum(accNo):
            accNo = entryBox1.get()
            self.accNo = accNo

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Accession Number :", width = 16, height = 5, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getAccessionNum)
        entryBox1.pack(side = 'left')
        frame2a.pack()
        
        "bottom"
        frame2 = tk.Frame(self)
        deleteButton = tk.Button(frame2, text= "Withdraw Book", width= 60, height = 5, command= self.confirm_withdraw, highlightbackground = '#A8E6CE')
        deleteButton.config(font = (navigator.headings_font, 14))

        bookMenuButton = tk.Button(frame2, text= "Back to Books Menu", width= 60, height = 5, command = lambda: navigator.show_frame("BooksPage"), highlightbackground = '#FFAAA6')
        bookMenuButton.config(font = (navigator.headings_font, 14))
        deleteButton.pack(side = 'left')
        bookMenuButton.pack(side = 'left')
        frame2.pack(pady = 100)
        
    def confirm_withdraw(self):
        # error popup - member does not exist 
        if not bookExists(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Withdrawal Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - book on loan
        if onLoan(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book is currently on Loan.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Withdrawal Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return
        
        # error popup - book on reservation
        if onReservation(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book is currently on Reservation.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Withdrawal Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # confirmation popup
        else:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Please Confirm\nDetails To Be Correct", font = (self.navigator.main_title_font, 40, font.BOLD))
            mainLabel.pack()

            acc, title, isbn, publisher, year, _, _ = getBookInfo(self.accNo)
            authors = getAuthors(self.accNo)

            acc = tk.Label(self.top, text = "Accession Number : " + self.accNo, font = self.navigator.headings_font)
            title = tk.Label(self.top, text = "Title : " + title, font = self.navigator.headings_font)
            authors = tk.Label(self.top, text = "Authors : " + authors, font = self.navigator.headings_font)
            isbn = tk.Label(self.top, text = "ISBN : " + str(isbn), font = self.navigator.headings_font)
            publisher = tk.Label(self.top, text = "Publisher : " + publisher, font = self.navigator.headings_font)
            year = tk.Label(self.top, text = "Year : " + year, font = self.navigator.headings_font)
            confirmDeletion = tk.Button(self.top, text = "Confirm Withdrawal", font = self.navigator.headings_font, command = self.confirm_withdrawal, width = 24, height = 3, highlightbackground = '#A8E6CE')
            escapeDeletion = tk.Button(self.top, text = "Back to Withdrawal Function", font = self.navigator.headings_font, command = self.close_popup, width = 24, height = 3, highlightbackground = '#FFAAA6')

            acc.pack(ipady = 20)
            title.pack(ipady = 20)
            authors.pack(ipady = 20)
            isbn.pack(ipady = 20)
            publisher.pack(ipady = 20)
            year.pack(ipady = 20)
            confirmDeletion.pack(side = "left", fill = 'x', expand=True)
            escapeDeletion.pack(side = "left", fill = 'x', expand=True)


    def confirm_withdrawal(self):
        deleteBook(self.accNo)
        self.top.grab_release()
        self.top.destroy()

        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")
        mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
        label = tk.Label(self.top, text = "Book Withdrawn", font = self.navigator.headings_font)
        getback = tk.Button(self.top, text = "Back to Withdrawal Function", font = self.navigator.headings_font, command = self.close_popup, width = 24, height = 3, highlightbackground = '#FFAAA6')
        
        mainLabel.pack(pady = 50)
        label.pack(pady = 50)
        getback.pack(pady = 50)

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class LoansPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame2a = tk.Frame(frame2)
        frame2a.pack(side = 'left')
        frame2b = tk.Frame(frame2)
        frame2b.pack(side = 'left', fill='both')
        frame2c = tk.Frame(frame2)
        frame2c.pack(side = 'left', fill='both')
        frame3 = tk.Frame(self)
        frame3.pack(fill='both')
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Select one of the options below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        
        "Frame 2"
        loanPhoto = Image.open("images/loan.png").resize((400,400))
        loanPhoto = ImageTk.PhotoImage(loanPhoto)
        loanIcon = Label(frame2a, text = "Loans", compound = "top", image = loanPhoto, font = navigator.headings_font)
        loanIcon.pack(side = "left")
        loanIcon.image = loanPhoto
        
        borrowBook = tk.Button(frame2b, text = "Borrow", width = 30, command = lambda: navigator.show_frame("BorrowBookPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')
        returnBook = tk.Button(frame2b, text = "Return", width = 30, command = lambda: navigator.show_frame("ReturnBookPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')

        borrowBook.pack(side = "top", fill = "both", expand= True, ipadx = 150)
        returnBook.pack(side = "top", fill = "both", expand= True)
        
        "Frame 3"
        emptySpace = tk.Label(frame3, background= "#e6f9ff")
        mainMenuButton = tk.Button(frame3, text= "Back to Main Menu", command = lambda: navigator.show_frame("StartPage"), pady = 40, relief= tk.SUNKEN, highlightbackground = '#FFAAA6', font = navigator.headings_font2)
        emptySpace.pack(fill = 'x', ipady= 40)
        mainMenuButton.pack(fill= 'x')
        
        borrowText = tk.Label(frame2c, text = "Book Borrowing", font = self.navigator.headings_font2, bg = '#ebf9f4')
        returnText = tk.Label(frame2c, text = "Book Returning", font = self.navigator.headings_font2 ,bg = '#ebf9f4')

        borrowText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        returnText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)

class BorrowBookPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.accNo = None
        self.membershipID = None
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        topLabel = tk.Label(frame1, text = "To Borrow a Book, Please Enter Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        
        def getAccessionNum(acc):
            acc = entryBox1.get()
            self.accNo = acc

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Accession Number :", width = 16, height = 5, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getAccessionNum)
        entryBox1.pack(side = 'left')
        frame2a.pack()

        def getMembershipID(ID):
            ID = entryBox2.get()
            self.membershipID = ID

        frame2a = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2a, text = "Membership ID :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2a, width = 30)
        entryBox2.bind("<Return>", getMembershipID)
        entryBox2.pack(side = 'left')
        frame2a.pack()
        
        frame2 = tk.Frame(self)
        BorrowButton = tk.Button(frame2, text= "Borrow Book", width= 60, height = 5, command= self.confirmation_page, highlightbackground = '#A8E6CE')
        BorrowButton.config(font = (navigator.headings_font, 14))

        LoanMenuButton = tk.Button(frame2, text= "Back to Loans Menu", width= 60, height = 5, command = lambda: navigator.show_frame("LoansPage"), highlightbackground = '#FFAAA6')
        LoanMenuButton.config(font = (navigator.headings_font, 14))
        BorrowButton.pack(side = 'left')
        LoanMenuButton.pack(side = 'left')
        frame2.pack(pady = 100)
        
    def confirmation_page(self):
        # error popup - member does not exist 
        if not memberExists(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Borrow Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return
        
        # error popup - book does not exist 
        if not bookExists(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Borrow Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return
            
        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")
        mainLabel = tk.Label(self.top, text = "Confirm Loan\nDetails To Be Correct", font = (self.navigator.main_title_font, 40, font.BOLD))

        acc, title, _, _, _, _, _ = getBookInfo(self.accNo)
        idx, fname, _, _, _ = getMemberInfo(self.membershipID)

        acc = tk.Label(self.top, text = "Accession Number : " + self.accNo, font = self.navigator.headings_font)
        title = tk.Label(self.top, text = "Book Title : " + title, font = self.navigator.headings_font)
        borrowDate = tk.Label(self.top, text = "Borrow Date : " + dt.date.today().strftime('%d/%m/%Y'), font = self.navigator.headings_font)
        ID = tk.Label(self.top, text = "Membership ID : " + self.membershipID, font = self.navigator.headings_font)
        name = tk.Label(self.top, text = "Member Name : " + fname, font = self.navigator.headings_font)
        dueDate = tk.Label(self.top, text = "Due Date : " + (dt.date.today()+ dt.timedelta(days=14)).strftime('%d/%m/%Y'), font = self.navigator.headings_font)
        confirmPayment = tk.Button(self.top, text = "Confirm Loan", font = self.navigator.headings_font, command = self.confirmLoan, width = 24, height = 3, highlightbackground = '#A8E6CE')
        goback = tk.Button(self.top, text = "Back to Borrow Function", font = self.navigator.headings_font, command = self.close_popup, width = 24, height = 3, highlightbackground = '#FFAAA6')

        mainLabel.pack()
        acc.pack(ipady = 20)
        title.pack(ipady = 20)
        borrowDate.pack(ipady = 20)
        ID.pack(ipady = 20)
        name.pack(ipady = 20)
        dueDate.pack(ipady = 20)
        confirmPayment.pack(side = "left", fill = "x", expand=True)
        goback.pack(side = "left", fill = "x", expand=True)

    def confirmLoan(self):
        self.top.grab_release()
        self.top.destroy()
        
        # error - book on loan
        if onLoan(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = f"Book currently on Loan until: {getBookDueDate(self.accNo).strftime('%d/%m/%Y')}.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Borrow Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")
            return

        # error - exceed 2 books 
        if numLoans(self.membershipID) >= 2:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = "Member loan quota exceeded.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Borrow Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")
            return

        # error - have outstanding fines
        if hasFines(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = f"Member has Outstanding Fine of: ${paymentDue(self.membershipID)}.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Borrow Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")
            return

        # check if book not on reservation
        # When a reserved book becomes available (because it has been returned), 
        # it can be loaned only to the member who reserved it. When the reservation is fulfilled 
        # (i.e., the book is loaned to the member who reserved it), the reservation is deleted.
        if onReservation(self.accNo):
            if getEarliestReservation(self.accNo) == self.membershipID:
                deleteReservation(self.accNo, self.membershipID)
    
            else:
                self.top = tk.Toplevel()
                self.top.grab_set()
                self.top.geometry("600x600")
                mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
                label = tk.Label(self.top, text = "Book currently on Reservation.", font = self.navigator.headings_font)
                backButton = tk.Button(self.top, text = "Back to Borrow Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
                mainLabel.pack(ipady = 120)
                label.pack()
                backButton.pack(side = "bottom")
                return

        # borrow success page
        borrowBook(self.accNo, self.membershipID)
        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")
        mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
        label = tk.Label(self.top, text = "Book Successfully Loaned", font = self.navigator.headings_font)
        backButton = tk.Button(self.top, text = "Back to Borrow Function", command = self.close_popup, width = 60, height = 5, highlightbackground = '#FFAAA6')
        mainLabel.pack(ipady = 120)
        label.pack()
        backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()
    
class ReturnBookPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.accNo = None
        self.date = None
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        topLabel = tk.Label(frame1, text = "To Return a Book, Please Enter Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        
        def getAccessionNum(acc):
            acc = entryBox1.get()
            self.accNo = acc

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Accession Number :", width = 16, height = 5, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getAccessionNum)
        entryBox1.pack(side = 'left')
        frame2a.pack()

        def getReturnDate(date):
            date = entryBox2.get()
            self.date = date

        frame2a = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2a, text = "Return Date :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2a, width = 30)
        entryBox2.bind("<Return>", getReturnDate)
        entryBox2.pack(side = 'left')
        frame2a.pack()
        
        frame2 = tk.Frame(self)
        returnButton = tk.Button(frame2, text= "Return Book", width= 60, height = 5, command= self.confirmation_page, highlightbackground = '#A8E6CE')
        returnButton.config(font = (navigator.headings_font, 14))

        LoanMenuButton = tk.Button(frame2, text= "Back to Loans Menu", width= 60, height = 5, command = lambda: navigator.show_frame("LoansPage"), highlightbackground = '#FFAAA6')
        LoanMenuButton.config(font = (navigator.headings_font, 14))
        returnButton.pack(side = 'left')
        LoanMenuButton.pack(side = 'left')
        frame2.pack(pady = 100)
        
    def confirmation_page(self):
        # error popup - book does not exist 
        if not bookExists(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Return Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - book not on loan
        if not onLoan(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book not on loan.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Return Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - incorrect date format
        if not validDate(self.date):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Invalid date format. Please enter the date in the format DD/MM/YYYY.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Return Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")
        mainLabel = tk.Label(self.top, text = "Confirm Return\nDetails To Be Correct", font = (self.navigator.main_title_font, 40, font.BOLD))

        acc, title, _, _, _, idx, borrowdate = getBookInfo(self.accNo)
        _, fname, _, _, _ = getMemberInfo(idx)

        acc = tk.Label(self.top, text = "Accession Number : " + self.accNo, font = self.navigator.headings_font)
        title = tk.Label(self.top, text = "Book Title : " + title, font = self.navigator.headings_font)
        idx = tk.Label(self.top, text = "Membership ID : " + idx, font = self.navigator.headings_font)
        name = tk.Label(self.top, text = "Member Name : " + fname, font = self.navigator.headings_font)
        returnDate = tk.Label(self.top, text = "Return Date : " + self.date, font = self.navigator.headings_font)
        fine = tk.Label(self.top, text = "Fine : $" + str(calculateFine(self.accNo, self.date)), font = self.navigator.headings_font)
        confirmPayment = tk.Button(self.top, text = "Confirm Return", font = self.navigator.headings_font, command = self.confirm_return, width = 24, height = 3, highlightbackground = '#A8E6CE')
        goback = tk.Button(self.top, text = "Back to Return Function", font = self.navigator.headings_font, command = self.close_popup, width = 24, height = 3, highlightbackground = '#FFAAA6')
        
        mainLabel.pack()
        acc.pack(ipady = 20)
        title.pack(ipady = 20)
        idx.pack(ipady = 20)
        name.pack(ipady = 20)
        returnDate.pack(ipady = 20)
        fine.pack(ipady = 20)
        confirmPayment.pack(side = "left", fill = "x", expand=True)
        goback.pack(side = "left", fill = "x", expand=True)

    def confirm_return(self):
        self.top.grab_release()
        self.top.destroy()
        
        amt = calculateFine(self.accNo, self.date)
        _, _, _, _, _, idx, _ = getBookInfo(self.accNo)

        # error - return book but late 
        if amt > 0:
            return_date = dt.datetime.strptime(self.date, '%d/%m/%Y').date()
            createFine(idx, return_date, amt)
            returnBook(self.accNo)
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = "Book returned successfully but has fines.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Return Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")
            
        # return success page
        else:
            returnBook(self.accNo)
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
            label = tk.Label(self.top, text = "Book Successfully Returned", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Return Function", command = self.close_popup, width = 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class ReservationsPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator

        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame2a = tk.Frame(frame2)
        frame2a.pack(side = 'left')
        frame2b = tk.Frame(frame2)
        frame2b.pack(side = 'left', fill='both')
        frame2c = tk.Frame(frame2)
        frame2c.pack(side = 'left', fill='both')
        frame3 = tk.Frame(self)
        frame3.pack(fill='both')
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Select one of the options below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        "Frame 2"
        reservationPhoto = Image.open("images/booking.png").resize((400,400))
        reservationPhoto = ImageTk.PhotoImage(reservationPhoto)
        reservationIcon = Label(frame2a, text = "Reservation", compound = "top", image = reservationPhoto, font = navigator.headings_font)
        reservationIcon.pack(side = "left")
        reservationIcon.image = reservationPhoto
        
        reserveABook = tk.Button(frame2b, text = "Reserve A Book", command = lambda: navigator.show_frame("BookReservationPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE', width = 30)
        reservationCancellation = tk.Button(frame2b, text = "Cancel Reservation", command = lambda: navigator.show_frame("BookCancellationPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE', width = 30)

        reserveABook.pack(side = "top", fill = "both", expand= True, ipadx = 150)
        reservationCancellation.pack(side = "top", fill = "both", expand= True)
        
        "Frame 3"
        emptySpace = tk.Label(frame3, background= "#e6f9ff")
        mainMenuButton = tk.Button(frame3, text= "Back to Main Menu", command = lambda: navigator.show_frame("StartPage"), pady = 40, relief= tk.SUNKEN, highlightbackground = '#FFAAA6', font = navigator.headings_font2)
        emptySpace.pack(fill = 'x', ipady= 40)
        mainMenuButton.pack(fill= 'x')
        
        reserveABookText = tk.Label(frame2c, text = "Reserve A Book", font = self.navigator.headings_font2, bg = '#ebf9f4')
        reservationCancellationText = tk.Label(frame2c, text = "Reservation Cancellation", font = self.navigator.headings_font2, bg = '#ebf9f4')

        reserveABookText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        reservationCancellationText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)

class BookReservationPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.accNo = None
        self.membershipID = None
        self.reserveDate = None

        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()

        "Frame 1"
        topLabel = tk.Label(frame1, text = "To Reserve a Book, Please Enter Required Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        "Frame 2"
        def getAccessionNum(accNo):
            accNo = entryBox1.get()
            self.accNo = accNo

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Accession Number:", width = 16, height = 4, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getAccessionNum)
        entryBox1.pack(side = 'left')
        frame2a.pack()

        def getMembershipID(ID):
            ID = entryBox2.get()
            self.membershipID = ID

        frame2b = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2b, text = "Membership ID:", width = 16, height = 4, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2b, width = 30)
        entryBox2.bind("<Return>", getMembershipID)
        entryBox2.pack(side = 'left')
        frame2b.pack()

        def getReserveDate(date):
            date = entryBox3.get()
            self.reserveDate = date

        frame2c = tk.Frame(frame2)
        entryLabel3 = tk.Label(frame2c, text = "Reserve Date:", width = 16, height = 4, font = navigator.headings_font)
        entryLabel3.pack(side = 'left')
        entryBox3 = tk.Entry(frame2c, width = 30)
        entryBox3.bind("<Return>", getReserveDate)
        entryBox3.pack(side = 'left')
        frame2c.pack()

        "Frame 3"
        reserveBook = tk.Button(frame3, text= "Reserve Book", width= 60, height = 5, command = self.confirmation_page, highlightbackground = "#91DDF2")
        reserveBook.config(font = navigator.headings_font2)
        reserveBook.pack(side = 'left')

        reservationMenuButton = tk.Button(frame3, text= "Back to Reservations Menu", width= 60, height = 5, command = lambda: navigator.show_frame("ReservationsPage"), highlightbackground = '#FFAAA6')
        reservationMenuButton.config(font = navigator.headings_font2)
        reservationMenuButton.pack(side = 'left')
    
    def confirmation_page(self):
        # error popup - book not on loan
        if not onLoan(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book is not on Loan.", font = self.navigator.headings_font, height = 4) 
            getback = tk.Button(self.top, text = "To Loans Function", command = self.close_popup2,  width= 24, height = 5, highlightbackground = '#FFAAA6')
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 24, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            getback.pack(side = "left", fill = 'x', expand = True)
            backButton.pack(side = "right", fill = 'x', expand = True)
            return

        # error popup - reservation already exists
        if reservationExists(self.accNo, self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Reservation already exists.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - member does not exist 
        if not memberExists(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return
        
        # error popup - book does not exist 
        if not bookExists(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - incorrect date format
        if not validDate(self.reserveDate):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Invalid date format.\nPlease enter the date in the format DD/MM/YYYY.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Return Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")

        _, title, _, _, _, _, _ = getBookInfo(self.accNo)
        _, fname, _, _, _ = getMemberInfo(self.membershipID)

        mainLabel = tk.Label(self.top, text = "Confirm Reservation\nDetails To Be Correct", font = (self.navigator.main_title_font, 40, font.BOLD))
        accNoLabel = tk.Label(self.top, text = "Acession Number: " + self.accNo, font = self.navigator.headings_font)
        bookTitleLabel = tk.Label(self.top, text = "Book Title: " + title , font = self.navigator.headings_font)
        membershipIDLabel = tk.Label(self.top, text = "Membership ID: " + self.membershipID, font = self.navigator.headings_font)
        memberNameLabel = tk.Label(self.top, text = "Member Name: " + fname, font = self.navigator.headings_font)
        reserveDateLabel = tk.Label(self.top, text = "Reserve Date: " + self.reserveDate, font = self.navigator.headings_font)
        confirmButton = tk.Button(self.top, text = "Confirm Reservation", command = self.confirm_reservation, width = 30, height = 5, highlightbackground = '#A8E6CE')
        backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width = 30, height = 5, highlightbackground = '#FFAAA6')

        mainLabel.pack(ipady = 20)
        accNoLabel.pack(ipady = 20)
        bookTitleLabel.pack(ipady = 20)
        membershipIDLabel.pack(ipady = 20)
        memberNameLabel.pack(ipady = 20)
        reserveDateLabel.pack(ipady = 20)
        confirmButton.pack(side = "left", fill = "x", expand=True)
        backButton.pack(side = "left", fill = "x", expand=True)


    def confirm_reservation(self):
        self.top.grab_release()
        self.top.destroy()

        # error - no. of reservations > 2
        if numReservations(self.membershipID) >= 2:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = "Member currently has 2 Books on Reservation.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")
            return 

        # error - member has outstanding fine
        if hasFines(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = f"Member has Outstanding Fine of: ${paymentDue(self.membershipID)}.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#A8E6CE')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")
            return

        # reservation success page
        else:
            createReservation(self.accNo, self.membershipID, self.reserveDate)
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
            label = tk.Label(self.top, text = "Book Successfully Reserved", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

    def close_popup2(self):
        self.top.grab_release()
        self.top.destroy()
        self.navigator.show_frame("LoansPage")

class BookCancellationPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.accNo = None
        self.membershipID = None
        self.cancellationDate = None

        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()

        "Frame 1"
        topLabel = tk.Label(frame1, text = "To Cancel a Reservation, Please Enter Required Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        "Frame 2"
        def getAccessionNum(accNo):
            accNo = entryBox1.get()
            self.accNo = accNo

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Accession Number:", width = 16, height = 4, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getAccessionNum)
        entryBox1.pack(side = 'left')
        frame2a.pack()

        def getMembershipID(ID):
            ID = entryBox2.get()
            self.membershipID = ID

        frame2b = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2b, text = "Membership ID:", width = 16, height = 4, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2b, width = 30)
        entryBox2.bind("<Return>", getMembershipID)
        entryBox2.pack(side = 'left')
        frame2b.pack()

        def getCancellationDate(date):
            date = entryBox3.get()
            self.cancellationDate = date

        frame2c = tk.Frame(frame2)
        entryLabel3 = tk.Label(frame2c, text = "Cancel Date:", width = 16, height = 4, font = navigator.headings_font)
        entryLabel3.pack(side = 'left')
        entryBox3 = tk.Entry(frame2c, width = 30)
        entryBox3.bind("<Return>", getCancellationDate)
        entryBox3.pack(side = 'left')
        frame2c.pack()

        "Frame 3"
        cancelReservation = tk.Button(frame3, text= "Cancel Reservation", width= 60, height = 5, command = self.confirmation_page, highlightbackground = "#91DDF2")
        cancelReservation.config(font = navigator.headings_font2)
        cancelReservation.pack(side = 'left')

        reservationMenuButton = tk.Button(frame3, text= "Back to Reservations Menu", width= 60, height = 5, command = lambda: navigator.show_frame("ReservationsPage"), highlightbackground = '#FFAAA6')
        reservationMenuButton.config(font = navigator.headings_font2)
        reservationMenuButton.pack(side = 'left')
    
    def confirmation_page(self):
        # error popup - member does not exist 
        if not memberExists(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return
        
        # error popup - book does not exist 
        if not bookExists(self.accNo):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Book does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - incorrect date format
        if not validDate(self.cancellationDate):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Invalid date format. Please enter the date in the format DD/MM/YYYY.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")

        _, title, _, _, _, _, _ = getBookInfo(self.accNo)
        _, fname, _, _, _ = getMemberInfo(self.membershipID)

        mainLabel = tk.Label(self.top, text = "Confirm Cancellation\nDetails To Be Correct", font = self.navigator.main_title_font)
        accNoLabel = tk.Label(self.top, text = "Acession Number: " + self.accNo, font = self.navigator.headings_font)
        bookTitleLabel = tk.Label(self.top, text = "Book Title: " + title, font = self.navigator.headings_font)
        membershipIDLabel = tk.Label(self.top, text = "Membership ID: " + self.membershipID, font = self.navigator.headings_font)
        memberNameLabel = tk.Label(self.top, text = "Member Name: " + fname, font = self.navigator.headings_font)
        cancellationDateLabel = tk.Label(self.top, text = "Cancellation Date: " + self.cancellationDate, font = self.navigator.headings_font)
        confirmButton = tk.Button(self.top, text = "Confirm Cancellation", command = self.confirm_cancellation, width = 30, height = 5, highlightbackground = '#A8E6CE')
        backButton = tk.Button(self.top, text = "Back to Cancellation Function", command = self.close_popup, width = 30, height = 5, highlightbackground = '#FFAAA6')

        mainLabel.pack(ipady = 20)
        accNoLabel.pack(ipady = 20)
        bookTitleLabel.pack(ipady = 20)
        membershipIDLabel.pack(ipady = 20)
        memberNameLabel.pack(ipady = 20)
        cancellationDateLabel.pack(ipady = 20)
        confirmButton.pack(side = "left", fill = "x", expand=True)
        backButton.pack(side = "left", fill = "x", expand=True)

    def confirm_cancellation(self):
        self.top.grab_release()
        self.top.destroy()

        #reservation success page
        if reservationExists(self.accNo, self.membershipID):
            deleteReservation(self.accNo, self.membershipID)
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
            label = tk.Label(self.top, text = "Reservation Successfully Cancelled", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")

        # error - member has no such reservation
        else:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = "Member has no such reservation.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Reserve Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class FinesPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame2a = tk.Frame(frame2)
        frame2a.pack(side = 'left')
        frame2b = tk.Frame(frame2)
        frame2b.pack(side = 'left', fill='both')
        frame2c = tk.Frame(frame2)
        frame2c.pack(side = 'left', fill='both')
        frame3 = tk.Frame(self)
        frame3.pack(fill='both')
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Select one of the options below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        "Frame 2"
        finePhoto = Image.open("images/money.png").resize((400,400))
        finePhoto = ImageTk.PhotoImage(finePhoto)
        fineIcon = Label(frame2a, text = "Fines", compound = "top", image = finePhoto, font = navigator.headings_font)
        fineIcon.pack(side = "left")
        fineIcon.image = finePhoto
        
        payment = tk.Button(frame2b, text = "Payment", width = 30, command = lambda: navigator.show_frame("FinePaymentPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')
        payment.pack(side = "top", fill = "both", expand= True, ipadx = 150)
        
        "Frame 3"
        emptySpace = tk.Label(frame3, background= "#e6f9ff")
        mainMenuButton = tk.Button(frame3, text= "Back to Main Menu", command = lambda: navigator.show_frame("StartPage"), pady = 40,relief= tk.SUNKEN, highlightbackground = '#FFAAA6')
        mainMenuButton.config(font = (navigator.headings_font, 18))
        emptySpace.pack(fill = 'x', ipady= 40)
        mainMenuButton.pack(fill= 'x')
        
        paymentText = tk.Label(frame2c, text = "Fine Payment", font = self.navigator.headings_font2, bg = '#ebf9f4')

        paymentText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        
class FinePaymentPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.membershipID = None
        self.date = None
        self.amt = None     
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "To Pay a Fine, Please Enter Required Information Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        def getMembershipID(ID):
            ID = entryBox1.get()
            self.membershipID = ID

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Membership ID :", width = 15, height = 5, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getMembershipID)
        entryBox1.pack(side = 'left')
        frame2a.pack()

        def getPaymentDate(date):
            date = entryBox2.get()
            self.date = date

        frame2a = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2a, text = "Payment Date :", width = 16, height = 5, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2a, width = 30)
        entryBox2.bind("<Return>", getPaymentDate)
        entryBox2.pack(side = 'left')
        frame2a.pack()

        def getPaymentAmount(amt):
            amt = entryBox3.get()
            self.amt = amt
            
        frame2a = tk.Frame(frame2)
        entryLabel3 = tk.Label(frame2a, text = "Payment Amount :", width = 16, height = 5, font = navigator.headings_font)
        entryLabel3.pack(side = 'left')
        entryBox3 = tk.Entry(frame2a, width = 30)
        entryBox3.bind("<Return>", getPaymentAmount)
        entryBox3.pack(side = 'left')
        frame2a.pack()
        
        payFine = tk.Button(frame3, text= "Pay Fine", width= 60, height = 5, command = self.confirm_payment, highlightbackground = '#A8E6CE')
        payFine.config(font = (navigator.headings_font, 14))
        payFine.pack(side = 'left')

        fineMenuButton = tk.Button(frame3, text= "Back to Fines Menu", width= 60, height = 5, command = lambda: navigator.show_frame("FinesPage"), highlightbackground = '#FFAAA6')
        fineMenuButton.config(font = (navigator.headings_font, 14))
        fineMenuButton.pack(side = 'left')

    def confirm_payment(self):
        # error popup - member does not exist 
        if not memberExists(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Member does not exist.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Delete Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - incorrect date format
        if not validDate(self.date):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Invalid date format. Please enter the date in the format DD/MM/YYYY.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Return Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("600x600")
        mainLabel = tk.Label(self.top, text = "Please Confirm\nDetails To Be Correct", font = (self.navigator.main_title_font, 40, font.BOLD))

        idx, _, amt = getPaymentInfo(self.membershipID)
        amt = tk.Label(self.top, text = "Payment Due: $" + str(amt) + " (Exact Fee Only)", font = self.navigator.headings_font)
        idx = tk.Label(self.top, text = "Member ID : " + self.membershipID, font = self.navigator.headings_font)
        date = tk.Label(self.top, text = "Payment Date : " + self.date, font = self.navigator.headings_font)
        confirmPayment = tk.Button(self.top, text = "Confirm Payment", font = self.navigator.headings_font, command = self.make_payment, width = 24, height = 3, highlightbackground = '#A8E6CE')
        goback = tk.Button(self.top, text = "Back to Payment Function", font = self.navigator.headings_font, command = self.close_popup, width = 24, height = 3, highlightbackground = '#FFAAA6')

        mainLabel.pack(ipady = 20)
        amt.pack(ipady = 45)
        idx.pack(ipady = 45)
        date.pack(ipady = 45)
        confirmPayment.pack(side = "left", fill = "x", expand=True)
        goback.pack(side = "left", fill = "x", expand=True)

    def make_payment(self):
        self.top.grab_release()
        self.top.destroy()
        
        # error - no fine:
        if not hasFines(self.membershipID):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = "Member has no fine.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Payment Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")
            return

        # error popup - incorrect num format
        if not validNumber(self.amt):
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label2 = tk.Label(self.top, text = "Invalid fine amount. Please enter a number.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Payment Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label2.pack()
            backButton.pack(side = "bottom")
            return

        # fine success page
        if checkPaymentAmount(self.membershipID, int(self.amt)):
            payFine(self.membershipID, self.date, int(self.amt))
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Success!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "green")
            label = tk.Label(self.top, text = "Fine Successfully Paid", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Payment Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")

        # error - wrong payment amount
        else:
            self.top = tk.Toplevel()
            self.top.grab_set()
            self.top.geometry("600x600")
            mainLabel = tk.Label(self.top, text = "Error!", font = (self.navigator.main_title_font, 60, font.BOLD), foreground = "red")
            label = tk.Label(self.top, text = "Incorrect fine payment amount.", font = self.navigator.headings_font)
            backButton = tk.Button(self.top, text = "Back to Payment Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')
            mainLabel.pack(ipady = 120)
            label.pack()
            backButton.pack(side = "bottom")

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class ReportsPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame2a = tk.Frame(frame2)
        frame2a.pack(side = 'left')
        frame2b = tk.Frame(frame2)
        frame2b.pack(side = 'left', fill='both')
        frame2c = tk.Frame(frame2)
        frame2c.pack(side = 'left', fill='both')
        frame3 = tk.Frame(self)
        frame3.pack(fill='both')
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Select one of the options below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        "Frame 2"
        reportPhoto = Image.open("images/monitor.png").resize((400,400))
        reportPhoto = ImageTk.PhotoImage(reportPhoto)
        reportIcon = Label(frame2a, text = "Reports", compound = "top", image = reportPhoto, font = navigator.headings_font)
        reportIcon.pack(side = "left")
        reportIcon.image = reportPhoto
        
        bookSearch = tk.Button(frame2b, text = "Book Search", width = 30, command = lambda: navigator.show_frame("BookSearchPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')
        booksOnLoan = tk.Button(frame2b, text = "Books on Loan", width = 30, command = lambda: navigator.show_frame("BooksOnLoanPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')
        booksOnReservation = tk.Button(frame2b, text = "Books on Reservation", width = 30, command = lambda: navigator.show_frame("BooksOnReservationPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')
        outstandingFines = tk.Button(frame2b, text = "Outstanding Fines", width = 30, command = lambda: navigator.show_frame("OutstandingFinesPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')
        loansToMemberPage = tk.Button(frame2b, text = "Books on Loan to Member", width = 30, command = lambda: navigator.show_frame("LoansToMemberPage"), font = navigator.headings_font, highlightbackground = '#A8E6CE')

        bookSearch.pack(side = "top", fill = "both", expand= True, ipadx = 150)
        booksOnLoan.pack(side = "top", fill = "both", expand= True)
        booksOnReservation.pack(side = "top", fill = "both", expand= True)
        outstandingFines.pack(side = "top", fill = "both", expand= True)
        loansToMemberPage.pack(side = "top", fill = "both", expand= True)
        
        "Frame 3"
        emptySpace = tk.Label(frame3, background= "#e6f9ff")
        mainMenuButton = tk.Button(frame3, text= "Back to Main Menu", command = lambda: navigator.show_frame("StartPage"), pady = 40,relief= tk.SUNKEN, highlightbackground = '#FFAAA6')
        mainMenuButton.config(font = navigator.headings_font2)
        emptySpace.pack(fill = 'x', ipady= 40)
        mainMenuButton.pack(fill= 'x')
        
        bookSearchText = tk.Label(frame2c, text = "Search through Collection of Books", font = self.navigator.headings_font2, bg = '#ebf9f4')
        booksOnLoanText = tk.Label(frame2c, text = "Display Books on Loan", font = self.navigator.headings_font2 ,bg = '#ebf9f4')
        booksOnReservationText = tk.Label(frame2c, text = "Display Books with Reservations", font = self.navigator.headings_font2 ,bg = '#ebf9f4')
        outstandingFinesText = tk.Label(frame2c, text = "Display All Members with Outstanding Fines", font = self.navigator.headings_font2 ,bg = '#ebf9f4')
        loansToMemberText = tk.Label(frame2c, text = "Display Books on Loan", font = self.navigator.headings_font2 ,bg = '#ebf9f4')

        bookSearchText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        booksOnLoanText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        booksOnReservationText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        outstandingFinesText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)
        loansToMemberText.pack(side = 'top', fill = 'both', expand = True, ipadx = 200, ipady = 20)

class BookSearchPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.title = None
        self.author = None
        self.isbn = None
        self.publisher = None
        self.year = None
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Search Based On One Of The Categories Below:", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        def getTitle(title):
            title = entryBox1.get()
            self.title = title

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Title :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getTitle)
        entryBox1.pack(side = 'left')
        frame2a.pack()      

        def getAuthor(author):
            author = entryBox2.get()
            self.author = author

        frame2a = tk.Frame(frame2)
        entryLabel2 = tk.Label(frame2a, text = "Authors :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel2.pack(side = 'left')
        entryBox2 = tk.Entry(frame2a, width = 30)
        entryBox2.bind("<Return>", getAuthor)
        entryBox2.pack(side = 'left')
        frame2a.pack()          

        def getISBN(isbn):
            isbn = entryBox3.get()
            self.isbn = isbn

        frame2a = tk.Frame(frame2)
        entryLabel3 = tk.Label(frame2a, text = "ISBN :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel3.pack(side = 'left')
        entryBox3 = tk.Entry(frame2a, width = 30)
        entryBox3.bind("<Return>", getISBN)
        entryBox3.pack(side = 'left')
        frame2a.pack()

        def getPublisher(publisher):
            publisher = entryBox4.get()
            self.publisher = publisher

        frame2a = tk.Frame(frame2)
        entryLabel4 = tk.Label(frame2a, text = "Publisher :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel4.pack(side = 'left')
        entryBox4 = tk.Entry(frame2a, width = 30)
        entryBox4.bind("<Return>", getPublisher)
        entryBox4.pack(side = 'left')
        frame2a.pack()
        
        def getPublicationYear(year):
            year = entryBox5.get()
            self.year = year

        frame2a = tk.Frame(frame2)
        entryLabel5 = tk.Label(frame2a, text = "Publication Year :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel5.pack(side = 'left')
        entryBox5 = tk.Entry(frame2a, width = 30)
        entryBox5.bind("<Return>", getPublicationYear)
        entryBox5.pack(side = 'left')
        frame2a.pack()

        searchBook = tk.Button(frame3, text= "Search Book", width= 60, height = 5, command = self.search_output, highlightbackground = '#A8E6CE')
        searchBook.config(font = navigator.headings_font)
        searchBook.pack(side = 'left')

        reportsMenuButton = tk.Button(frame3, text= "Back to Reports Menu", width= 60, height = 5, command = lambda: navigator.show_frame("ReportsPage"), highlightbackground = '#FFAAA6')
        reportsMenuButton.config(font = navigator.headings_font)
        reportsMenuButton.pack(side = 'left')
    
    def search_output(self):
        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("1200x600")

        frame1 = tk.Frame(self.top)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self.top)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self.top)
        frame3.pack()

        mainLabel = tk.Label(frame1, text = "Book Search Results", font = self.navigator.main_title_font)
        backButton = tk.Button(frame3, text = "Back to Search Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')

        tv = tk.ttk.Treeview(frame2)

        df = self.get_dataframe() 

        tv["column"] = list(df.columns)
        tv["show"] = "headings"

        for column in tv["column"]:
            tv.heading(column, text = column)

        df_rows = df.to_numpy().tolist()
        for i in range(len(df_rows)):
            row = df_rows[i]
            tv.insert("", "end", values = row, tags = ('odd',) if i % 2 == 1 else ('even',))

        tv.tag_configure('odd', background='#E8E8E8')
        tv.tag_configure('even', background='#DFDFDF')
        mainLabel.pack()
        tv.pack(ipady = 100)
        backButton.pack(side = "bottom", pady= 20)

    def get_dataframe(self):
        return bookSearch(self.title, self.author, self.isbn, self.publisher, self.year)

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

class BooksOnLoanPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both', ipady = 150)
        frame2a = tk.Frame(frame2)
        frame2a.pack()
        frame2b = tk.Frame(frame2)
        frame2b.pack()
        frame3 = tk.Frame(self)
        frame3.pack()
        
        topLabel = tk.Label(frame1, text = "Books on Loan Report", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        tv = tk.ttk.Treeview(frame2a)
        tv.pack()
        refreshButton = tk.Button(frame2b, text = "Refresh", command = lambda: self.get_table(tv))
        refreshButton.pack()
        
        reportsMenuButton = tk.Button(frame3, text= "Back to Reports Menu", width= 60, height = 5, command = lambda: navigator.show_frame("ReportsPage"), highlightbackground = '#FFAAA6')
        reportsMenuButton.config(font = navigator.headings_font)
        reportsMenuButton.pack(side = 'left')

    def get_table(self, tv):
        
        tv.delete(*tv.get_children())
        df = self.get_dataframe() 

        tv["column"] = list(df.columns)
        tv["show"] = "headings"

        for column in tv["column"]:
            tv.heading(column, text = column)

        df_rows = df.to_numpy().tolist()
        for i in range(len(df_rows)):
            row = df_rows[i]
            tv.insert("", "end", values = row, tags = ('odd',) if i % 2 == 1 else ('even',))

        tv.tag_configure('odd', background='#E8E8E8')
        tv.tag_configure('even', background='#DFDFDF')
        

    def get_dataframe(self):
        return displayBookLoans()

class BooksOnReservationPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both', ipady = 150)
        frame2a = tk.Frame(frame2)
        frame2a.pack()
        frame2b = tk.Frame(frame2)
        frame2b.pack()
        frame3 = tk.Frame(self)
        frame3.pack()
        
        topLabel = tk.Label(frame1, text = "Books on Reservation Report", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        tv = tk.ttk.Treeview(frame2a)        
        tv.pack()
        refreshButton = tk.Button(frame2b, text = "Refresh", command = lambda: self.get_table(tv))
        refreshButton.pack()

        reportsMenuButton = tk.Button(frame3, text= "Back to Reports Menu", width= 60, height = 5, command = lambda: navigator.show_frame("ReportsPage"), highlightbackground = '#FFAAA6')
        reportsMenuButton.config(font = navigator.headings_font)
        reportsMenuButton.pack(side = 'left')
    
    def get_table(self, tv):
        
        tv.delete(*tv.get_children())
        df = self.get_dataframe() 

        tv["column"] = list(df.columns)
        tv["show"] = "headings"

        for column in tv["column"]:
            tv.heading(column, text = column)

        df_rows = df.to_numpy().tolist()
        for i in range(len(df_rows)):
            row = df_rows[i]
            tv.insert("", "end", values = row, tags = ('odd',) if i % 2 == 1 else ('even',))

        tv.tag_configure('odd', background='#E8E8E8')
        tv.tag_configure('even', background='#DFDFDF')

    def get_dataframe(self):
        return displayReservations()

class OutstandingFinesPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both', ipady = 150)
        frame2a = tk.Frame(frame2)
        frame2a.pack()
        frame2b = tk.Frame(frame2)
        frame2b.pack()
        frame3 = tk.Frame(self)
        frame3.pack()
        
        topLabel = tk.Label(frame1, text = "Members With Outstanding Fines", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)
        tv = tk.ttk.Treeview(frame2a)
        tv.pack()
        refreshButton = tk.Button(frame2b, text = "Refresh", command = lambda: self.get_table(tv))
        refreshButton.pack()

        reportsMenuButton = tk.Button(frame3, text= "Back to Reports Menu", width= 60, height = 5, command = lambda: navigator.show_frame("ReportsPage"), highlightbackground = '#FFAAA6')
        reportsMenuButton.config(font = navigator.headings_font)
        reportsMenuButton.pack(side = 'left')
    
    def get_table(self, tv):
        
        tv.delete(*tv.get_children())
        df = self.get_dataframe() 

        tv["column"] = list(df.columns)
        tv["show"] = "headings"

        for column in tv["column"]:
            tv.heading(column, text = column)

        df_rows = df.to_numpy().tolist()
        for i in range(len(df_rows)):
            row = df_rows[i]
            tv.insert("", "end", values = row, tags = ('odd',) if i % 2 == 1 else ('even',))

        tv.tag_configure('odd', background='#E8E8E8')
        tv.tag_configure('even', background='#DFDFDF')

    def get_dataframe(self):
        return displayMemberFines()

class LoansToMemberPage(tk.Frame):
    def __init__(self, parent, navigator):
        tk.Frame.__init__(self, parent)
        self.navigator = navigator
        self.membershipID = ""
        
        frame1 = tk.Frame(self)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self)
        frame3.pack()
        
        "Frame 1"
        topLabel = tk.Label(frame1, text = "Books On Loan To Member", relief = tk.RAISED, font=navigator.headings_font, background= "#e6f9ff")
        topLabel.pack(fill = "x", ipady = 50)

        def getMembershipID(ID):
            ID = entryBox1.get()
            self.membershipID = ID

        frame2a = tk.Frame(frame2)
        entryLabel1 = tk.Label(frame2a, text = "Membership ID :", width = 16, height = 4, font = navigator.headings_font)
        entryLabel1.pack(side = 'left')
        entryBox1 = tk.Entry(frame2a, width = 30)
        entryBox1.bind("<Return>", getMembershipID)
        entryBox1.pack(side = 'left')
        frame2a.pack()      

        searchLoan = tk.Button(frame3, text= "Search Book", width= 60, height = 5, command = self.search_output, highlightbackground = '#A8E6CE')
        searchLoan.config(font = navigator.headings_font)
        searchLoan.pack(side = 'left')

        reportsMenuButton = tk.Button(frame3, text= "Back to Reports Menu", width= 60, height = 5, command = lambda: navigator.show_frame("ReportsPage"), highlightbackground = '#FFAAA6')
        reportsMenuButton.config(font = navigator.headings_font)
        reportsMenuButton.pack(side = 'left')
    
    def search_output(self):
        self.top = tk.Toplevel()
        self.top.grab_set()
        self.top.geometry("1200x600")

        frame1 = tk.Frame(self.top)
        frame1.pack(fill='both')
        frame2 = tk.Frame(self.top)
        frame2.pack(fill='both')
        frame3 = tk.Frame(self.top)
        frame3.pack()

        mainLabel = tk.Label(frame1, text = "Books On Loan To Member", font = self.navigator.main_title_font)
        backButton = tk.Button(frame3, text = "Back to Search Function", command = self.close_popup, width= 60, height = 5, highlightbackground = '#FFAAA6')

        tv = tk.ttk.Treeview(frame2)

        df = self.get_dataframe() 

        tv["column"] = list(df.columns)
        tv["show"] = "headings"

        for column in tv["column"]:
            tv.heading(column, text = column)

        df_rows = df.to_numpy().tolist()
        for i in range(len(df_rows)):
            row = df_rows[i]
            tv.insert("", "end", values = row, tags = ('odd',) if i % 2 == 1 else ('even',))

        tv.tag_configure('odd', background='#E8E8E8')
        tv.tag_configure('even', background='#DFDFDF')
    
        mainLabel.pack()
        tv.pack(ipady = 100)
        backButton.pack(side = "bottom", pady= 20)

    def get_dataframe(self):
        return displayMemberLoans(self.membershipID)

    def close_popup(self):
        self.top.grab_release()
        self.top.destroy()

if __name__ == "__main__":
    als = ALS()
    als.mainloop()
