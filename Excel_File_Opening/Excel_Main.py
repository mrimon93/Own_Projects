import pandas as pd
import time

#Creating an app where it can read any Excel File
#Goal: Is to able to open and search an excel file so that we can either vizualize or show the data in the command



def open_the_excel_file():
    user_excel =input("Write down the Excel-File: ")
    user_sheet = input("What Sheet Number? ")
    #Something is disturbing me here, i want to make sure that you can just write 1
    df = pd.read_excel(f'{user_excel}.xlsx', sheet_name='Sheet' + user_sheet)
    print(df.head())


def conversion_from_xlxlsx_to_CSV():
    conversion_excel = input("Write the title of the excel file for conversion to CSV")
    # Load the Excel file
    df_conversion = pd.read_excel(f'{conversion_excel}.xlsx')

    # Convert the DataFrame to a CSV file
    df_conversion.to_csv(f'{conversion_excel}.csv', index=False)



#--------------------------------------- EXECUTION OF THE PROGRAM --------------------------------------
print("Hello Welcome to the execution of the Using Excel File \n")


#Asking the user of the options
user_asking = int(input("What do you want to do? press 1 for opening an excel file or 2 for conversion excel file to csv file: "))


if user_asking == 1:
    open_the_excel_file()
elif user_asking ==2:
    conversion_from_xlxlsx_to_CSV()
else:
    print("I am sorry, but you suck")
    time.sleep(2)
    exit()