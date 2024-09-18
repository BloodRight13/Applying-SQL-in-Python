import sqlite3

# Task 1
def add_member(id, name, age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (?, ?, ?)", (id, name, age))
        
        conn.commit()
        print("Member added successfully.")
        
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. This ID might already exist.")
        
    finally:
        conn.close()

# Task 2
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)", 
                       (member_id, date, duration_minutes, calories_burned))
        
        conn.commit()
        print("Workout session added successfully.")
        
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. The member ID might be invalid.")
        
    finally:
        conn.close()

# Task 3
def update_member_age(member_id, new_age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Members WHERE id = ?", (member_id,))
        member = cursor.fetchone()
        
        if member:
            cursor.execute("UPDATE Members SET age = ? WHERE id = ?", (new_age, member_id))
            conn.commit()
            print("Member age updated successfully.")
        else:
            print("Member not found.")
        
    finally:
        conn.close()

# Task 4
def delete_workout_session(session_id):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM WorkoutSessions WHERE id = ?", (session_id,))
        
        if cursor.rowcount == 0:
            print("Session ID not found.")
        else:
            conn.commit()
            print("Workout session deleted successfully.")
        
    finally:
        conn.close()

delete_workout_session(1)
