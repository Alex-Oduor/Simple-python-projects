import json
import os

#function to add contact
def addcontact():
    first_name= input("Enter first name: ")   #prompt user to enter details
    second_name= input("Enter second name: ")
    fullname= first_name+' '+second_name
    fullname=fullname.title()
    detail = input("Enter contact[Email/telephone number]: ")

    filepath='contact.json'
    if os.path.exists(filepath):
       with open('contact.json','r') as f:
        contents=json.load(f)
        contents[fullname]=detail
       with open('temp.json','a')as tempfile:
        json.dump(contents, tempfile)

       os.remove('contact.json')
       os.rename('temp.json','contact.json')
    else:
       contact[fullname]=detail
       with open('contact.json','w')as file:
          json.dump(contact,file)
        

#function to delete  contact
def deletecontact():
   name= input("Enter fullname of the person you wish to delete: ")
   name= name.title()
   
   with open("contact.json",'r') as original_file:
      
     contents= json.load(original_file)
     if name in contents:
         found=1
         print("Contact found")
         del contents[name]

         with open("temp.json",'w') as temp_file:
            json.dump(contents, temp_file)
           
     else:
         found=0
         print("Contact not found")
   if found==1:
    os.remove('contact.json')
    os.rename('temp.json','contact.json')


#function to search contact
def searchcontact():
 name= input("Enter the full name of the person you wish to search: ")
 name= name.title()
 with open('contact.json','r') as file:
     content=json.load(file)
     if name in content:
        print("Contact found!\n "+content[name])
     else:
      print("Contact not found")
    
#funtion to show all keys(contact)
def showallcontacts():
   with open('contact.json','r') as file:
      content = file.load(file)
      print(list(content))


contact={}
print("***CONTACT LIST***\n")
print("1.Add contact.")
print("2.Delete contact.")
print("3.Search contact.")
print("4.Show All contacts.")
print("**************")

option=input("Choose one to continue:")
for choice in option:
     if choice=='1':
        addcontact()
        print("Added successfully")
        break
     elif choice == '2':
        deletecontact()
        break
     elif choice=='3':
        searchcontact()
        break
     elif choice=='4':
        print(sorted(contact))
        break
     else:
        print("Invalid option please try again")
        