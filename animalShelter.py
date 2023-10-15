#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:36:58 2023
CS-340 Client/Server Development
Python Module for CRUD Functionality
Version: 1.1
Update: 9/28/2023
 - Added Update and Delete functionality

@author: matthewbandyk_snhu
"""

from pymongo import MongoClient
#from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

# Initializing the MongoClient. This helps to 
# access the MongoDB databases and collections.
# This is hard-wired to use the aac database,  
# and the animals collection
# Definitions of the connection string variables are
# unique to the individual Apporto environment.
#
# You must edit the connection variables below to reflect
# your own instance of MongoDB!
#
# @param USER - Username for the user
#        PASS - Password for the user
    def __init__(self, USER, PASS):
        # Connection Variables for MongoDB
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31718
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Successfully Connected to Database")

# Create method to insert new document into the specified database and collection
# validates data is a dictionary (Key/Value Pairs)
# returns true if successfully created
# exception if insert_one is unsuccessful
# exception if data value is empty
#
# @params data - Key / Value pairs of document to be inserted  
    def create(self, data):
        # Validate data isn't empty
        if data is not None:
            # try / catch to insert new document
            try:
                # if data is a dictionary, make a new document and return true, if not, return false
                if isinstance(data, dict):
                    self.database.animals.insert_one(data)  # data should be dictionary
                    return True
                else:
                    return False
            except:
                print("Issue when creating document, no document created") 
        else:
            raise Exception("Nothing to save, because data parameter is empty") 

# Read method to implement a query on specified database and collection.
# validates query data is a dictionary (Key/Value Pairs)
# returns list of documents based on query data provided
# returns empty list if query finds nothing
# exception if error running the query or if query data provided is empty
#
# @param query - Key / Value pairs to be queried in the database 
    def read(self, query):
        if query:
            # try / catch running query with provided query data
            try:
                # if query is a dictionary, run query and return list of documents
                if isinstance(query, dict):
                    return list(self.collection.find(query))  # query should be dictionary
                else:
                    return list()
            except:
                print("Exception occurred when running query")
        else:
            raise ValueError("Nothing to find as the query parameter is empty")
            
# Update method to complete updates to existing documents in the database
# Validates query and data are dictionary values (Key/Value Pairs)
# If query is found, executes update many with data
# Returns number of modified documents
# Exception if error running the update
#
# @param query - Key / Value pairs to be queried and updated in database
#        data - Key / Value pairs of the new data to utilize
    def update(self, query, data):
        if query and data:
            # try / catch running query with provided data and updating docs
            try:
                if isinstance (query, dict) and isinstance (data, dict):
                    result = self.collection.update_many(query, {"$set": data})
                    return result.modified_count
                else:
                    print("Data values must be key/value pairs")
            except:
                print("Exception occurred when trying to update document/s")
        else:
            raise ValueError("either query or data or both are empty")
        
# Delete method to remove a document from the database
# Validates query data are dictionary values (Key/Value Pairs)
# Removes documents queried 
# Returns number of documents removed
#
# @params query - Key / Value pairs to be queried and removed from database
    def delete(self, query):
        if query:
            # try / catch running query with provided data, removing docs
            try:
                if isinstance(query, dict):
                    result = self.collection.delete_many(query)
                    return result.deleted_count
                else:
                    print ("Data values must be key/value pairs")
            except Exception as e:
                    print(f"Exception occurred when deleting documents: {e}")
        else:
            raise ValueError("Query parameter must be provided")