#!/usr/bin/env python3.5
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
print("Connection Successful")

print("Welcome to the mall")

database = client["mdatabase"]

# DATABASE LIST
# print(client.list_database_names())

# print("read from Database")

# print("delete database")

collection = database["customers"]

name = input("Enter your name to create an account: ")

mydict = { "name": "Peter", "address": "Lowstreet 27" }

print("update database")

x = collection.insert_one(mydict)

print(x.inserted_id)
# assigned_id = collection.insert_one({ "name" : name, "id" : 0})


isAdmin = False
adminPassword = "adminPassword"
userPassword = input("Enter the password for the Administrator: ")

if userPassword == adminPassword:
    isAdmin = True

client.close()