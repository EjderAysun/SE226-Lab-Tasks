import mysql.connector
from datetime import datetime

# connect to MySQL #
# Please do not forget to fill in the fields with question marks (???).
db = mysql.connector.connect(
    host="???",
    user="???",
    password="???",
)

cursorObj = db.cursor()

cursorObj.execute('DROP DATABASE IF EXISTS Marvel')
cursorObj.execute('CREATE DATABASE Marvel')

# Please do not forget to fill in the fields with question marks (???).
connection = mysql.connector.connect(
    host = "???",
    user = "???",
    password = "???",
    database = "???"
)

if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version:", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You are connected to database: ", record)

# task 2 #
try:
    mySql_Create_Table_Query = """CREATE TABLE Marvel (
                            Id int(4) NOT NULL,
                            Movie varchar(75) NOT NULL,
                            Date date NOT NULL,
                            Mcu_Phase varchar(10) NOT NULL
                            ) """
    result = cursor.execute(mySql_Create_Table_Query)
    print("Marvel Table created successfully.")

    cursor.execute("SHOW TABLES")
    for table_name in cursor:
        print(table_name)

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
# finally:
#      if connection.is_connected():
#          cursorObj.close()
#          connection.close()
#          print("MySQL connection is closed")

elements = list()

def getElementsFromTxt():
    with open("marvel.txt") as file:
        for line in file:
            elements.append(line.split())
    file.close()

# task 3 #
mySql_insert_query = """INSERT INTO Marvel (Id, Movie, Date, Mcu_Phase)
                        VALUES (%s, %s, %s, %s)
                        """
try:
    getElementsFromTxt()

    for line in elements:
        # print(line)
        if(len(line) == 5):
            line[1] += line[2]
            line.pop(2)
        line[2] = datetime.strptime(line[2], "%B%d,%Y").strftime("%Y-%m-%d")
    
    cursor.executemany(mySql_insert_query, elements)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Marvel table")

except mysql.connector.Error as error:
    print("Failed to insert record into Marvel table {}".format(error))

# task 4 & 5 & 6 & 7 #
import tkinter as tk
root = tk.Tk()
root.title("LAB#9")
root.geometry("800x300")
root.configure(bg="#E8F5FD")

text_box = tk.Text(root, width = 30, height = 7)
text_box.grid(row=0, column=1, padx=10, pady=10)

def get_all_elements_from_Database():
    try:
        mySql_select_all_elements_query = """SELECT * FROM Marvel"""
        cursor.execute(mySql_select_all_elements_query)
        return cursor.fetchall()
    except mysql.connector.Error as error:
        print("Failed to get record from Marvel table: {}".format(error))

def print_all_elements():
    record = get_all_elements_from_Database()
    text_box.delete(1.0, tk.END)
    output = ""
    for rec in record:
        for r in rec:
            output += " "
            output += str(r)
        output += "\n"    
    text_box.insert(tk.END, output)
    # text_box.update_idletasks()
    text_box.config(width = 55)
    text_box.config(height = 15)

list_all_button = tk.Button(root, text="LIST ALL MOVIES", command = print_all_elements)
list_all_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")

id_var = tk.StringVar(root)
id_var.set("Select ID")

def get_movie(id):
    try:
        mySql_select_movie_from_id_query = """SELECT * FROM Marvel WHERE id = %s"""
        cursor.execute(mySql_select_movie_from_id_query, (id,))
        return cursor.fetchall()
    except mysql.connector.Error as error:
        print("Failed to get record from Marvel table: {}".format(error))

def id_var_changed(*args):
    selected_id = int(id_var.get())
    if selected_id != "Select ID":
        text_box.delete(1.0, tk.END)
        record = get_movie(selected_id)
        print(record)
        output = """
ID:  %s
Movie:  %s
Date:  %s
Phase:  %s
        """ %(record[0][0], record[0][1], record[0][2], record[0][3])            
        text_box.insert(tk.END, output)
        # text_box.update_idletasks()
        text_box.config(width = len(record[0][1]) + 15)
        text_box.config(height = 7)

def get_id_list():
    try:
        mySql_select_all_ids_query = """SELECT id FROM Marvel"""
        cursor.execute(mySql_select_all_ids_query)
        rows = cursor.fetchall()
        id_list = [row[0] for row in rows]
        return id_list
    except mysql.connector.Error as error:
        print("Failed to get id list from Marvel table: {}".format(error))

def get_movie_name_list():
    try:
        mySql_select_all_ids_query = """SELECT movie FROM Marvel"""
        cursor.execute(mySql_select_all_ids_query)
        rows = cursor.fetchall()
        movie_name_list = [row[0] for row in rows]
        print(movie_name_list)
        return movie_name_list
    except mysql.connector.Error as error:
        print("Failed to get id list from Marvel table: {}".format(error))

id_var.trace("w", id_var_changed) # TRACE

is_window_open = False
def add_movie(*args):
    global is_window_open
    if is_window_open == False:
        is_window_open = True
        root2 = tk.Tk()
        root2.title("Add Movie Record")
        root2.geometry("650x100")
        root2.configure(bg="#E8F2FD")

        def ok():
            movie_record = text_field.get()
            delete_text_field()
            try:
                record = movie_record.split()
                print(record)
                id_list = get_id_list()
                movie_name_list = get_movie_name_list()
                if(len(record) == 4):
                    record[2] = datetime.strptime(record[2], "%B%d,%Y").strftime("%Y-%m-%d")
                    if (int(record[0]) in id_list):
                        text_field.insert(0, "Whether your format is correct or not, a record with this id already exists.")
                    elif (record[1] in movie_name_list):
                        text_field.insert(0, "Whether your format is correct or not, a record with this movie name already exists.")
                    else:
                        cursor.execute(mySql_insert_query, record)
                        connection.commit()
                        print(cursor.rowcount, "Record inserted successfully into Marvel table")
                        text_field.insert(0, "Record inserted successfully into Marvel table")
                        refresh_id_dropdown_list(get_id_list())
                else:
                    text_field.insert(0, "Please enter a valid format! (Example: 23 Spider-Man:FarFromHome July2,2019 Phase3)")
            except mysql.connector.Error as error:
                print("Failed to insert record into Marvel table {}".format(error))
                text_field.insert(0, "Please enter a valid format! (Example: 23 Spider-Man:FarFromHome July2,2019 Phase3)")

        def cancel():
            global is_window_open
            is_window_open = False
            root2.destroy()

        def delete_text_field():
            text_field.delete(0, tk.END)

        text_field = tk.Entry(root2, width=80)
        text_field.grid(row=0, column=4, padx=10, pady=10)

        ok_button = tk.Button(root2, text="OK", command = ok)
        ok_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        cancel_button = tk.Button(root2, text="Cancel", command = cancel)
        cancel_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

add_button = tk.Button(root, text="Add Movie", command = add_movie)
add_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

def refresh_id_dropdown_list(id_list):
    city_dropdown = tk.OptionMenu(root, id_var, *id_list)
    city_dropdown.grid(row=0, column=4, padx=10, pady=10, sticky="w")

id_list = get_id_list()
refresh_id_dropdown_list(id_list)

root.mainloop()

# task 8.a #
get_movie_name_list()

# task 8.b #
try:
    mySql_delete_movie_query = """DELETE FROM Marvel WHERE movie = %s"""
    cursor.execute(mySql_delete_movie_query, ("TheIncredibleHulk",))
    connection.commit()
    print("Movie record deleted successfully.")
    get_movie_name_list()
except mysql.connector.Error as error:
    print("Failed to get record from Marvel table: {}".format(error))

# task 8.c #
try:
    mySql_get_movies_by_phase = """SELECT movie FROM Marvel WHERE Mcu_Phase = %s"""
    cursor.execute(mySql_get_movies_by_phase, ("Phase2",))
    rows = cursor.fetchall()
    movie_list = [row[0] for row in rows]
    print(movie_list)
    print("Phase 2 movies selected successfully.")
except mysql.connector.Error as error:
    print("Failed to get record from Marvel table: {}".format(error))

def get_movie_date_list():
    try:
        mySql_select_all_dates_query = """SELECT movie, date FROM Marvel"""
        cursor.execute(mySql_select_all_dates_query)
        rows = cursor.fetchall()
        movie_date_list = [[row[0], row[1]] for row in rows]
        print(movie_date_list)
    except mysql.connector.Error as error:
        print("Failed to get id list from Marvel table: {}".format(error))

# task 8.d #
try:
    mySql_update_query = """UPDATE Marvel SET date = CONCAT(%s, SUBSTRING(date, 5)) WHERE movie = %s"""
    cursor.execute(mySql_update_query, (2019, "Thor:Ragnarok",))
    connection.commit()
    get_movie_date_list()
    print("Thor:Ragnarok's date is updated successfully.")
except mysql.connector.Error as error:
    print("Failed to get record from Marvel table: {}".format(error))

'''
Log:

Due to the nature of my task,
even if there are some misspellings or deviations from the given pattern in the provided text file \
(As an example, line 19 of the marvel.txt file has a space between 'Infinity' and 'War', which breaks the general order and requires an exception.),
I have made some unusual movements while extracting the data from the given marvel.txt \
file to avoid making any manual changes. (as an example, line [73-75]).

The 7 hour development process is over,
now I'm going to get some sleep and then I'll develop detailed comment lines :)

And please do not forget to fill in the fields with question marks (line [7-9] and [19-22]).
'''