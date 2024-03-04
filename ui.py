# Nicole Kwan
# nkwan3@uci.edu
# 76647093

from pathlib import Path
from Profile import *
from ds_client import send

def print_directory(args):
    path = Path(args[0])

    if path.exists() and path.is_dir():
        files = [file for file in path.iterdir() if file.is_file()]
        directories = [directory for directory in path.iterdir() if directory.is_dir()]

        for file in files:
            print(file)
        for directory in directories:
            print(directory)
            if "-r" in args:
                print_directory([str(directory)])

def output_directory(args):
    path = Path(args[0])

    if path.exists() and path.is_dir(): 
        files = [file for file in path.iterdir() if file.is_file()]
        directories = [directory for directory in path.iterdir() if directory.is_dir()]
        
        if "-f" in args:
            for file in files:
                print(file)
            if "-r" in args:
                for directory in directories:
                    output_directory([str(directory)] + args)

        if "-s" in args:
            search = args[-1]
            for file in files:
                if str(search) in str(file):
                    print(file)
            for directory in directories:
                if "-r" in args:
                    output_directory([str(directory)] + args)
        
        if "-e" in args:
            extension = args[-1]
            for file in files:
                if extension in str(file):
                    print(file)
            if "-r" in args:
                for directory in directories:
                    output_directory([str(directory)] + args)

# PART 2 | .dsu files

def create_file(args):
    try:
        new_file = args[-1] + ".dsu"
        path = Path(args[0]) / new_file
        path.touch()
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        bio = input("Enter bio: ").strip()

        profile = Profile(str(path), username, password)
        profile.bio = bio
        print("Great! We saved your profile, so you can come back to your journal in the future.")
        profile.save_profile(str(path))
        return str(path)
        
    except FileExistsError:
        return open_file(path)

def delete_file(args):
    path = Path(args[0])

    try:
        if path.exists():
            path.unlink()
            return print(f"{path} DELETED")
        else:
            print("ERROR")
    except Exception as e:
        return "ERROR"

def read_file(args):
    path = Path(args[0])

    if (path.stat().st_size == 0) is True:
        print("EMPTY")
    else:
        try:
            with open(path, "r") as file:
                content = file.read()
                print(content.strip())
        except Exception:
            print(f"ERROR")

def open_file(path):
    try:
        path = Path(path)
        if path.exists():
            profile = Profile()
            profile.load_profile(str(path))
            print(f"{path} successfully loaded!")
            return path
    except FileNotFoundError:
        print(f"File {path} not found.")
    except Exception as e:
        print(f"Error occurred while opening the file: {e}")

def edit_file(args):
    try:
        path = Path(args[0])
        print("DSU file successfully loaded.")
        if path.exists():
            profile = Profile()
            profile.load_profile(str(path))
            if '-usr' in args:
                username = args.index('-usr') + 1
                profile.username = args[username]
            if '-pwd' in args:
                password = args.index('-pwd') + 1
                profile.password = args[password]
            if '-bio' in args:
                bio = args.index('-bio') + 1
                profile.bio = args[bio]
            if '-addpost' in args:
                idx = args.index('-addpost') + 1
                new_post = args[idx:]
                message = (" ").join(new_post)
                profile.add_post(Post(message))
            if '-delpost' in args:
                idx = args.index('-delpost') + 1
                post_id = args[idx]
                if profile.del_post(int(post_id)):
                    print(f"Deleted post with ID {post_id}.")
                else:
                    print(f"Post with ID {post_id} not found.")

            profile.save_profile(str(path))
            print("Profile successfully updated.")            
        else:
            print(f"File {path} not found.")
    except Exception as e:
        print(f"Error occurred while editing the file: {e}")


def print_profile(args):
    try:
        path = args[0]
        with open(path, 'r') as file:
            data = json.load(file)
            if '-usr' in args:
                print(f"Username: {data['username']}")
            if '-pwd' in args:
                print(f"Password: {data['password']}")
            if '-bio' in args:
                print(f"Bio: {data['bio']}")
            if '-posts' in args:
                print("Posts:")
                for index, post in enumerate(data['_posts']):
                    print(f"{index}: {post}")
            if '-post' in args:
                post_id = int(args[args.index('-post') + 1])
                print(f"Post {post_id}: {data['_posts'][post_id]}")
            if '-all' in args:
                print("All data:")
                print(f"Username: {data['username']}")
                print(f"Password: {data['password']}")
                print(f"Bio: {data['bio']}")
                print("Posts:")
                for index, post in enumerate(data['_posts']):
                    print(f"{index}: {post}")
    except FileNotFoundError:
        print(f"File {path} not found.")
    except Exception as e:
        print(f"Error occurred while printing profile data: {e}")

def post_online(path, message, bio=""):
    try:
        profile = Profile()
        profile.load_profile(path)
        if profile.dsuserver == "":
            server = input("Enter server name: ")
        else:
            server = "168.235.86.101"
        send(server, 3021, profile.username, profile.password, message, bio=bio)

    except FileNotFoundError:
        print(f"File {path} not found.")



# RUN METHOD
current_file = ""

def run(command, args):
    global current_file
    if command.lower() == 'q':
        exit()

    elif command.lower() == 'l': 
        if ("-f" in args) or ("-s" in args) or ("-e" in args):
            output_directory(args)
        elif (args[-1] == "-r") or (len(args) == 1):
            print_directory(args)
        else:
            print("Error: Invalid Option.")

    elif command.lower() == "c":
        print(create_file(args))

    elif command.lower() == "d":
        if Path(args[0]).suffix.lower() != ".dsu":
            print("ERROR")
        else:
            delete_file(args)

    elif command.lower() == "r":
        if Path(args[0]).suffix.lower() != ".dsu":
            print("ERROR")
        elif len(args) < 0:
            print("ERROR")
        else:
            read_file(args)
    
    elif command.lower() == "o":
        current_file = open_file(args[0])

    else:
        print("Error: Please enter a valid command and path")

def run_edits(command, args):
    if command.lower() == "e":
        if current_file:
            args.insert(0, current_file)
            edit_file(args)
        else:
            print("No file is currently opened. Please open a file first.")
    elif command.lower() == "p":
        if current_file:
            args.insert(0, current_file)
            print_profile(args)
        else:
            print("No file is currently opened. Please open a file first.")
    elif command.lower() == "i":
        if current_file:
            if "-post" in args:
                while True:
                    message = input("Enter post: ").strip()
                    if message.lower() == "q":
                        break
                    if len(message) > 0:
                        post_online(current_file, message)
                    else:
                        print("Not enough characters. Please try again")
                        continue
            if "-bio" in args:
                ask = input("Would you like to enter a message? (y/n): ")
                if ask.lower() == "y":
                    message = input("Enter message: ")
                else:
                    message = ""
                bio = input("Enter new bio: ")
                post_online(current_file, message, bio)
                

        else:
            print("No file is currently opened. Please open a file first.")