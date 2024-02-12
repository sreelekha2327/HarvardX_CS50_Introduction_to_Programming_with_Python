    # Marks Card Generator
    #### Video Demo: [Link](https://youtu.be/2b-uqtfMX9Q?si=-x2Ypn8YBNw3eycn)
    #### Description: This project is used to check whether student record exists or not. To add the new student record to the file. Modifying the existing record. Finally, to generate marks card in .pdf format by using the below functions.

    ##### **class Student()**

    Student is the user-defined data type. We call the class method Student.get by passing a hall Ticket number as an Argument. It then prompts for inputs of first name, last name, marks of english, mathematics, science, social studies, computer science marks of the student and returns instance object by passing all the above arguments. __str__ method if called returns all the instance variables in dict() format.

    ``` Python
    class Student:
    def __init__(self, hallTicket, firstName, lastName, english, mathematics, science, socialStudies, computerScience):
        self._hallTicket = hallTicket
        self.firstName = firstName
        self.lastName = lastName
        self.english = english
        self.mathematics = mathematics
        self.science = science
        self.socialStudies = socialStudies
        self.computerScience = computerScience

    def __str__(self):
        data = {
            "hallTicket": self.hallTicket,
            "fn": self.firstName,
            "ln": self.lastName,
            "eng": self.english,
            "maths": self.mathematics,
            "sci": self.science,
            "ss": self.socialStudies,
            "cs": self.computerScience,
        }
        return data

    @classmethod
    def get(cls, hallTicket):
        firstName = input("Enter first name : ")
        lastName = input("Enter last name : ")
        english = input("Enter English Marks : ")
        mathematics = input("Enter Mathematics Marks : ")
        science = input("Enter Science Marks : ")
        socialStudies = input("Enter Social Studies Marks : ")
        computerScience = input("Enter Computer Science Marks : ")
        return Student(hallTicket, firstName, lastName, english, mathematics, science, socialStudies, computerScience)
    ```

    The instance object is created only if valid inputs are passed to the instance variables, if not raises a Value Error.
    first name and last name - accepts [a-zA-z ] and should not be more than 15 characters
    marks of subject - accepts values from 0 to 100

    Getter and setter methods for first name instance variable.

    ``` Python
    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        name = self.name(firstName)
        if name != None :
            self._firstName = name
        else :
            print("Value Error : Invalid firstName" )
            raise ValueError("Invalid firstName")

    def name(self, name):
        if len(name) <= 15 :
            if matches := re.search(r"^([a-zA-Z ]+)$", name):
                name = matches.group(1)
                return name.title()
    ```

    Getter and setter methods for english instance variable.

    ``` Python
    @property
    def english(self):
        return self._english

    @english.setter
    def english(self, eng):
        marks = self.subject(eng)
        if marks != None :
            self._english = marks
        else :
            print("-------------------------------------------")
            print("Value Error : Invalid English Marks")
            print("-------------------------------------------")
            raise ValueError("Invalid English Marks")

    def subject(self, marks):
        if matches := re.search(r"^(100|[1-9]?[0-9])$", marks):
            return matches.group(1)
    ```

    ##### **check()**

    check is a user-defined function. It takes hall number as an argument and check in the records for the hall ticket number and returns the details of student in dict() format if present.

    ``` Python
    # Function that checks whether student data is in records or not
    def check(ID):
        with open("record.txt", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["hallTicket"] == ID:
                    return row
    ```

    ##### **upload()**

    upload is a user-defined function. It takes student data in dict() format as an argument and appends the data to the file.

    ``` Python
    def upload(**data):
    if not os.path.exists("record.txt"):
        with open("record.txt", "a") as file:
            write = csv.DictWriter(
                file,
                fieldnames=[
                    "hallTicket",
                    "fn",
                    "ln",
                    "eng",
                    "maths",
                    "sci",
                    "ss",
                    "cs",
                ],
            )
            write.writeheader()

    with open("record.txt", "a") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["hallTicket", "fn", "ln", "eng", "maths", "sci", "ss", "cs"],
        )
        writer.writerow(data)
    ```

    ##### **modify()**

    modify is a user-defined function. It takes data of the student to be modified in dict() format and changes the record in the file as required.

    ``` Python
    # Function that modifies the existing data
    def modify(**data):
        hallTicket = data["hallTicket"]
        print("------------------------")
        print("The Existing Data")
        print("------------------------")
        print(f'Hall Ticket No : {data["hallTicket"]}')
        print(f'First name : {data["fn"]}')
        print(f'Last name : {data["ln"]}')
        print(f'English : {data["eng"]}')
        print(f'Mathematics : {data["maths"]}')
        print(f'Science : {data["sci"]}')
        print(f'Social Studies : {data["ss"]}')
        print(f'Computer Science : {data["cs"]}')
        print("------------------------")
        print("Enter Modified Data")
        print("------------------------")
        try :
            student = Student.get(hallTicket)
        except ValueError :
            return False
        else :
            modified = student.__str__()
            deleteRow = pd.read_csv("record.txt", index_col="hallTicket")
            deleteRow = deleteRow.drop(hallTicket)
            deleteRow.to_csv("record.txt", index=True)
            upload(**modified)
            return True
    ```

    ##### **totalScore()**

    totalScore is a user-defined function. It takes student data in dict() format as an argument, calculate the total score by adding all the subect marks secured by student and grades the total score. It returns total score and grade in dict() format.

    ``` Python
    def totalScore(**data):
    total = (
        int(data["eng"])
        + int(data["maths"])
        + int(data["sci"])
        + int(data["ss"])
        + int(data["cs"])
    )
    if total > 425:
        grade = "A"
    elif 350 < total <= 425:
        grade = "B"
    elif 275 < total <= 350:
        grade = "C"
    elif 200 < total <= 275:
        grade = "D"
    else:
        grade = "E"
    return {"total": total, "grade": grade}
    ```

    ##### **subjectGrade()**

    subjectGrade is a user-defined function that grades the marks of the subject that is passed as an argument and returns grade.

    ``` Python
    def subjectGrade(marks):
        if marks > 90:
            grade = "A"
        elif 75 < marks <= 90:
            grade = "B"
        elif 55 < marks <= 75:
            grade = "C"
        elif 35 < marks <= 55:
            grade = "D"
        else:
            grade = "E"
        return grade
    ```

    ##### **marksCard()**

    marksCard is a user-defined function. It takes student data in dict() format as an arguments and generates the marks card in .pdf format in the name of hall ticket of the student.

    If required we can do changes to the class and institution names of the student in the below code.

    ```Python
    def marksCard(**data):
        TABLE_DATA = (
            ("Subject", "Maximum Marks", "Marks Scored", "Grade"),
            ("English", "100", data["eng"], subjectGrade(int(data["eng"]))),
            ("Mathematics", "100", data["maths"], subjectGrade(int(data["maths"]))),
            ("Science", "100", data["sci"], subjectGrade(int(data["sci"]))),
            ("Social Studies", "100", data["ss"], subjectGrade(int(data["ss"]))),
            ("Computer Science", "100", data["cs"], subjectGrade(int(data["cs"]))),
        )

        pdf = FPDF(orientation="P", unit="mm", format="A4")

        pdf.add_page()
        pdf.set_font("Times", style="B", size=50)
        pdf.cell(190, 50, "Marks Card", align="C")
        pdf.ln(40)
        pdf.set_font("helvetica", style="I", size=20)
        pdf.cell(190, 20, f'   Student Name : {data["ln"]} {data["fn"]}', align="L")
        pdf.ln(5)
        pdf.cell(190, 30, f'   Hall Ticket : {data["hallTicket"]}', align="L")
        pdf.ln(5)
        pdf.cell(190, 40, "   Class : X ", align="L")
        pdf.ln(5)
        pdf.cell(190, 50, "   Institution : XYZ English Medium High School", align="L")

        pdf.ln(40)

        pdf.set_font("Times", size=20)
        with pdf.table(
            width=150, col_widths=(60, 50, 40, 30), text_align="CENTER"
        ) as table:
            for data_row in TABLE_DATA:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)

        pdf.ln(10)
        pdf.set_font("helvetica", style="I", size=20)
        pdf.cell(190, 20, f'   Total : {data["total"]}/500', align="L")
        pdf.ln(5)
        pdf.cell(190, 30, f'   Grade : {data["grade"]}', align="L")
        pdf.output(f'{data["hallTicket"]}.pdf')
        print("---------------------------------------")
        print("\tMarks Card PDF generated")
        print("---------------------------------------")
    ```

    ##### **main**

    main function intially prompts the user to choose from the below options.

    1. Check whether student data exists or not"
    2. Add a new student record"
    3. Modify existing record"
    4. Print marks card"

    Later, it prompts for the user for the hall ticket number (accepts [a-zA-Z0-9]).

    It then executes code for the selected option.

    For 1st option below code is executed.

    ```Python
                if os.path.exists("record.txt") :
                    if check(hallTicket) != None:
                        print("Record exists")
                    else:
                        print("Record doesn't exists")
                else:
                    print("record.txt doesn't exists")
    ```

    For 2nd option below code is executed.

    ```Python
                if os.path.exists("record.txt") and check(hallTicket) != None :
                    print("Record exists")
                else:
                    student = Student.get(hallTicket)
                    data = student.__str__()
                    upload(**data)
                    print("---------------------------")
                    print("Data Uploaded Successfully")
                    print("---------------------------")
    ```

    For 3rd option below code is executed.

    ```Python
                if not os.path.exists("record.txt") :
                    print("record.txt doesn't exists")
                else :
                    data = check(hallTicket)
                    if data == None:
                        print("Record doesn't exists")
                    else:
                        if modify(**data) :
                            print("---------------------------")
                            print("Data Modified Successfully")
                            print("---------------------------")
    ```

    For 4th option below code is executed.

    ```Python
                if not os.path.exists("record.txt") :
                    print("record.txt doesn't exists")
                else :
                    data = check(hallTicket)
                    if data != None:
                        total = totalScore(**data)
                        data.update(total)
                        marksCard(**data)
                    else:
                        print("Record doesn't exists")
    ```

    Finally it asks for the user to exit the program or not.










