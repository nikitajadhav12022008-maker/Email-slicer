#python based email slicer
#input email
email = input("enter email:")
#splitting
username,domain = email.split("@")
#final step printing
print("Username:",username)
print("Domain",domain)

