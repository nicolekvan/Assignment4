# Assignment4

This assignment is a journal/note taking platform that runs on your own
local desktop. You can record and manage your own notes, or share them
online. Updates were made to connect onto the ICS 32 Distributed Social
Network which is connected by a specific server and port address.

a3.py is where the code runs. It prints out the menu option with templates given
on how to utilize the tools. It takes a list of commands and puts the user in a
while loop to consistently retreive data.

ui.py handles the user inputs. Depending on the command, it will use the run()
or run_edits() methods that handle the different options and functions.

menu.py is a simple python text file intended to save space and keep the options
organized for user interface

ds_client.py is the client-side file that connects to the ICS 32 distributed server
The join_server function connects to the host address and returns True or False
depending on the result of the input

ds_protocol.py retreives the json strings and handles the values to parse
responses from the structure using named tuples

NEW UPDATES:

API Services: OpenWeather and LastFM
These are online web platforms that provide weather and music data 
that can be attained using an online web api provided from their website
Using these APIs, users can get pieces of data with transclusded messages
that are able to be posted on the online distributed server.

LastFM and OpenWeather are the child class of WebAPI which creates abstract methods
for the child class to use.