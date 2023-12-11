# AirBnB Clone

## Overview
This project is the first full web application in the ALX-SE journey of a web developer.
This project is divided into 7 steps:

0. The Console :
	This is the first step in this big project. It focuses on:
	- Creating the parent class 'BaseModel' which takes care of the initialization, serialization and deserialization of the instances.
	- creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	- creating all classes used for the project : 'User', 'State', 'City', 'Place' ... that inherit from 'BaseModel'.
	- Creating the first abstracted storage engine of the project: File storage.

	After this step, we should have a command interpreter that manages the objects of our project:
	- Create a new object (ex: a new User or a new Place)
	- Retrieve an object from a file, a database etc…
	- Do operations on objects (count, compute stats, etc…)
	- Update attributes of an object
	- Destroy an object
1. Web Static:
	- updates are comming...

2. MySQL Storage:
	- updates are comming...

3. Deploy Static:
	- updates are comming...

4. Web Framework:
	- updates are comming...

5. RESTful API:
	- updates are comming...

6. Web Dynamic:
	- updates are comming...


## Features
The console has severale commands, each serves in a particular way:
1. create :
creates a new instance of a class passed as an argument.
2. show :
displays an instance of a class by its id.
3. all :
displays all the objects.
4. destroy :
deletes an object by its class name and id.
5. update :
updates an attribute of an instance (identifesd by its class name and id) with a new value.
## Usage
For the console:
- all command		:	`all [[class name]]`			OR	`[class_name].all()`
- create command	:	`create [class_name]`			OR	`[class_name].create()`
- show command 		: 	`show [class_name] [id]`		OR	`[class_name].show([id])`
- destroy command	:	`destroy [class_name] [id]`		OR	`[class_name].destroy([id])`
- update command	:	`update [class_name] [id] [attribute_name] [attribute_value]`
					OR	`[class_name].update([id], [attribute_name], [attribute_value])`
- quit command		:	`quit`
- EOF command		:	`EOF`
- help command		:	`help [[command]]`

## File Structure
This repository contains (other than README.md file and AUTHOR file),
- `model/` directory: it contains all classes used for the entire project.
- `tests/` directory : it contains all unit tests.
- `console.py` file : it is the entry point of our command interpreter.
- `models/base_model.py` file : it is the base class of all our models. It contains common elements:
	- attributes: `id`, `created_at` and `updated_at`
	- methods: `save()` and `to_json()`
- `models/engine` directory : it contains all storage classes (using the same prototype).