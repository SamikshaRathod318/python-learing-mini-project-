from db_config import connect


def load_data():
    connection = connect()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS videos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    `time` VARCHAR(100) NOT NULL
                )
                """
            )
            cursor.execute("SELECT name, `time` FROM videos ORDER BY id")
            return [
                {"name": name, "time": time}
                for name, time in cursor.fetchall()
            ]
        finally:
            cursor.close()
    finally:
        connection.close()


def save_data_helper(videos):
    connection = connect()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM videos")
            if videos:
                cursor.executemany(
                    "INSERT INTO videos (name, `time`) VALUES (%s, %s)",
                    [(video["name"], video["time"]) for video in videos],
                )
        finally:
            cursor.close()
        connection.commit()
    finally:
        connection.close()


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video}")
    print("\n")
    print("*" * 70)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)

    index = int(input("Enter the video number to update: "))

    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")

        videos[index - 1] = {
            "name": name,
            "time": time
        }

        save_data_helper(videos)
        print("Video updated successfully!")

    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)

    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("Video deleted successfully!")
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1.list all youtube video")
        print("2.add youtube video")
        print("3.update youtube video details")
        print("4.delete youtube video")
        print("5.exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()
