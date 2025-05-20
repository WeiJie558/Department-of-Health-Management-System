############################Below are login page#######################################################
import time
from datetime import datetime
import sys

now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d")

controller_ID_list = [['kj0604', '1234']]

#######################################Initial Creation######################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Only execute one time is enough!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""PPE = open('PPE.txt', 'w')
PPE.write("Item Name\tItem Code\tSupplier Code\tQuantity\n"
           "Head Cover\tHC\t\tC01\t\t100\n"
           "Face Shield\tFS\t\tC02\t\t100\n"
           "Mask\t\tMS\t\tC03\t\t100\n"
           "Gloves\t\tGL\t\tC04\t\t100\n"
           "Gown\t\tGW\t\tC02\t\t100\n"
           "Shoe Covers\tSC\t\tC03\t\t100")"""

"""supplier = open('Supplier.txt', 'w')
supplier.write("Supplier\tSupplier Code\tCountry\n"
           "Company A\tC01\t\tMalaysia\n"
           "Company B\tC02\t\tSingapore\n"
           "Company C\tC03\t\tThailand\n"
           "Company D\tC04\t\tIndonesia\n")"""

"""hospital = open('Hospital.txt', 'w')
hospital.write("Hospital_Name\tHospital_Code\tHC\tFS\tMS\tGL\tGW\tSC\n"
               "Hospital_A\tH01\t\t0\t0\t0\t0\t0\t0\n"
               "Hospital_B\tH02\t\t0\t0\t0\t0\t0\t0\n"
               "Hospital_C\tH03\t\t0\t0\t0\t0\t0\t0\n"
               "Hospital_D\tH04\t\t0\t0\t0\t0\t0\t0\n")"""
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Only execute one time is enough!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#######################################Initial Creation#####################################

################below are define login#################
def login():
    attempt = 0
    login_status = "denied"
    register_admin = "denied"

    while attempt < 3:
        login_ID = input("Please enter your ID: ")
        login_PW = input("Please enter your password: ")

        for num in controller_ID_list:
            if login_ID == num[0] and login_PW == num[1]:
                login_status = "granted"
                print("Logged in")
                register_admin = "granted"
                attempt = 0
                return login_status, register_admin

            elif login_ID and login_PW not in controller_ID_list:
                print("Incorrect ID or password. Please try again.")
                attempt += 1

        if attempt == 3:
            print("You had attempted 3 times. Please try again after 60 seconds.")
            time.sleep(60)
            attempt = 0

    return login_status, register_admin
######################################above are define login#####################################
#######################################below are define main page################################
def main_page():
    action = input("What action did you want to perform?\n"
                   "1. Check inventory quantity\n"
                   "2. Check hospital inventory quantity\n"
                   "3. Received inventory from supplier\n"
                   "4. Distribute inventory to hospital\n"
                   "5. Check distribution record\n"
                   "6. Check suppliers of inventory\n"
                   "7. Item Inventory Tracking\n"
                   "8. Monthly Report\n"
                   "Enter 'X' to exit the program\n").upper()
    if action == "X":
        print("Thank you for using our program!")
        sys.exit()
    return action
#######################################above are define main page#########################################
######################################below are define inventory access###################################
def inventory():
    file = open('PPE.txt', 'r')
    read = str(file.readlines())  # if juz read, print exactly the txt file
    # if readlines, print txt file in one line

    file = open('PPE.txt', 'r')
    read = file.readlines()

    first_row = read[1].split('\t')
    second_row = read[2].strip('\t')
    third_row = read[3].strip('\t')
    fourth_row = read[4].strip('\t')
    fifth_row = read[5].strip('\t')
    sixth_row = read[6].strip('\t')
    """column1 = first_row.split('\t')
    column2 = second_row.split('\t')
    column3 = third_row.split('\t')
    column4 = fourth_row.split('\t')
    column5 = fifth_row.split('\t')
    column6 = sixth_row.split('\t')"""

    while True:
        item_select = input("Which inventory you want to access?\n"
                            "1. Head Cover\n"
                            "2. Face Shield\n"
                            "3. Mask\n"
                            "4. GLoves\n"
                            "5. Gown\n"
                            "6. Shoe Covers\n"
                            "Enter 'X' to back to main page\n").upper()
        if item_select == "X":
            pickup()################################################################################################
            break

        if item_select == "1":
            print("These are the inventory details")
            print("Item Name: ", first_row[0])
            print("Item Code: ", first_row[1])
            print("Supplier Code: ", first_row[3])
            print("Quantity In Stock: ", first_row[-1], "boxes")
            time.sleep(3)


        elif item_select == "2":
            print("These are the inventory details")
            print("Item Name: ", second_row[0:11])
            print("Item Code: ", second_row[12:16])
            print("Supplier Code: ", second_row[16:21])
            print("Quantity In Stock: ", second_row[-4:-1], "boxes")
            time.sleep(3)

        elif item_select == "3":
            print("These are the inventory details")
            print("Item Name: ", third_row[0:4])
            print("Item Code: ", third_row[6:9])
            print("Supplier Code: ", third_row[10:13])
            print("Quantity In Stock: ", third_row[-4:-1], "boxes")
            time.sleep(3)

        elif item_select == "4":

            print("These are the inventory details")
            print("Item Name: ", fourth_row[0:5])
            print("Item Code: ", fourth_row[8:10])
            print("Supplier Code: ", fourth_row[12:15])
            print("Quantity In Stock: ", fourth_row[-4:-1], "boxes" )
            time.sleep(3)


        elif item_select == "5":
            print("These are the inventory details")
            print("Item Name: ", fifth_row[0:4])
            print("Item Code: ", fifth_row[6:8])
            print("Supplier Code: ", fifth_row[10:13])
            print("Quantity In Stock: ", fifth_row[-4:-1], "boxes")
            time.sleep(3)

        elif item_select == "6":
            print("These are the inventory details")
            print("Item Name: ", sixth_row[0:11])
            print("Item Code: ", sixth_row[12:15])
            print("Supplier Code: ", sixth_row[16:20])
            print("Quantity In Stock: ", sixth_row[-3:], "boxes")
            time.sleep(3)

    return read
######################################above are define inventory access############################################
######################################below are define ask hospital###############################################
def hospital():
    ask_hospital = input("Which hospital you want to access?\n"
                         "1. Hospital A\n"
                         "2. Hospital B\n"
                         "3. Hospital C\n"
                         "4. Hospital D\n"
                         "Enter 'X' to back to main page\n").upper()
    if ask_hospital == "X":
        pickup()################################################################################################
    return ask_hospital
##########################################above are define hospital#################################################
##########################################below are define hospital inventory######################################
def hospital_inventory():
    file = open('hospital.txt', 'r')
    read = file.readlines()  # if juz read, print exactly the txt file
                             # if readlines, print txt file in one line
    read_all = file.read()

    first_row = read[1].strip()
    second_row = read[2].strip()
    third_row = read[3].strip()
    fourth_row = read[4].strip()
    column1 = first_row.split("\t")
    column2 = second_row.split('\t')
    column3 = third_row.split('\t')
    column4 = fourth_row.split('\t')

    hospital_name = 0
    hospital_code = 1
    head_cover = 3
    face_shield = 4
    mask = 5
    gloves = 6
    gown = 7
    shoe_covers = -1

    hos_list = ["1", "2", "3", "4"]

    while True:
        ask_hospital = hospital()
        if ask_hospital == "X":
            pickup()############################################################################

        if ask_hospital in hos_list:
            while True:
                ask = input("What hospital inventory did you want to access?\n"
                            "1. Head Cover\n"
                            "2. Face Shield\n"
                            "3. Mask\n"
                            "4. Gloves\n"
                            "5. Gown\n"
                            "6. Shoe Covers\n"
                            "7. All inventory\n"
                            "Enter 'X' to back to choose hospital\n").upper()

                if ask == "X":
                    hospital()
                    break

                if ask_hospital == "1":
                    if ask == "1":
                        print("Head Cover: ", column1[head_cover], "boxes")
                        break

                    elif ask == "2":
                        print("Face Shield: ", column1[face_shield], "boxes")
                        break

                    elif ask == "3":
                        print("Mask: ", column1[mask], "boxes")
                        break

                    elif ask == "4":
                        print("Gloves: ", column1[gloves], "boxes")
                        break

                    elif ask == "5":
                        print("Gown: ", column1[gown], "boxes")
                        break

                    elif ask == "6":
                        print("Shoe Covers: ", column1[shoe_covers], "boxes")
                        break

                    elif ask == "7":
                        print("Head Cover: ", column1[head_cover], "boxes")
                        print("Face Shield: ", column1[face_shield], "boxes")
                        print("Mask: ", column1[mask], "boxes")
                        print("Gloves: ", column1[gloves], "boxes")
                        print("Gown: ", column1[gown], "boxes")
                        print("Shoe Covers: ", column1[shoe_covers], "boxes")
                        break

                    elif ask == "X":
                        hospital()
                        break

                    else:
                        print("Please enter a valid number.")

                elif ask_hospital == "2":
                    if ask == "1":
                        print("Head Cover: ", column2[head_cover], "boxes")
                        break

                    elif ask == "2":
                        print("Face Shield: ", column2[face_shield], "boxes")
                        break

                    elif ask == "3":
                        print("Mask: ", column2[mask], "boxes")
                        break

                    elif ask == "4":
                        print("Gloves: ", column2[gloves], "boxes")
                        break

                    elif ask == "5":
                        print("Gown: ", column2[gown], "boxes")
                        break


                    elif ask == "6":
                        print("Shoe Covers: ", column2[shoe_covers], "boxes")
                        break

                    elif ask == "7":
                        print("Head Cover: ", column2[head_cover], "boxes")
                        print("Face Shield: ", column2[face_shield], "boxes")
                        print("Mask: ", column2[mask], "boxes")
                        print("Gloves: ", column2[gloves], "boxes")
                        print("Gown: ", column2[gown], "boxes")
                        print("Shoe Covers: ", column2[shoe_covers], "boxes")
                        break

                    elif ask == "X":
                        hospital()
                        break

                    else:
                        print("Please enter a valid number.")

                elif ask_hospital == "3":
                    if ask == "1":
                        print("Head Cover: ", column3[head_cover], "boxes")
                        break

                    elif ask == "2":
                        print("Face Shield: ", column3[face_shield], "boxes")
                        break

                    elif ask == "3":
                        print("Mask: ", column3[mask], "boxes")
                        break

                    elif ask == "4":
                        print("Gloves: ", column3[gloves], "boxes")
                        break

                    elif ask == "5":
                        print("Gown: ", column3[gown], "boxes")
                        break

                    elif ask == "6":
                        print("Shoe Covers: ", column3[shoe_covers], "boxes")
                        break

                    elif ask == "7":
                        print("Head Cover: ", column3[head_cover], "boxes")
                        print("Face Shield: ", column3[face_shield], "boxes")
                        print("Mask: ", column3[mask], "boxes")
                        print("Gloves: ", column3[gloves], "boxes")
                        print("Gown: ", column3[gown], "boxes")
                        print("Shoe Covers: ", column3[shoe_covers], "boxes")
                        break

                    elif ask == "X":
                        hospital()
                        break

                    else:
                        print("Please enter a valid number.")

                elif ask_hospital == "4":
                    if ask == "1":
                        print("Head Cover: ", column4[head_cover], "boxes")
                        break

                    elif ask == "2":
                        print("Face Shield: ", column4[face_shield], "boxes")
                        break

                    elif ask == "3":
                        print("Mask: ", column4[mask], "boxes")
                        break

                    elif ask == "4":
                        print("Gloves: ", column4[gloves], "boxes")
                        break

                    elif ask == "5":
                        print("Gown: ", column4[gown], "boxes")
                        break

                    elif ask == "6":
                        print("Shoe Covers: ", column4[shoe_covers], "boxes")
                        break

                    elif ask == "7":
                        print("Head Cover: ", column4[head_cover], "boxes")
                        print("Face Shield: ", column4[face_shield], "boxes")
                        print("Mask: ", column4[mask], "boxes")
                        print("Gloves: ", column4[gloves], "boxes")
                        print("Gown: ", column4[gown], "boxes")
                        print("Shoe Covers: ", column4[shoe_covers], "boxes")
                        break

                    elif ask == "X":
                        hospital()
                        break

                    else:
                        print("Please enter a valid number.")

                elif ask_hospital == "X":
                    pickup()#################################################################################
                    break

                else:
                    print("Please enter a valid number.")
####################################above are define hospital inventory#############################################
####################################below are receive inventory#####################################################
def receive_inventory():
    while True:
        file = open('Received.txt', 'a')

        PPE_file = open('PPE.txt', 'r')
        read = PPE_file.readlines()
        first_row = read[1].strip()
        second_row = read[2].strip()
        third_row = read[3].strip()
        fourth_row = read[4].strip()
        fifth_row = read[5].strip()
        sixth_row = read[6].strip()
        column1 = first_row.split('\t')
        column2 = second_row.split('\t')
        column3 = third_row.split('\t')
        column4 = fourth_row.split('\t')
        column5 = fifth_row.split('\t')
        column6 = sixth_row.split('\t')

        quantity = -1
        receive = input("Which inventory received from supplier?\n"
                        "1. Head Cover\n"
                        "2. Face Shield\n"
                        "3. Mask\n"
                        "4. Gloves\n"
                        "5. Gown\n"
                        "6. Shoe Covers\n"
                        "Enter 'X' to back to main page").upper()

        if receive == "X":
            pickup()########################################################################################
            break

        if receive == "1":
            quant = input("How many box(es) received?")
            write = "Received " + str(quant) + " boxes Head Cover from Company A on " + str(formatted_time) + "\n"
            file.write(write)
            file.close()
            print("Received ", quant, " boxes Head Cover from Company A on ", formatted_time)
            column1[quantity] = str(int(column1[quantity]) + int(quant))
            updated_line = '\t'.join(column1) + '\n'
            read[1] = updated_line
            PPE_file = open('PPE.txt', 'w')
            PPE_file.writelines(read)
            PPE_file.close()

        elif receive == "2":
            quant = input("How many box(es) received?")
            write = "Received " + str(quant) + " boxes Face Shield from Company B on " + str(formatted_time) + "\n"
            file.write(write)
            file.close()
            print("Received ", quant, " boxes Face Shield from Company B" + str(formatted_time) + "\n")
            column2[quantity] = str(int(column2[quantity]) + int(quant))
            updated_line = '\t'.join(column2) + '\n'
            read[2] = updated_line
            PPE_file = open('PPE.txt', 'w')
            PPE_file.writelines(read)
            PPE_file.close()

        elif receive == "3":
            quant = input("How many box(es) received?")
            write = "Received " + str(quant) + " boxes Mask from Company C on " + str(formatted_time) + "\n"
            file.write(write)
            file.close()
            print("Received ", quant, " boxes Mask from Company C" + str(formatted_time) + "\n")
            column3[quantity] = str(int(column3[quantity]) + int(quant))
            updated_line = '\t'.join(column3) + '\n'
            read[3] = updated_line
            PPE_file = open('PPE.txt', 'w')
            PPE_file.writelines(read)
            PPE_file.close()

        elif receive == "4":
            quant = input("How many box(es) received?")
            write = "Received " + str(quant) + " boxes Gloves from Company D on " + str(formatted_time) + "\n"
            file.write(write)
            file.close()
            print("Received ", quant, " boxes Gloves from Company D" + str(formatted_time) + "\n")
            column4[quantity] = str(int(column4[quantity]) + int(quant))
            updated_line = '\t'.join(column4) + '\n'
            read[4] = updated_line
            PPE_file = open('PPE.txt', 'w')
            PPE_file.writelines(read)
            PPE_file.close()

        elif receive == "5":
            quant = input("How many box(es) received?")
            write = "Received " + str(quant) + " boxes Gown from Company B on " + str(formatted_time) + "\n"
            file.write(write)
            file.close()
            print("Received ", quant, " boxes Gown from Company B" + str(formatted_time) + "\n")
            column5[quantity] = str(int(column5[quantity]) + int(quant))
            updated_line = '\t'.join(column5) + '\n'
            read[5] = updated_line
            PPE_file = open('PPE.txt', 'w')
            PPE_file.writelines(read)
            PPE_file.close()

        elif receive == "6":
            quant = input("How many box(es) received?")
            write = "Received " + str(quant) + " boxes Shoe Covers from Company C on " + str(formatted_time) + "\n"
            file.write(write)
            file.close()
            print("Received ", quant, " boxes Shoe Covers from Company C" + str(formatted_time) + "\n")
            column6[quantity] = str(int(column6[quantity]) + int(quant))
            updated_line = '\t'.join(column6) + '\n'
            read[6] = updated_line
            PPE_file = open('PPE.txt', 'w')
            PPE_file.writelines(read)
            PPE_file.close()
######################################above are receive inventory##################################################
######################################below are distribute inventory###############################################
def distribute():
    file = open('Distribution.txt', 'a')
    hospital = open('Hospital.txt', 'r')
    read_hospital = hospital.readlines()
    while True:
        ask_hos = input("Which hospital you want to send the inventory?\n"
                        "1. Hospital A\n"
                        "2. Hospital B\n"
                        "3. Hospital C\n"
                        "4. Hospital D\n"
                        "5. Enter 'X' to back to main page").upper()

        if ask_hos == "X":
            pickup()############################################################################
            break

        ask_inventory = input("1. Head Cover\n"
                              "2. Face Shield\n"
                              "3. Mask\n"
                              "4. GLoves\n"
                              "5. Gown\n"
                              "6. Shoe Covers")

        first_row = read_hospital[1].strip()
        second_row = read_hospital[2].strip()
        third_row = read_hospital[3].strip()
        fourth_row = read_hospital[4].strip()
        column1 = first_row.split("\t")
        column2 = second_row.split('\t')
        column3 = third_row.split('\t')
        column4 = fourth_row.split('\t')

        hospital_name = 0
        hospital_code = 1
        head_cover = 3
        face_shield = 4
        mask = 5
        gloves = 6
        gown = 7
        shoe_covers = -1
        ###########################################################################
        PPE_file = open('PPE.txt', 'r')
        read = PPE_file.readlines()
        PPE_first_row = read[1].strip()
        PPE_second_row = read[2].strip()
        PPE_third_row = read[3].strip()
        PPE_fourth_row = read[4].strip()
        PPE_fifth_row = read[5].strip()
        PPE_sixth_row = read[6].strip()
        PPE_column1 = PPE_first_row.split('\t')
        PPE_column2 = PPE_second_row.split('\t')
        PPE_column3 = PPE_third_row.split('\t')
        PPE_column4 = PPE_fourth_row.split('\t')
        PPE_column5 = PPE_fifth_row.split('\t')
        PPE_column6 = PPE_sixth_row.split('\t')

        if ask_hos == "1":
            if ask_inventory == "1":
                while True:
                    # Situation for insufficient quantity if inventory
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column1[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Head Cover to Hospital A on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Head Cover to Hospital A on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column1[head_cover] = str(int(column1[head_cover]) + int(quant))
                        updated_line = '\t'.join(column1) + '\n'
                        read_hospital[1] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column1[-1] = str(int(PPE_column1[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column1) + '\n'
                        read[1] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "2":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column2[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Face Shield to Hospital A on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Face Shield to Hospital A on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column1[face_shield] = str(int(column1[face_shield]) + int(quant))
                        updated_line = '\t'.join(column1) + '\n'
                        read_hospital[1] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column2[-1] = str(int(PPE_column2[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column2) + '\n'
                        read[2] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "3":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column3[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Mask to Hospital A on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Mask to Hospital A on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column1[mask] = str(int(column1[mask]) + int(quant))
                        updated_line = '\t'.join(column1) + '\n'
                        read_hospital[1] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column3[-1] = str(int(PPE_column3[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column3) + '\n'
                        read[3] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "4":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column4[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gloves to Hospital A on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gloves to Hospital A on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column1[gloves] = str(int(column1[gloves]) + int(quant))
                        updated_line = '\t'.join(column1) + '\n'
                        read_hospital[1] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column4[-1] = str(int(PPE_column4[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column4) + '\n'
                        read[4] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "5":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column5[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gown to Hospital A on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gown to Hospital A on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column1[gown] = str(int(column1[gown]) + int(quant))
                        updated_line = '\t'.join(column1) + '\n'
                        read_hospital[1] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column5[-1] = str(int(PPE_column5[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column5) + '\n'
                        read[5] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "6":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column6[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Shoe Covers to Hospital A on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Shoe Covers to Hospital A on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column1[shoe_covers] = str(int(column1[shoe_covers]) + int(quant))
                        updated_line = '\t'.join(column1) + '\n'
                        read_hospital[1] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column6[-1] = str(int(PPE_column6[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column6) + '\n'
                        read[6] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

        elif ask_hos == "2":
            if ask_inventory == "1":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column1[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Head Cover to Hospital B on " + formatted_time + "\n"
                        file.write(write)
                        file.close()
                        print("Distributed ", quant, " boxes Head Cover to Hospital B on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column2[head_cover] = str(int(column2[head_cover]) + int(quant))
                        updated_line = '\t'.join(column2) + '\n'
                        read_hospital[2] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column1[-1] = str(int(PPE_column1[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column1) + '\n'
                        read[1] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "2":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column2[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Face Shield to Hospital B on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Face Shield to Hospital B on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column2[face_shield] = str(int(column2[face_shield]) + int(quant))
                        updated_line = '\t'.join(column2) + '\n'
                        read_hospital[2] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column2[-1] = str(int(PPE_column2[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column2) + '\n'
                        read[2] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "3":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column3[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Mask to Hospital B on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Mask to Hospital B on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column2[mask] = str(int(column2[mask]) + int(quant))
                        updated_line = '\t'.join(column2) + '\n'
                        read_hospital[2] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column3[-1] = str(int(PPE_column3[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column3) + '\n'
                        read[3] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "4":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column4[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gloves to Hospital B on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gloves to Hospital B on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column2[gloves] = str(int(column2[gloves]) + int(quant))
                        updated_line = '\t'.join(column2) + '\n'
                        read_hospital[2] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column4[-1] = str(int(PPE_column4[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column4) + '\n'
                        read[4] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "5":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column5[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gown to Hospital B on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gown to Hospital B on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column2[gown] = str(int(column2[gown]) + int(quant))
                        updated_line = '\t'.join(column2) + '\n'
                        read_hospital[2] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column5[-1] = str(int(PPE_column5[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column5) + '\n'
                        read[5] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "6":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column6[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Shoe Covers to Hospital B on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Shoe Covers to Hospital B on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column2[shoe_covers] = str(int(column2[shoe_covers]) + int(quant))
                        updated_line = '\t'.join(column2) + '\n'
                        read_hospital[2] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column6[-1] = str(int(PPE_column6[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column6) + '\n'
                        read[6] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

        elif ask_hos == "3":
            if ask_inventory == "1":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column1[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Head Cover to Hospital C on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Head Cover to Hospital C on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column3[head_cover] = str(int(column3[head_cover]) + int(quant))
                        updated_line = '\t'.join(column3) + '\n'
                        read_hospital[3] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column1[-1] = str(int(PPE_column1[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column1) + '\n'
                        read[1] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "2":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column2[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Face Shield to Hospital C on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Face Shield to Hospital C on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column3[face_shield] = str(int(column3[face_shield]) + int(quant))
                        updated_line = '\t'.join(column3) + '\n'
                        read_hospital[3] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column2[-1] = str(int(PPE_column2[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column2) + '\n'
                        read[2] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "3":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column3[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Mask to Hospital C on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Mask to Hospital C on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column3[mask] = str(int(column3[mask]) + int(quant))
                        updated_line = '\t'.join(column3) + '\n'
                        read_hospital[3] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column3[-1] = str(int(PPE_column3[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column3) + '\n'
                        read[3] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "4":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column4[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gloves to Hospital C on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gloves to Hospital C on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column3[gloves] = str(int(column3[gloves]) + int(quant))
                        updated_line = '\t'.join(column3) + '\n'
                        read_hospital[3] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column4[-1] = str(int(PPE_column4[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column4) + '\n'
                        read[4] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "5":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column5[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gown to Hospital C on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gown to Hospital C on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column3[gown] = str(int(column3[gown]) + int(quant))
                        updated_line = '\t'.join(column3) + '\n'
                        read_hospital[3] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column5[-1] = str(int(PPE_column5[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column5) + '\n'
                        read[5] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "6":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column6[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Shoe Covers to Hospital C on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Shoe Covers to Hospital C on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column3[shoe_covers] = str(int(column3[shoe_covers]) + int(quant))
                        updated_line = '\t'.join(column3) + '\n'
                        read_hospital[3] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column6[-1] = str(int(PPE_column6[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column6) + '\n'
                        read[6] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

        elif ask_hos == "4":
            if ask_inventory == "1":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column1[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Head Cover to Hospital D on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Head Cover to Hospital D on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column4[head_cover] = str(int(column4[head_cover]) + int(quant))
                        updated_line = '\t'.join(column4) + '\n'
                        read_hospital[4] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column1[-1] = str(int(PPE_column1[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column1) + '\n'
                        read[1] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "2":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column2[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Face Shield to Hospital D on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Face Shield to Hospital D on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column4[face_shield] = str(int(column4[face_shield]) + int(quant))
                        updated_line = '\t'.join(column4) + '\n'
                        read_hospital[4] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column2[-1] = str(int(PPE_column2[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column2) + '\n'
                        read[2] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "3":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column3[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Mask to Hospital D on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Mask to Hospital D on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column4[mask] = str(int(column4[mask]) + int(quant))
                        updated_line = '\t'.join(column4) + '\n'
                        read_hospital[4] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column3[-1] = str(int(PPE_column3[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column3) + '\n'
                        read[3] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "4":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column4[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gloves to Hospital D on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gloves to Hospital D on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column4[gloves] = str(int(column4[gloves]) + int(quant))
                        updated_line = '\t'.join(column4) + '\n'
                        read_hospital[4] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column4[-1] = str(int(PPE_column4[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column4) + '\n'
                        read[4] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "5":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column5[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Gown to Hospital D on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Gown to Hospital D on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column4[gown] = str(int(column4[gown]) + int(quant))
                        updated_line = '\t'.join(column4) + '\n'
                        read_hospital[4] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column5[-1] = str(int(PPE_column5[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column5) + '\n'
                        read[5] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break

            elif ask_inventory == "6":
                while True:
                    quant = int(input("How many box(es) need to distribute?"))
                    initial = int(PPE_column6[-1])
                    if quant > initial:
                        print("Sorry, the quantity of inventory is insufficient.")
                    else:
                        write = "Distributed " + str(quant) + " boxes Shoe Covers to Hospital D on " + formatted_time + "\n"
                        file.write(write)
                        print("Distributed ", quant, " boxes Shoe Covers to Hospital D on " + formatted_time + "\n")
                        #####above are record for Distributed file######
                        #####below are record for Hospital file######
                        column4[shoe_covers] = str(int(column4[shoe_covers]) + int(quant))
                        updated_line = '\t'.join(column4) + '\n'
                        read_hospital[4] = updated_line
                        hospital = open('Hospital.txt', 'w')
                        hospital.writelines(read_hospital)
                        hospital.close()
                        ######below are record for PPE file#####
                        PPE_column6[-1] = str(int(PPE_column6[-1]) - int(quant))
                        updated_line = '\t'.join(PPE_column6) + '\n'
                        read[6] = updated_line
                        PPE_file = open('PPE.txt', 'w')
                        PPE_file.writelines(read)
                        PPE_file.close()
                        break
#########################################above are distribute inventory##########################################
#########################################below are check distribution record#####################################
def parse_line(line):
    parts = line.strip().split(' ')

    if len(parts) >= 6 and parts[0] == "Distributed":
        try:
            quantity = int(parts[1])
            item_name = ' '.join(parts[3:-3])
            hospital_name = ' '.join(parts[-2:])
            return item_name, quantity, hospital_name
        except ValueError:
            print("Invalid quantity in line:", line)
            return None, None, None
    return None, None, None


def search_distribution(item_name, filename='Distribution.txt'):
    distribution_summary = {}

    try:
        file = open('Distribution.txt', 'r')
        lines = file.readlines()
    except FileNotFoundError:
        print("File ", filename, " not found.")
        return

    for line in lines:
        line_item_name, quantity, hospital_name = parse_line(line)
        if line_item_name and quantity and hospital_name:
            if line_item_name.lower() == item_name.lower():
                if hospital_name in distribution_summary:
                    distribution_summary[hospital_name] += quantity
                else:
                    distribution_summary[hospital_name] = quantity

    if hospital_name == "Head Cover":
        hospital_code = "HC"

    elif hospital_name == "Face Shield":
        hospital_code = "FS"

    elif hospital_name == "Mask":
        hospital_code = "MS"

    elif hospital_name == "Gloves":
        hospital_code = "GL"

    elif hospital_name == "Gown":
        hospital_code = "GW"

    elif hospital_name == "Shoe Covers":
        hospital_code = "SC"


    if distribution_summary:
        print("Distribution list for item", item_name, ":")
        for hospital_name, total_quantity in distribution_summary.items():
            print("Hospital:", hospital_name, "\nQuantity: ", total_quantity)
    else:
        print("No distribution data found for item ", item_name, ".")

    return item_name
#########################################above are check distribution record#####################################
#########################################below are check suppliers of inventory####################################
def suppliers():
    while True:
        ask = input("Which suppliers of inventory you want to check?\n"
                    "1. Company A\n"
                    "2. Company B\n"
                    "3. Company C\n"
                    "4. Company D\n"
                    "Enter 'X' to back to main page")
        if ask == "1":
            print("Company A supply Head Covers\n")

        elif ask == "2":
            print("Company B supply Face Shield and Gown\n")

        elif ask == "3":
            print("Company C supply Mask and Shoe Covers\n")

        elif ask == "4":
            print("Company D supply Gloves\n")

        elif ask.upper() == "X":
            pickup()############################################################################################
            break

        else:
            print("Please enter a valid input\n")
#########################################above are check suppliers of inventory####################################
#########################################below are item inventory tracking#########################################
def inventory_tracking():
    while True:
        ask = input("What you want to check?\n"
                    "1. Total quantity of inventory\n"
                    "2. Inventory that less than 25 boxes\n"
                    "Enter 'X' to back to main page\n").upper()
        if ask == "X":
            pickup()#############################################################################################
            break

        if ask == "1":
            file = open('PPE.txt', 'r')
            read = file.readlines()

            first_row = read[1].strip()
            second_row = read[2].strip()
            third_row = read[3].strip()
            fourth_row = read[4].strip()
            fifth_row = read[5].strip()
            sixth_row = read[6].strip()
            column1 = first_row.split('\t')
            column2 = second_row.split('\t')
            column3 = third_row.split('\t')
            column4 = fourth_row.split('\t')
            column5 = fifth_row.split('\t')
            column6 = sixth_row.split('\t')

            sent1 = column1[1] + " has " + column1[-1] + " boxes"
            sent2 = column2[1] + " has " + column2[-1] + " boxes"
            sent3 = column3[1+1] + " has " + column3[-1] + " boxes"
            sent4 = column4[1+1] + " has " + column4[-1] + " boxes"
            sent5 = column5[1+1] + " has " + column5[-1] + " boxes"
            sent6 = column6[1] + " has " + column6[-1] + " boxes"

            big_list = [sent1, sent2, sent3, sent4, sent5, sent6]
            big_list.sort()

            for item in big_list:
                print(item)

        elif ask == "2":
            file = open('PPE.txt', 'r')
            read = file.readlines()
            first_row = read[1].strip()
            second_row = read[2].strip()
            third_row = read[3].strip()
            fourth_row = read[4].strip()
            fifth_row = read[5].strip()
            sixth_row = read[6].strip()
            column1 = first_row.split('\t')
            column2 = second_row.split('\t')
            column3 = third_row.split('\t')
            column4 = fourth_row.split('\t')
            column5 = fifth_row.split('\t')
            column6 = sixth_row.split('\t')

            if int(column1[-1]) < 25:
                print(column1[0], " has only left", column1[-1])
            if int(column2[-1]) < 25:
                print(column2[0], " has only left", column2[-1])
            if int(column3[-1]) < 25:
                print(column3[0], " has only left", column3[-1])
            if int(column4[-1]) < 25:
                print(column4[0], " has only left", column4[-1])
            if int(column5[-1]) < 25:
                print(column5[0], " has only left", column5[-1])
            if int(column6[-1]) < 25:
                print(column6[0], " has only left", column6[-1])

#########################################above are item inventory tracking#########################################
#########################################below are monthly report generate#########################################
def parse_supply_line(line):
    parts = line.split()

    try:
        quantity = int(parts[1])
        item_index = parts.index("boxes") + 1
        from_index = parts.index("from")
        date_index = parts.index("on")

        # Extract item and company correctly
        item = ' '.join(parts[item_index:from_index])
        company = ' '.join(parts[from_index + 1:date_index])
        date = parts[date_index + 1]

        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        return quantity, item, company, parsed_date
    except (ValueError, IndexError):
        return None, None, None, None


def generate_receive_report():
    supply_data = []
    while True:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        formatted_month = str(month).zfill(2)

        # Read and filter supply data
        file = open('Received.txt', 'r')
        for line in file:
            quantity, item, company, date = parse_supply_line(line)
            if date and date.month == month and date.year == year:
                supply_data.append((date, company, item, quantity))

        print("Transaction Report for " + str(year) + "-" + formatted_month + "\n")

        print("Supply Received:")
        supply_summary = {}
        for date, company, item, quantity in supply_data:
            if company not in supply_summary:
                supply_summary[company] = {}
            if item not in supply_summary[company]:
                supply_summary[company][item] = 0
            supply_summary[company][item] += quantity

        for company, items in supply_summary.items():
            for item, quantity in items.items():
                print("Company:", company, "Item: ", item, "Quantity: ", quantity, " boxes")

        a = input("Enter 'X' to back to main page.\n"
                  "Hit ENTER to back to monthly report selection\n").upper()

        return a
#########################################above are monthly receive report generate####################################
#########################################below are monthly distribution report generate###############################
from datetime import datetime
def parse_supply_line_distribution(line):
    parts = line.split()

    try:
        quantity = int(parts[1])
        item_index = parts.index("boxes") + 1
        to_index = parts.index("to")
        on_index = parts.index("on")

        item = ' '.join(parts[item_index:to_index])
        hospital = ' '.join(parts[to_index + 1:on_index])
        date = parts[on_index + 1]

        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        return quantity, item, hospital, parsed_date
    except (ValueError, IndexError):
        return None, None, None, None


def generate_distribution_report():
    supply_data = []
    while True:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        formatted_month = str(month).zfill(2)

        # Read and filter supply data
        file = open('Distribution.txt', 'r')
        for line in file:
            quantity, item, hospital, date = parse_supply_line_distribution(line)
            if date and date.month == month and date.year == year:
                supply_data.append((date, hospital, item, quantity))

        print("Transaction Report for " + str(year) + "-" + formatted_month + "\n")

        print("Supply Distributed:")
        supply_summary = {}
        for date, hospital, item, quantity in supply_data:
            if hospital not in supply_summary:
                supply_summary[hospital] = {}
            if item not in supply_summary[hospital]:
                supply_summary[hospital][item] = 0
            supply_summary[hospital][item] += quantity

        for hospital, items in supply_summary.items():
            for item, quantity in items.items():
                print("Company:", hospital, "Item: ", item, "Quantity: ", quantity, " boxes")

        a = input("Enter 'X' to back to main page.\n"
                  "Hit ENTER to back to monthly report selection\n").upper()

        return a
#########################################above are monthly distribution report generate####################################
def pickup():
    while True:
        action = main_page()

        if action == "1":
            inventory()
            break

        elif action == "2":
            hospital_inventory()
            break

        elif action == "3":
            receive_inventory()
            break

        elif action == "4":
            distribute()
            break

        elif action == "5":
            while True:
                item_code = input("Enter the item code to search for\n"
                                  "Enter 'X' to back to main page").upper()
                if item_code == "X":
                    pickup()####################################################################################
                    break

                if item_code == "HC":
                    item_name = "Head Cover"

                elif item_code == "FS":
                    item_name = "Face Shield"

                elif item_code == "MS":
                    item_name = "Mask"

                elif item_code == "GL":
                    item_name = "Gloves"

                elif item_code == "GW":
                    item_name = "Gown"

                elif item_code == "SC":
                    item_name = "Shoe Covers"

                search_distribution(item_name)

        elif action == "6":
            suppliers()
            break

        elif action == "7":
            inventory_tracking()
            break

        elif action == "8":
            while True:
                ask = input("1. Distribution monthly report\n"
                            "2. Receive inventory monthly report\n"
                            "Enter 'X' to back to main page").upper()
                if ask == "1":
                    generate_distribution_report()
                    if a == "X":
                        pickup()
                        break

                elif ask == "2":
                    generate_receive_report()
                    if a == "X":
                        pickup()
                        break

                elif ask == "X":
                    pickup()
                    break

                else:
                    print("Please enter a valid value")

            else:
                print("Please enter a valid value")
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################

a = input("Hi, are you an admin of Department of Health management system? (Y/N)").upper()
if a == "Y":
    print("This is the admin login page")
    login_status, register_admin = login()
    if login_status == "granted":
        pickup()


elif a == "N":
    if len(controller_ID_list) < 4:
        b = input("Did you want to register as admin? (Y/N)").upper()

        if b == "Y":
            print("Please log in to an admin account to continue.")
            register_admin = login()
            #if register_admin == "granted":
            new_admin_list = []
            controller1_ID = input("Enter new admin ID")
            controller1_PW = input("Enter new admin password")
            new_admin_list.append(controller1_ID)
            new_admin_list.append(controller1_PW)
            controller_ID_list.append(new_admin_list)
            login()
            pickup()

        elif b == "N":
            print("You have no right to access to management system")

    else:
        print("I'm sorry, our admin account has reach limit.\n"
              "Please contact our admin for further action or use existing admin account to login.\n")