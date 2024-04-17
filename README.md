# AIRBNB CLONE PROJECT (Version @)

## Project Description:

This is the first section of the AirBnB clone project where we worked on the backend of the project with the help of the cmd module in python.

Data (python objects) stored in files generated are stored in a json file and can be accessed with the json module in python

## Description of the command interpreter:

A command line interpreter allows the user to interact with a program using commands in the form of text lines. Our command line interpreter functions like the Bash shell except that it recognizes a limited number of commands that were solely defined and implemented for the purposes of the AirBnB website. This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:

	* create
	* show ( read )
	* count
	* update
	* destroy
And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:

	* Creating new objects (ex: a new User or a new Place)
	* Retrieving or reading an object from a file, a database etc…
	* executing several operations(count, compute stats, etc…)
	* Updating of an object
	* Destroying an object

## Console.py

## How it works

(To be Updated soon)

### Example:

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

or o

user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py

### Recognized Commands
	* do_show (read all Users)
	* do_destroy (deletes a User)
	* do_update (update a User)
	* do_count (counts all Users)
	* do_create (create a User)
	* do_quit (quits a command)
	* do_EOF (Ctel + D: exits the command)
	* empty_line (does nothing)

### Overview Of Classes Created

BaseModel: Parent class that defines all common attributes/methods for other classes. It handles Public attributes including:

	* id: created using uuid
	* created_at: using the date object
	* updated_at: using the date object and Public instance methods:
	* save(self): updates the public instance attribute updated_at with the current datetime to_dict(self): returns a dictionary containing all keys/values of dict of the Public instance

### User: Class that inherits from BaseModel. It handles Public Attributes including:
	* email: string object
	* password: string object
	* first_name: string object
	* last_name: string object

### State Public class attributes:
	* name: string - empty string

### City Public class attributes:
	* state_id: string - empty string
	* name: string - empty string
### Amenity Public class attributes:
	* name: string - empty string

### Place Public class attributes:
	* city_id: string - empty string
	* user_id: string - empty string
	* name: string - empty string
	* description: string
	* number_rooms: integer - 0
	* number_bathrooms: integer - 0
	* max_guest: integer - 0
	* price_by_night: integer - 0
	* latitude: float - 0.0
	* longitude: float - 0.0
	* amenity_ids: list of string

### Review Public class attributes:
	* place_id: string - empty string
	* user_id: string - empty string
	* text: string - empty string

### Overview of Unittest

Unit tests are essential for ensuring the correctness of code. Every 
possible edge cases have been covered by working with a wide range of 
students participating in this project. Unittest can be found in test/test_models 
directory, Handling test cases for:

	* BaseModel
	* Amenity
	* City
	* Place
	* Review
	* State
	* User
	* File storage (test/test_models/iengine)
