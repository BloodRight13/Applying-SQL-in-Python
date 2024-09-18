import sqlite3

#Task 1
def get_members_in_age_range(start_age, end_age):

    conn = sqlite3.connect('gym_database.db')

    c = conn.cursor()

    c.execute('''

        SELECT * FROM Members WHERE age BETWEEN ? AND ?

    ''', (start_age, end_age))

    members = c.fetchall()

    for member in members:

        print(member)

    conn.close()
