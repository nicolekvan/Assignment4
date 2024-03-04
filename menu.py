# Nicole Kwan
# nkwan3@uci.edu
# 76647093

def print_menu():
    print("Welcome to the ICS 32 Journal File System!")
    print("Here are the commands with their available options:")
    print("""
          Q - Quit Program
          L - List All Files In Current Directory
            '-r': list all files in all directories
            '-f': list only files
            '-s': search specific file
            '-e': print file under specific extension

          .DSU FILES

          C - Create New .dsu File
            '-n': name .dsu file
          D - Delete .dsu File
          R - Read .dsu File Contents
          O - Open Existing .dsu File
          E - Edit New or Existing .dsu File
            '-addpost': add new post in journal
            '-delpost': delete post ID in journal
          P - Print Data in the DSU File Loaded by C or O command
            '-posts': print stored posts
            '-post': print specific post ID
            '-all': print all profile content
          E (Edit) or P (Print)
            '-usr': E/P stored profile username
            '-pwd': E/P stored profile password
            '-bio': E/P stored profile bio
          I - Post on the Internet
            'i -post': Post on ICS 32 Distributed Social
            'i -bio': Change bio on Distributed Social profile

          """)
    print("Format: COMMAND INPUT -OPTION INPUT")
    print("-----------------------------------")
