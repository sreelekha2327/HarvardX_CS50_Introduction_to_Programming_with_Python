import re
import csv
from fpdf import FPDF
import os
import pandas as pd


# Define Class Student
class Student:
    def __init__(
        self,
        hallTicket,
        firstName,
        lastName,
        english,
        mathematics,
        science,
        socialStudies,
        computerScience,
    ):
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

    def name(self, name):
        if len(name) <= 15:
            if matches := re.search(r"^([a-zA-Z ]+)$", name):
                name = matches.group(1)
                return name.title()

    def subject(self, marks):
        if matches := re.search(r"^(100|[1-9]?[0-9])$", marks):
            return matches.group(1)

    @property
    def hallTicket(self):
        return self._hallTicket

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        name = self.name(firstName)
        if name != None:
            self._firstName = name
        else:
            print("Value Error : Invalid firstName")
            raise ValueError("Invalid firstName")

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        name = self.name(lastName)
        if name != None:
            self._lastName = name
        else:
            print("Value Error : Invalid lastName")
            raise ValueError("Invalid lastName")

    @property
    def english(self):
        return self._english

    @english.setter
    def english(self, eng):
        marks = self.subject(eng)
        if marks != None:
            self._english = marks
        else:
            print("-------------------------------------------")
            print("Value Error : Invalid English Marks")
            print("-------------------------------------------")
            raise ValueError("Invalid English Marks")

    @property
    def mathematics(self):
        return self._mathematics

    @mathematics.setter
    def mathematics(self, maths):
        marks = self.subject(maths)
        if marks != None:
            self._mathematics = marks
        else:
            print("-------------------------------------------")
            print("Value Error : Invalid Mathematics Marks")
            print("-------------------------------------------")
            raise ValueError("Invalid Mathematics Marks")

    @property
    def science(self):
        return self._science

    @science.setter
    def science(self, science):
        marks = self.subject(science)
        if marks != None:
            self._science = marks
        else:
            print("-------------------------------------------")
            print("Value Error : Invalid Science Marks")
            print("-------------------------------------------")
            raise ValueError("Invalid Science Marks")

    @property
    def socialStudies(self):
        return self._socialStudies

    @socialStudies.setter
    def socialStudies(self, ss):
        marks = self.subject(ss)
        if marks != None:
            self._socialStudies = marks
        else:
            print("-------------------------------------------")
            print("Value Error : Invalid Social Studies Marks")
            print("-------------------------------------------")
            raise ValueError("Invalid Social Studies Marks")

    @property
    def computerScience(self):
        return self._computerScience

    @computerScience.setter
    def computerScience(self, cs):
        marks = self.subject(cs)
        if marks != None:
            self._computerScience = marks
        else:
            print("-------------------------------------------")
            print("Value Error : Invalid Computer Science Marks")
            print("-------------------------------------------")
            raise ValueError("Invalid Computer Science Marks")

    @classmethod
    def get(cls, hallTicket):
        firstName = input("Enter first name : ")
        lastName = input("Enter last name : ")
        english = input("Enter English Marks : ")
        mathematics = input("Enter Mathematics Marks : ")
        science = input("Enter Science Marks : ")
        socialStudies = input("Enter Social Studies Marks : ")
        computerScience = input("Enter Computer Science Marks : ")
        return Student(
            hallTicket,
            firstName,
            lastName,
            english,
            mathematics,
            science,
            socialStudies,
            computerScience,
        )


# Function that checks whether student data is in records or not
def check(ID):
    with open("record.txt", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["hallTicket"] == ID:
                return row


# Append a record to a file
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
    try:
        student = Student.get(hallTicket)
    except ValueError:
        return False
    else:
        modified = student.__str__()
        deleteRow = pd.read_csv("record.txt", index_col="hallTicket")
        deleteRow = deleteRow.drop(hallTicket)
        deleteRow.to_csv("record.txt", index=True)
        upload(**modified)
        return True


# Function that calculates totol score and grade
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


# Function that grades the subject
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


# Function that prints marks Card
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


# Main Function
def main():
    while True:
        print("------------------------------------------------------")
        print("Available options : ")
        print("1. Check whether student data exists or not")
        print("2. Add a new student record")
        print("3. Modify existing record")
        print("4. Print marks card")
        print("------------------------------------------------------")
        while True:
            try:
                if choice := re.search(r"^([1-4])$", input("Choose one from above : ")):
                    break
            except ValueError:
                pass

        while True:
            if hallTicket := re.search(
                r"^([a-zA-Z0-9]+)$",
                input("Enter Hall Ticket number : "),
                re.IGNORECASE,
            ):
                hallTicket = hallTicket.group(1)
                hallTicket = hallTicket.upper()
                break

        match int(choice.group(1)):
            case 1:
                if os.path.exists("record.txt"):
                    if check(hallTicket) != None:
                        print("Record exists")
                    else:
                        print("Record doesn't exists")
                else:
                    print("record.txt doesn't exists")

            case 2:
                if os.path.exists("record.txt") and check(hallTicket) != None:
                    print("Record exists")
                else:
                    student = Student.get(hallTicket)
                    data = student.__str__()
                    upload(**data)
                    print("---------------------------")
                    print("Data Uploaded Successfully")
                    print("---------------------------")

            case 3:
                if not os.path.exists("record.txt"):
                    print("record.txt doesn't exists")
                else:
                    data = check(hallTicket)
                    if data == None:
                        print("Record doesn't exists")
                    else:
                        if modify(**data):
                            print("---------------------------")
                            print("Data Modified Successfully")
                            print("---------------------------")

            case 4:
                if not os.path.exists("record.txt"):
                    print("record.txt doesn't exists")
                else:
                    data = check(hallTicket)
                    if data != None:
                        total = totalScore(**data)
                        data.update(total)
                        marksCard(**data)
                    else:
                        print("Record doesn't exists")

        inp = input("Want to Exit (y|n) : ")
        if inp == "Y" or inp == "y":
            break


if __name__ == "__main__":
    main()
