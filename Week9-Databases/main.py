# from https://www.py4e.com/html3/15-database

import sqlite3
import os

# Ensures the script finds the database in the same folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(SCRIPT_DIR, 'registration.sqlite')

def connect_db():
    """Connects to the SQLite database with error handling."""
    if not os.path.exists(DB_NAME):
        print(f"Error: {DB_NAME} not found! Ensure the .sqlite file is in the same folder.")
        return None
    return sqlite3.connect(DB_NAME)

def main():
    conn = connect_db()
    if not conn:
        input("\nPress Enter to exit...")
        return
        
    cursor = conn.cursor()
    print("                                                 ")
    print("           PROJECT 4 - REGISTRATION SYSTEM     \n")

    while True:
        print("\n      --- MAIN MENU ---")
        print("      1. Manage Faculty (Original Logic)")
        print("      2. Manage Students (Add/Update Major)")
        print("      3. Get Student Transcript (Complex Join)")
        print("      4. General Search (Any Table)")
        print("      5. View Full Table")
        print("      6. Exit")
        
        choice = input("\n      Select an option: ").upper()

        if choice == "1":
            action = input("\n      Enter 1 for List Faculty, 2 for Add Faculty, 3 for Update Faculty: ")
            if action == "1":
                cursor.execute('SELECT * FROM Faculty')
                print(f"\n{'ID':<5} {'NAME':<20} {'EMAIL'}")
                print("-" * 45)
                for row in cursor:
                    print(f"{row[0]:<5} {row[1]:<20} {row[2]}")
            elif action == "2":
                name = input("\n      Enter name: ")
                email = input("\n      Enter email: ")
                cursor.execute('INSERT INTO Faculty (Name, Email) VALUES (?, ?)', (name, email))
                conn.commit()
                print("Faculty record added.")
            elif action == "3":
                f_id = int(input("\n      Enter the Faculty ID to update: "))
                name = input("\n      Enter new name: ")
                email = input("\n      Enter new email: ")
                cursor.execute('UPDATE Faculty SET Name = ?, Email = ? WHERE ID = ?', (name, email, f_id))
                conn.commit()
                print("Faculty record updated.")

        elif choice == "2":
            action = input("\n      Enter 1 to Add Student, 2 to Update Student Major: ")
            if action == "1":
                name = input("\n      Enter Student Name: ")
                major = input("\n      Enter Major: ")
                cursor.execute('INSERT INTO Student (Name, Major) VALUES (?, ?)', (name, major))
                conn.commit()
                print("Student record added.")
            elif action == "2":
                s_id = input("\n      Enter Student ID: ")
                new_major = input("\n      Enter new Major: ")
                cursor.execute('UPDATE Student SET Major = ? WHERE ID = ?', (new_major, s_id))
                conn.commit()
                print(f"Major updated for Student ID {s_id}.")

        elif choice == "3":
            s_id = input("\n      Enter Student ID to generate transcript: ")
            # This query joins Student, Enrollment, Section, and Course tables
            query = """
                SELECT Course.Department, Course.Number, Course.Credits, Enrollment.Grade 
                FROM Enrollment
                INNER JOIN Student ON Student.ID = Enrollment.Student_ID
                INNER JOIN Section ON Section.ID = Enrollment.Section_ID
                INNER JOIN Course ON Course.ID = Section.Course_ID
                WHERE Enrollment.Student_ID = ?
            """
            cursor.execute(query, (s_id,))
            results = cursor.fetchall()
            
            if results:
                print(f"\n--- TRANSCRIPT FOR STUDENT {s_id} ---")
                print(f"{'DEPT':<10} {'NUMBER':<10} {'CREDITS':<10} {'GRADE'}")
                print("-" * 45)
                for r in results:
                    print(f"{r[0]:<10} {r[1]:<10} {r[2]:<10} {r[3]}")
            else:
                print("No enrollment records found for this student ID.")

        elif choice == "4":
            table = input("\n      Search in which table? (Student/Faculty/Course): ").capitalize()
            keyword = input(f"\n      Enter search term for {table} name/title: ")
            
            # Dynamically select column based on table
            col = "Name" if table != "Course" else "Description"
            
            try:
                cursor.execute(f"SELECT * FROM {table} WHERE {col} LIKE ?", (f'%{keyword}%',))
                rows = cursor.fetchall()
                print(f"\nSearch Results in {table}:")
                for row in rows: print(row)
            except sqlite3.Error as e:
                print(f"Search error: {e}")

        # View full table (Select Query)
        elif choice == "5":
            tbl = input("\n      Enter table name to view (Student, Faculty, Course, Section, Enrollment): ").capitalize()
            try:
                cursor.execute(f"SELECT * FROM {tbl}")
                rows = cursor.fetchall()
                print(f"\n--- {tbl.upper()} TABLE ---")
                for row in rows: print(row)
            except sqlite3.Error as e:
                print(f"Table error: {e}")

        elif choice == "6" or choice == "QUIT":
            print("Closing database connection...")
            break
        else:
            print("Invalid selection. Try again.")

    conn.close()
    input("\nProgram Finished. Press Enter to exit...")

# to get a transcript for a given student
# select course.Department, Course.Number, course.Credits, Enrollment.Grade from Enrollment
# inner join student on Student.id = Enrollment.Student_ID
# inner join section on Section.ID = Enrollment.Section_ID
# inner join course on Course.id = Section.Course_ID
# where Student_ID = 1"

if __name__ == "__main__":
    main()