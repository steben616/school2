#Project 1:Basic School Administration tool
import csv

def write_info_csv(info_list):
    with open('student_info.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0:
        writer.writerow(["Name", "age", "Contact Number", "E-mail ID"])
        
        writer.writerow(info_list)

 if __name__=='__main__':       
condition = True

while(condition):
    student_info = input("Enter some student information in the following format (Name Age Contact_Number E-mail_ID): ")
    print("Entered Information: " + student_info)

    #split
    student_info_list = student_info.split(' ')
    print("Entered split up information is: " + str(student_info_list))

    print("\nThe entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nE-mail ID:{}"
          .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    write_info_csv(student_info_list)
    
    condition_check = input("Enter (yes/no) it you want to enter information for another student: ")
    if condition_check == "yes":
        condition = True
    elif condition_check == "no":
        condition = False
