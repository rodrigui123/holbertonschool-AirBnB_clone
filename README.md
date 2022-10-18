
## **Python - Airbnb Clone**
![enter image description here](https://camo.githubusercontent.com/b1440bbfbf0f228b6ae82edb9cf1bdca2548131ec09f297971eed8112433cf06/68747470733a2f2f692e696d6775722e636f6d2f454b6267764b462e706e67)

## **Project Description:**
This proyect is the first part of a larger proyect, which is the Airbnb Clone. which consists of 6 projects, in which we will deal with each phase of creating this app, from back-end to front-end.


## Proyect Requirements:
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- A README.md file must exist.
-   All the files use the  `pycodestyle (version 2.7.)`  standard guidelines, including class and functions documentation
-   All tests are executed using the  `unittest`  module

## About this Proyect (The Console)
The model system; this part of the proyect contains all functions in order to **Create** ( creates new BaseModel), **Destroy** (destroys the Basemodel), **Show** (shows information of specific instance on Basemodel); **All** (Prints all string representation of all instances based or not on the class name) and **Update** (Updates an instance based on the class name and id by adding or updating attribute).

The **engine**, is based on a JSON file, it is able to handle the process of serialization and deserialization of an object. 
 

## How to use the interpreter
The console as the shell, can be run both interactive and non interactive mode. To run the console in a non interactive mode you can pipe any command into an execution of the console.py file at the command line.

To run it in interactive mode, you should run the console.py file by itself.

    Rodrigos-MacBook-Air:holbertonschool-AirBnB_clone rodrigolivera$ ./console.py

While you run that, a prompt ("(hbnb)") will be displayed for input to enter any of the named commands.

    rodrigolivera$ ./console.py
	(hbnb)

To exit the console type **quit** or the end of file signal (EOF) ctrl + d.

    rodrigolivera$ ./console.py
	(hbnb)quit
	Rodrigos-MacBook-Air:holbertonschool-AirBnB_clone 
	rodrigolivera$ 


## Object-attributes

BaseModel, is the only common base attribute because it is the base of the other object-attribute.
BaseModel: id, updated_at, created_at

### Specific object-attribute
 
**Review**  : place_id, user_id, text 

**User** : email, password, first_name, last_name
  
 **Place**  : city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
    
 **Amenity**  : name
    
 **State**  : name
    
 **City**  : state_id, name



## 	Contributors
Nahuel Alvarez: nahuel.alvarez1612@gmail.com
Rodrigo Olivera: jroliverasaavedra@gmail.com
