donors_list = (['Ralph Anders', 5, 10], ['Andrei Wasinski', 101, 151, 75], ['Stalk Holmes', 40], ['Traci Johnston', 20], ['James Hendrick', 60], ['Angelica Kisel', 45, 25, 55.60])
#email sent out to donor
def email(donor, donation):
    print('')
    print(f'Hello, {donor}! Thank you very much for your generous donation of ${donation}! Your contribution is essential and will be well utilized.')

#function if user chooses to send a thank you email
def send_thank_you(donors_list):
    while True:
        x = 0
        print('')
        response = input('Type a Full Name: ')
        if response == 'list':
            for i in donors_list:
                print(i[0])
        elif response == 'quit':
            return(donors_list)
        else:
            print('')
            don_amt = input('What is the donation amount?: ')
            if don_amt == 'quit':
                return donors_list
            else:
                float(don_amt)
                count = 0
                for i in donors_list:
                    if i[0] == response:
                        donors_list[count].append(float(don_amt))
                        email(response, don_amt)
                        x = 2
                        break
                    count += 1
                if x != 2:
                    donors_list += ([response],)
                    donors_list[count].append(float(don_amt))
                    email(response, don_amt)
                return(donors_list)
                
#def send_thank_you():
#    while True:
#        resp = input("Please type 'list', 'quit' or name of the donor")
#        if resp == "list":
#            list_donors()
#        elif resp == "quit":
#            return
#        else:
#            new_donation = input("Please enter amount")
#            new_donor = False
#            for donor_name, donations in donors_list:
#                if donor_name == resp:
#                    donations.append(new_donation)
#                    break
#            else:
#                new_donor = True
#                donors_list.append((resp, [new_donation]))
#            
#            print_email(new_donor)  # passed bool for custom message
#            return

        
#function if user wants a report of donors and donations
def create_report(donors_list):
    print('')
    y = '|'
    print(f'Donor Name{y:>14} Total Given {y} Num Gifts {y} Average Gift')
    print('-' * 63)
    temp = []
    for i in donors_list:
        total = sum(i[1:])
        temp += [total]
    x = temp[:]
    for i in x:
        a = max(temp)
        temp.remove(max(temp))
        for item in donors_list:                
            if a == sum(item[1:]):
                gift = len(item[1:])
                average = (a / gift)
                print(f'{item[0]:<23} ${a:>11.2f} {gift:>11}  ${average:>11.2f}')
                break
   
#main function
if __name__ == "__main__":
    while True:
        print('')
        response = input('1: Send a Thank You \n2: Create a Report \n3: Quit \nChoose an Option: ')
        if response == '1':
            donors_list = send_thank_you(donors_list)
        elif response == '2':
            create_report(donors_list)
        elif response == '3' or response == 'quit':
            break
        else:
            continue
    
