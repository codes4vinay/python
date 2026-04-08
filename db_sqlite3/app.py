import sqlite3

conn = sqlite3.connect('yt_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name, time))
    conn.commit()

def update_video(name,time,id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name,time,id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name : ")
                time = input("Enter the video time: ")
                add_video(name,time)
            case '3':
                id = input("Enter video id : ")
                name = input("Enter the video name : ")
                time = input("Enter the video time: ")
                update_video(name, time, id)
            case '4':
                id = input("Enter video id : ")
                delete_video(id)
            case '5':
                break
            case _:
                print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()