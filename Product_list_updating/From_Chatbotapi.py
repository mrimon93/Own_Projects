import pandas as pd
import matplotlib.pyplot as plt

def asking_the_user_question():
    product_name = input("What is the Name of the Product you want to buy? ")
    product_category = input("Product category? ")
    product_location = input("Where did you find the product? ")
    product_link = input("Do you have the link of the product? If YES paste the link, if NO press Enter ")
    product_price = int(input("The price of the Product? "))
    product_currency = input("What currency? ")
    return product_name, product_category, product_location, product_link, product_price, product_currency

def output_csv_file(product_name, product_category, product_location, product_link, product_price, product_currency, filename):
    data = {"Name": [product_name], "Category": [product_category], "location": [product_location], "link": [product_link],"Price": [product_price], "Currency": [product_currency]}
    df = pd.DataFrame(data)
    df.to_csv(filename, index=True)

def matplot_csv_data(filename):
    df = pd.read_csv(filename)
    fig, ax = plt.subplots()
    ax.plot(df.index, df["Price"])
    ax.set_xlabel("Index")
    ax.set_ylabel("Price")
    plt.show()

while True:
    cmd = input("Command: ").lower()
    if cmd == "add":
        product_name, product_category, product_location, product_link, product_price, product_currency = asking_the_user_question()
        filename = input("Enter the name of the CSV file: ")
        output_csv_file(product_name, product_category, product_location, product_link, product_price, product_currency, filename)
    elif cmd == "plot":
        filename = input("Enter the name of the CSV file: ")
        matplot_csv_data(filename)
    elif cmd == "quit":
        print("Quitting! Good bye!")
        exit()
