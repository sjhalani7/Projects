file1=open('accounts.txt','w')
file1.write('1001:Gautum Sarkar:50000:\n')
file1.close()

#create account file for first entry
file=open('A'+'1001','w')
file.write('0.00'+':'+'C'+':'+'50000'+':'+ '50000'+":"+'\n')
file.close()

def display():
   file1=open('accounts.txt','r')
   print(file1.read())
   file1.close()


def add_account(): #Assuming each account entered is new.
    file1=open('accounts.txt','r')
    lis=file1.readlines()
    file1.close()
    name=input('Enter Name of the Account Holder: ')
    op_bal=input('Enter the opening balance of the account: ')
    length=len(lis)
    prev_acc=lis[length-1]
    lis2=prev_acc.split(':')
    prev_accNum=int(lis2[0])
    new_accNum=str(prev_accNum+1)
    file1=open('accounts.txt','a')
    file1.write(new_accNum +':'+ name +':'+op_bal+':'+'\n')
    file1.close()
    file=open('A'+new_accNum,'w')
    file.write('0.00'+':'+'C'+':'+op_bal+':'+ op_bal+":"+'\n')
    file.close()
    print('Account added')
    print()


def transaction():
    file1=open('accounts.txt','r')
    lis=file1.readlines()
    file1.close()
    acc_num=input('Please enter your account number: ')
    length=len(lis)
    i=0
    
    for acc in lis:
        lis2=acc.split(':')
        if lis2[0]==acc_num:
            command=input('Would you like to deposit or withdraw? ')
            if command.lower()=='deposit':
                amt=float(input('Enter the amount you wish to deposit: '))
                upd_balance=str(float(lis2[2])+amt)
                upd_acc=(acc_num+':'+lis2[1]+':'+upd_balance+':'+'\n')
                lis.append(upd_acc)
                index=lis.index(acc)
                lis.pop(index)
                file1=open('accounts.txt','w')
                file1.writelines(lis)
                file1.close()

                file=open('A'+acc_num,'r')
                list1=file.readlines()
                file.close()
                last_acc=list1[len(list1)-1]
                list2=last_acc.split(':')
                prev_balance=float(lis2[2])
                new_bal=str(prev_balance+amt)
                upda_acc=(lis2[2]+':'+'C'+':'+str(amt)+':'+new_bal+':'+'\n')
                file=open('A'+acc_num,'a')
                file.write(upda_acc)
                file.close()
                print()
                break
                
            if command.lower()=='withdraw':
               amt=float(input('Enter the amount you wish to withdraw: '))
               if amt>float(lis2[2]):
                   print('The withdrawal amount exceeds the balance of the account.')
               elif amt<=float(lis2[2]):
                   upd_balance=str(float(lis2[2])-amt)
                   upd_acc=(acc_num+':'+lis2[1]+':'+upd_balance+':'+'\n')
                   lis.append(upd_acc)
                   index=lis.index(acc)
                   lis.pop(index)
                   file1=open('accounts.txt','w')
                   file1.writelines(lis)
                   file1.close()

                   file=open('A'+acc_num,'r')
                   list1=file.readlines()
                   file.close()
                   last_acc=list1[len(list1)-1]
                   list2=last_acc.split(':')
                   prev_balance=float(lis2[2])
                   new_bal=str(prev_balance-amt)
                   upda_acc=(lis2[2]+':'+'C'+':'+str(amt)+':'+new_bal+':'+'\n')
                   file=open('A'+acc_num,'a')
                   file.write(upda_acc)
                   file.close()
                   print('Account Updated. ')
                   print()
                   break
                   
        if (lis2[0]!=acc_num):
            i+=1
            if i<length:
               continue
            print('Account number Invalid. Account does not exist.')
    print('The transaction details of the '+lis2[1]+"'s bank account are as follows: ")        
    file=open('A'+acc_num,'r')
    print(file.read())
    file.close()  


########### MENU OF PROGRAM ##############
########### Main Method ##################
print('\n\n')
print('You have the following items in your bank system currently: ')
display()
while True:
    print('-------------------------------------------------------------------------------')
    print('Welcome to your bank system \n\n')
    print('Input the number corresponding with your choice\n')
    print('1. Add an account to the banking system')
    print('2. Make a Transaction.')
    print('3. Display the master file consisting of all accounts')
    print('4. Quit this program\n')
    choice=int(input("Enter your choice: "))
    print()
    
    if choice==1:
        add_account()
        command=input('Would you like to add more accounts to the system? ')
        while command.lower()=='yes':
            add_account()
            command=input('Would you like to add more accounts to the system? ')
            
        else:
            continue
        
    elif choice==2:
        transaction()
        command=input('Would you like to make more transactions? ')
        while command.lower()=='yes':
            transaction()
            command=input('Would you like to make more transactions? ')
            
        else:
            continue
    
        
    elif choice==3:
        display()
        

    elif choice==4:
        print('Thank you for using this program\n\n')
        print('Hope to see you soon!')
        break
    
    else:
        print('Choice invalid\n')
        print('Please enter a valid choice')

               


                


            
                        
                
