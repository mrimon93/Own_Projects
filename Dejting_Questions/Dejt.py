import pandas as pd


#Make a clean output of def
def yes_to_dejt():
        if answer_to_dejt == 'yes':
            df = pd.DataFrame(columns =['Age','Size','Job'])
            age = int(input('What Age should he be? '))
            size = input("What Size, Athletic, tall? ")
            job = input('What job should he have?')

            df = df.append({'Age': age, 'Size': size,'Job':job}, ignore_index=True)

            # Write the dataframe to a CSV file
            df.to_csv('data.csv', index=False)
        else:
            print("Well, suck off then")

#Execution of the program

print("Hello, and welcome to the intressting Question \n")

user_question = input('Are you single? ').lower()

if user_question == 'yes':
    answer_to_dejt = input('are you intressting in dejting').lower()
    yes_to_dejt()
else:
    print('Well, cook of then')