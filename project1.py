# Project that stores the data of the students and allows to perform certain operations in mongoDB using pymongo library of Python

import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
database=client["StudentRecord"]
collection=database["EducationalRecord"]

while True:
    print("Choose what you want to do:\n 1.Show Record \n 2.Add Record \n 3.Search Data \n 4.Update Record \n 5.Delete Record \n 6.Exit")
    ch=int(input("Enter the choice in number based on above given list of operations: "))
    if ch==1:
            count=0
            cursor=collection.find({})
            for item in cursor:
                print(item)
                count+=1
            if count==0:
                print("Empty collection!!")
                

    elif ch==2:
        _id=int(input("Enter the roll number: "))
        name=input("Enter your name: ")
        phone=int(input("Enter your phone number: "))
        email_id=input("Enter the email id: ")
        dictionary={"_id":_id,"Name":name,"Phone_No":phone,"Email_id":email_id}
        collection.insert_one(dictionary)
        print("Record added (-:")
        print("\n \n")
        
    elif ch==3:
        ch1=int(input("Search by: RollNo(1) \n Name(2) \n PhoneNo(3) \n Email_Id(4)"))
        if ch1==2:
            name1=input("Enter the name to search: ")
            finding=collection.find({"Name":name1})
            for item in finding:
                print(item)
                print("\n \n \n")

        if ch1==1:
            roll1=input("Enter the rollNo to search: ")
            finding1=collection.find({"_id":roll1})
            for item in finding1:
                print(item)
                print("\n \n \n")
        if ch1==3:
            phone1=input("Enter the phone number to search: ")
            finding2=collection.find({"Phone_No":phone1})
            for item in finding2:
                print(item)
                print("\n \n")
                
        if ch1==4:
            email=input("Enter the email to search: ")
            finding3=collection.find({"Email_Id":email})
            for item in finding3:
                print(item)
                print("\n \n \n")

    elif ch==4:
        where=input("Enter the roll no to update the data of: ")
        while True:
            toChange=input("What to update: ")
            if toChange=="name" or toChange=="NAME" or toChange=="Name":
                newName=input("Enter the new name: ")
                prev={"Name":where}
                nextt={"$set":{"Name":newName}}
                collection.update_one(prev,nextt)
                print("Name Updated")
                break
            
            if toChange=="phoneno" or "PhoneNo" or "PHONENO":
                newNo=int(input("Enter the new phone number: "))
                prev={"PhoneNo":where}
                nextt={"$set":{"PhoneNo":newNo}}
                collection.update_one(prev,nextt)
                print("Phone Number Updated")
                break

            if toChange=="email_id" or "Email_Id" or "emailid":
                newMail=input("Enter the new mail ID: ")
                prev={"Email_Id":where}
                nextt={"$set":{"Email_Id":newMail}}
                collection.update_one(prev,nextt)
                

            else:
                print("Error! Please update existing data..")
            
    elif ch==5:
        nameDel=print("Enter roll no. of the student to delete the record: ")
        collection.delete_one({"Name":nameDel})
        print("The desired record has been deleted...")
        print("\n \n \n")


    else:
        print("Thank You for using our services (-:")
        break

    

                


