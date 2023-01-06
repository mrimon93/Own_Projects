import pandas as pd
import time
import matplotlib as plt
import seaborn as seaborn



#---------------------------Writing Function-------------------------------


def asking_the_user_question():
    product_name = input("What is the Name of the Product you want to buy? ")
    product_category = input("Product category? ")
    product_location = input("Where did you find the product? ")
    product_link = input("Do you have the link of the product? If YES paste the link, if NO press Enter ")
    product_price = int(input("The price of the Product? "))
    product_currency = input("What currency? ")
    #FIX THE RETURN IN NICE AND BEAUTIFUL OUT
    return f"{product_name},{product_category},{product_location},{product_link,product_price},{product_currency}"

#Creating a CSV-File
def output_csv_file(product_name,product_category,product_location,product_link,product_price,product_currency):
    data = {"Name": [product_name], "Category": [product_category], "location": [product_location], "link": [product_link],"Price": [product_price],
            "Currency": [product_currency]}
    df = pd.DataFrame(data)
    #Remember to have a filename input
    df.to_csv(filename, index=False)

def matplot_csv_data(filename):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(filename)
    # Create a figure and a subplot
    fig, ax = plt.subplots()
    # Plot the "Price" column against the index of the DataFrame
    ax.plot(df.index, df["Price"])
    # Set the x-axis label
    ax.set_xlabel("Index")
    # Set the y-axis label
    ax.set_ylabel("Price")
    # Show the plot
    plt.show()

"""
def seaborn_sns_scatterplot_csv_data(filename):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(filename)
    # Use the `scatterplot` function to plot the "Price" column against the "Category" column
    sns.scatterplot(x="Category", y="Price", data=df)
    # Show the plot
    plt.show()
"""
#-------------------------- Execution of the Code ---------------------------------
print("Hello and Welcome the cart-Program \n")
print("Please enter the following values\n")

while True:
    cmd = input("Command: ")
    if cmd == "LIST":
        print(asking_the_user_question())
    elif cmd == "ADD":
        id= input('Enter Id number after 7 ')
        first_name = input("  Name: ")
        last_name = input("  Lastname: ")
        title = input('Your Title? ')
        organization = input('Where do your work? ')
        add_contacts(dbconn,id, first_name, last_name,title,organization)
    elif cmd == "DELETE":
        id = input("  id: ")
        delete_contacts(dbconn, id)
    elif cmd == "QUIT":
        save_contacts(dbconn)
        print("Committing all changes to the database and quitting! Good bye!")
        exit()












#Ideas!
"""
#Making the User to answer the question!
def force_type(typ):
    while True:
        try:
            s = input("Enter a string: ")
            return typ(s)
        except (TypeError, ValueError):
            print(f"Could not convert string to {typ.__name__}. Please try again.")


result = force_type(int)
print(f"Result: {result}")

"""