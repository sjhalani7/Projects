##### PASSWORD BANK PROJECT #######
#Modify, create, and read passwords
# {website:pw, google;}
#menu based: modify(), add(), delete(), display(), search(), generate()
# enter the password to acces the classified file.  


import random #for pw generator
import pickle
import string as st

s=st.printable ##string of all ascii characters
lis=[]          ## list of ascii characters
for ch in s:
    lis.append(ch)

def encrypt(password):  #encrypt function is used to encrypt the password before storing it in the binary file for 
                        # extra security
    s=password
    enc_pw=''
    for ch in s:
        for i in range(len(lis)):
            if ch==lis[i]:
                try:
                    enc_pw+=lis[i+1]
                except:
                    enc_pw+=lis[0] 
    return enc_pw

def decrypt(encr_pw):
    s2=encr_pw
    dec_pw=''
    for ch in s2:
        for i in range(len(lis)):
            if ch==lis[i]:
                 dec_pw+=lis[i-1]
    return dec_pw



def add(web, pw):
    while True:
        try:
            file=open('pw.dat','rb')
            D=pickle.load(file)  #dictionary that stores passwords by website
            file.close()
            break

        except:
            D={}
            break
    D1={}
    f=open("pw.dat",'wb')        #pw.dat is the file to store user entered passwords               
    
    D1[web]=encrypt(pw)          #encrypt() function is called to encrypt password and enter the passwor in the dictionary
    D.update(D1)
    pickle.dump(D,f)
    f.close()
    print(f"The password '{pw}' has been added to the database for the website '{web}'. ")


def display():              #to display all passwords 
    while True:
        try:
            file=open('pw.dat','rb')
            D=pickle.load(file)
            file.close()
            break
           
        except:
            D={}
            break
    d1={}
    for key in D.keys():
        act_pw=decrypt(D[key])              # act_pw is actual password
        d1[key]=act_pw
    print(d1)

def search(web):
    while True:
        try:
            file=open('pw.dat','rb')
            D=pickle.load(file)
            file.close()
            break
           
        except:
            D={}
            break
    d1={}
    for key in D.keys():
        act_pw=decrypt(D[key])              # act_pw is actual password
        d1[key]=act_pw
    if d1=={}:
        print("You have no passwords stored.")
    else: 
        print(f'The password stored for {web} is {d1[web]}')

def gen(leng):
    
    password=""
    for i in range(leng):
        char=st.ascii_letters+st.punctuation+st.digits
        password+=random.choice(char)
    return password

def delete():

    web=input("Enter the Website you want to delete: ")
    
    while True:
        try:
            file=open('pw.dat','rb')
            D=pickle.load(file)
            file.close()
            break
           
        except:
            D={}
            break
    del_pw=D[web]
    del(D[web])
    f=open("pw.dat",'wb')        #pw.dat is the file to store user entered passwords               

    pickle.dump(D,f)
    f.close()

    print(f"The password {decrypt(del_pw)} for {web} has been deleted.")

def modify(web,new_pw):
    while True:
        try:
            file=open('pw.dat','rb')
            D=pickle.load(file)
            file.close()
            break
           
        except:
            D={}
            break
    d1={}
    for key in D.keys():
        act_pw=decrypt(D[key])              # act_pw is actual password
        d1[key]=act_pw
        if key==web:
            ch=input(f'Confirmation required: Is {d1[key]} the password you want to modify? (Y/N): ')
            if ch.lower()=='y':
                d1[key]=new_pw
                print(f"Password updated. New password for {key} is {d1[key]} ")
    print(d1)
    dic={}
    for k in d1.keys():
        dic[k]=encrypt(d1[k])
    
    f=open("pw.dat",'wb')        #pw.dat is the file to store user entered passwords               
    pickle.dump(dic,f)
    f.close()

##---------------------------menu-----------------##

choice=0
print('''  \n\n\n                                               Welcome to the Password Bank Software                   

                                     

''')

try:
    f=open("master_pw.txt","r")
    master_pw=f.read()
    f.close()
    
except:
    master_pw=input('''\n\n                                              Welcome to the Password Bank Software                   
                                \n
        Since this is the first time using our software, kindly go through our brief initialization process to 
        start your storage. 

        You will require a master password everytime you want to access your existing password database. 
        Note: You will not be able to change the master password once added.

        Please enter the master password:   
                        ''')
    encry_mp=encrypt(master_pw)
    f=open("master_pw.txt","w")     
    f.write(encry_mp)
    f.close 

    f=open("master_pw.txt","r")
    master_pw=f.read()
    f.close()

pw_try=0  # number of times user can enter a wrong password-password tries

while pw_try<=2 and choice!=7:
    ch=input(" Please enter the Master Key to access your directory of passwords: ")

    if encrypt(ch)==master_pw: 
        print('''  \n\n\n
                                                            Welcome to the Password Bank Software                   
                                                \n  

''')
        choice=0
        while choice!=7:
            print('''                                       
            
                                                            1. Add a password.
                                                            2. Generate a password.
                                                            3. Search for a password.
                                                            4. Modify an existing password.
                                                            5. Delete an existing password.
                                                            6. Display all services
                                                            7. Exit

                    ''')
            choice=int(input('                               Enter your choice: '))
            
            if choice==1:
                web=input("Enter the name of the website: ")
                pw=input("Enter the password used in the website: ")
                add(web,pw)

            elif choice==2:
                web=input("Enter a website: ")
                leng=int(input("Enter the number of characters in the password: "))
                passw=gen(leng)
                print(passw)
                add(web,passw)
                print()
                
                
            elif choice==3: 
                web=input('Enter the website: ')
                search(web) 


            elif choice==4: 
                web=input("Enter the website: ")
                new_pw=input("Enter the updated password: ")
                modify(web, new_pw) 

            elif choice==5:
                delete()

            elif choice==6:
                display()


            elif choice==7:
                print("Thank You !!!!")
                break
    
    else:
        pw_try+=1
        print(" The password you entered is wrong...Please try again!!!! \n\n\n")

if pw_try>=2:
    print(" You entered the password wrong too many times!")
    print(" Program disabled...\n Please re-run the software to access the passwords.")
    
