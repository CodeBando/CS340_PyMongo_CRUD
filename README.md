# CS340_PyMongo_CRUD
Python CRUD Module – Connect and run CRUD operations with MongoDB

### About the Project/Project Title
This README provides information about the Python Module, which facilitates CRUD operations on a MongoDB database for an animal shelter. This module allows users to interact with the database to manage animal records. 

### Motivation
The motivation behind this project is to create a Python module that simplifies the interaction with a MongoDB Database for managing animal records in an animal shelter. By providing a convenient interface for CRUD operations, the module aims to streamline the development of applications related to connecting with a MongoDB database and performing those CRUD operations. It will allow the user to access the database by utilizing the username and password to connect directly to the database, then allowing the user to perform the CRUD operations. <br><br>

This module was created to provide a simplistic interface that will abstract the complex interactions between the user and with MongoDB, allowing users to work with the database without needing to write extensive code for every operation, increasing productivity and consistency, and ensuring a structured approach to database operations.  This module also allows for reusability for any MongoDB connection through a simple and easy update to the module.

### Getting Started
To get started with the Python module, follow these simple steps: <br>
⦁	Clone the repository to your local machine<br>
⦁	Ensure you have Python 3.x installed<br>
⦁	Install the required packages (See installation):<br>
⦁	Initialize an instance of the ‘AnimalShelter’ class<br>
&emsp;⦁	You must provide the MongoDB Credentials for username and password<br>
&emsp;⦁	All other connection details are hard-coded<br>
⦁	Utilize methods of module to complete Create and Read operations on the MongoDB. Example executions can be found in the usage section below<br>

### Installation
In order to utilize the Python module, you will need the following tools installed:<br>
⦁	Python 3.x<br>
&emsp;⦁	Visit https://www.python.org/downloads/ to download<br>
⦁	PyMongo Library<br>
&emsp;⦁	You can install PyMongo using pip: pip install pymongo<br>
&emsp;&emsp;⦁	See https://pypi.org/project/pymongo/ for more information<br>

### Usage
Below are some examples of how to utilize the module to connect to the MongoDB database and utilize its CRUD functionality, as well as examples of the codebase. 

#### Code Example
This Module allows for the utilization of 5 key features, which can be accomplished as seen below: Connection to MongoDB, Create, Read, Update, and Delete.<br><br>

#### *Connect to AAC Database and the animals collection:* <br>
------------------------------------------
![1_Connect](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/5344f747-012f-4eee-807a-29e3e4652f99) <br>
The username and password for the user will be passed to the initialization method to connect to the MongoDB, as seen in the example above.<br><br>

If you wish to utilize this module for a different database, you will simply need to update the database connection details located in the __init__() method. <br>
**HOST** – provide the location of the MongoDB environment
**PORT** – the port location of the database
**DB** – the name of the database to access
**COL** – the collection that you wish to work with


#### *Create new document:*
------------------------------------------
![2_Create](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/823b15f2-a034-4680-8647-0ed723a7e018)
<br>
Utilizing the create method and passing Key/Value pairs as a dictionary, the module will create new documents within the AAC database in the animals collection. Validation is in place to ensure passed data is in the form of a dictionary to help protect the database’s data integrity. Include all key/value pairs required for the document insertion. <br><br>

#### *Read functionality:*
------------------------------------------
![3_Read1](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/84a88c2b-d15c-40fa-be00-b64fe93dd515)
<br>
Utilizing the read method and passing Key/Value pairs as a dictionary, you are able to perform queries on the database and collection. Will return a list of documents which can then be printed to view them. If no documents are found, an empty list is returned. There is validation in place to ensure that passed query data is in the form of a dictionary. Utilize as many Key/Value pairs as needed for the query.

#### *Update functionality:*
------------------------------------------
![1_Update1_Copy](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/17751215-f7dd-487c-8be8-173c4e107992)
<br>
Utilizing the update method and passing Key/Value pairs of documents that should be found along with the data that should update, you are able to perform queries on the database and collection to perform the desired data updates passed. This will return a value indicating the number of documents that were updated. There is validation in place to ensure that passed data is in the form of a dictionary. 

#### *Delete functionality:*
------------------------------------------
![5_DeleteTest](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/0cbeb6b5-aa93-443c-8606-bb0c18e724fb)
<br>
Utilizing the delete method and passing the Key/Value pair of the documents you would like to remove, you are able to delete documents from the database and collection. It will remove all documents that fit the query of key/value pairs passed through. It will return a value indicating the number of documents removed from the database. Validation is in place to ensure that Key/Value pairs in the form of a dictionary are passed through.

#### Tests
Each method in the module can be tested to ensure that it is correctly functioning. 
When connecting to the database, message will be displayed if connection was successful:<br>
![1_Connect](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/575c9a50-1631-429a-96c5-3088d3cc7cc7)<br>
<br>
When creating a new document and inserting it into the database, it will return True if successfully inserted and False if not:<br>
![2_Create](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/190393a5-f7d4-474f-acc8-536e9a5cf383)<br>
<br>
When utilizing the read method, it will return a list of documents. Print out returned list to confirm query was successful:<br>
![4_ReadMulti](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/107a6765-8558-4c60-a24e-149b0c59adb5)<br>
<br>
When utilizing the update method, it will return the number of documents that were updated. Print returned value to confirm number of documents updated:<br>
![1_Update1](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/f6347647-a46a-4b7d-9a79-7bffc9ff468b)<br>
<br>
When utilizing the delete method, it will return the number of documents that were removed. Print return value to confirm number of documents removed from database:<br>
![5_Delete1](https://github.com/CodeBando/CS340_PyMongo_CRUD/assets/90794751/47beb297-3f05-49db-8017-ad2b1cf35dea)<br>
<br>
<br>
#### Contact
Matthew Bandyk








