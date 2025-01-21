import random as r  ###GENERATE RANDOM NUMBERS###
import conn


####GENERATOR STUDENTS ###


###LIST OF NAMES###
names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", 
    "Ethan", "Sophia", "Mason", "Isabella", "Lucas", 
    "Charlotte", "Amelia", "James", "Harper", "Benjamin", 
    "Mia", "William", "Ella", "Alexander", "Zoe"
]


surnames = [
    "Smith", "Johnson", "Taylor", "Anderson", "Brown", 
    "Williams", "Davis", "Miller", "Wilson", "Moore", 
    "Jackson", "Martin", "Lee", "Perez", "Harris", 
    "Clark", "Lewis", "Young", "Walker", "Allen"
]

###LIST OF SCHOOLS###
schools = [
    "Greenwood High School", "Maple Ridge Academy", "Oak Valley School", 
    "Silver Creek Institute", "Pinehill School", "Bluewater Academy", 
    "Riverstone High", "Sunset Valley School", "Eastwood Academy", 
    "Mountain Peak High School"
]
###LIST OF INFO OF THE STUDENTS###
Columns =  [
'Name', 
'Lastname', 
'School',
"Mathematics",
"Science",
"Language Arts",
"History",
"Physical Education",
"Email"
]


sql= '''INSERT INTO public.info_students
            ("name", lastname, school, maths, science, art, history, biology, email)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s); '''

###GENERATE A LIST OF STUDENTS###
def students(qty):

    list_students = []
    while qty != 0:
        list_students.append(
            [names[r.randint(0,19)],
                surnames[r.randint(0,19)],
                schools[r.randint(0,9)],
                round(r.uniform(r.randint(1,99),100),2),
                round(r.uniform(r.randint(1,99),100),2),
                round(r.uniform(r.randint(1,99),100),2),
                round(r.uniform(r.randint(1,99),100),2),
                round(r.uniform(r.randint(1,99),100),2)
            ])
        qty-= 1
    ###ADDING A EMAIL FOR EACH STUDENT###
    for student in list_students:
        student.append((student[0]+student[1]+'@yopmail.com').lower()) #YOPmail provides disposable and free email addresses.
        
    return list_students

###OUR START###
def start():

    ###MAX 3 ATTEMPTS TO INPUT A INTEGER NUMBER###
    attempts = 0

    while attempts < 3:
        students_number = input("Please, choose the number of students you want to generate: ")
        
        try:
            students_number = int(students_number)
            
            if students_number > 0:  
                new_students = students(students_number)
                return new_students
            else: 
                print("The number must be greater than 0. Please try again.")
                attempts += 1
        
        except ValueError:  
            print("Invalid input. Please enter a positive integer.")
            attempts += 1
        
        if attempts < 3:
            print(f"You have {3 - attempts} attempts left.")
        else:
            print("Too many invalid attempts. Exiting the program.")
            return  
    
try:
    # start funtion
    list_of_students = start()
    
    # DB CONECTION
    con = conn.connection()
    cursor = con.cursor()
    
    # execute sql +  list of students
    cursor.executemany(sql, list_of_students)
    con.commit()  # confirm the data.
    
    # close cursor and Connection.
    cursor.close()
    con.close()
    
    print("Data inserted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    

    
        