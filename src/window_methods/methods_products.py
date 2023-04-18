import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry, DISABLED
from src.datatier import Datatier
from src.model import Products

data_tier = Datatier()


def show_products():
    result_window = Toplevel()
    result_window.title("Products")
    result_window.geometry("900x600+100+100")
    result_window.configure(bg='gray10')

    products = data_tier.get_product()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Product Name", "Price", "In Stock", "Category"]
    col_widths = [10, 30, 10, 10, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, product in enumerate(products, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, product['Product_name'], str(product['Products_price']) + "Kč", product['Products_in_stock'], product['Categories_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Products are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))



def add_product():
    add_window = Toplevel()
    add_window.title("Add Product")
    add_window.geometry("1200x800+100+100")
    add_window.configure(bg='gray10')

    # Create labels and entry widgets for the order information
    product_name_label = Label(add_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_entry = Entry(add_window, font=("Helvetica", 12))
    product_name_label.pack(pady=10)
    product_name_entry.pack()

    description_label = Label(add_window, text="Description:", bg='gray10', fg="white", font=("Helvetica", 12))
    description_entry = Entry(add_window, font=("Helvetica", 12))
    description_label.pack(pady=10)
    description_entry.pack()

    price_label = Label(add_window, text="Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    price_entry = Entry(add_window, font=("Helvetica", 12))
    price_label.pack(pady=10)
    price_entry.pack()

    in_stock_label = Label(add_window, text="In Stock (Yes/No):", bg='gray10', fg="white", font=("Helvetica", 12))
    in_stock_entry = Entry(add_window, font=("Helvetica", 12))
    in_stock_label.pack(pady=10)
    in_stock_entry.pack()

    category_label = Label(add_window, text="Category:", bg='gray10', fg="white", font=("Helvetica", 12))
    category_entry = Entry(add_window, font=("Helvetica", 12))
    category_label.pack(pady=10)
    category_entry.pack()

    # Create a function to submit the product
    def submit_product():
        # Get the product information from the entry widgets
        product_name = product_name_entry.get().strip()
        description = description_entry.get().strip()
        price = price_entry.get()
        in_stock = in_stock_entry.get()
        category = category_entry.get()

        # Check if in_stock value is valid
        if in_stock not in ["Yes", "No"]:
            output_text.insert(END, "Invalid value for In Stock. Please enter either 'Yes' or 'No'.\n")
            return

        # Check if the price value is valid
        if not re.match(r'^[1-9]\d*(\.\d+)?$', price):
            output_text.insert(END, "Invalid Price.\n")
            return

        # Check if product_name and description fields are filled
        if not product_name:
            output_text.insert(END, "Please enter a Product Name.\n")
            return
        if not description:
            output_text.insert(END, "Please enter a Description.\n")
            return

        # Create a Products object and add it to the data tier
        product = Products(product_name, description, price, in_stock, category)
        data_tier.add_product(product)

        output_text.insert(END, "Product added successfully.\n")

    # Create a button to submit the product
    submit_button = Button(add_window, text="Submit", bg="#4a4a4a",
                           fg="white", command=submit_product, font=("Helvetica", 14))
    submit_button.pack(pady=10)

    # Create a text widget to display output messages
    output_text = Text(add_window, bg='gray10', fg="white", font=("Helvetica", 12))
    output_text.pack(fill=BOTH, expand=True)

    result_label = Label(add_window, text="Add Product", bg='gray10', fg="white", font=("Helvetica", 16))
    result_label.pack(pady=(10, 0))


def update_product():
    update_window = Toplevel()
    update_window.title("Update Product")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    products = data_tier.get_product()
    update_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    update_text.pack(fill=BOTH, expand=True)

    update_text.insert(END, "\n{:<5} {:<30} {:<20} {:<20} {:<20}\n".format("No.", "Product name", "Price", "Stock",
                                                                           "Category"))
    update_text.insert(END, "-" * 115 + "\n")

    cislo = 0
    for product in products:
        cislo += 1
        update_text.insert(END, "{:<5} {:<30} {:<20} {:<20} {:<20}\n\n".format(str(cislo), product['Product_name'],
                                                                               str(product['Products_price']) + " Kč",
                                                                               product['Products_in_stock'],
                                                                               product['Categories_name']))
    update_text.config(state=DISABLED)
    product_name_label = Label(update_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_label.pack(pady=(10, 0))
    product_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    product_name_entry.pack()
    price_label = Label(update_window, text="New Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    price_label.pack(pady=(10, 0))
    price_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    price_entry.pack()

    in_stock_label = Label(update_window, text="Update Stock:", bg='gray10', fg="white", font=("Helvetica", 12))
    in_stock_label.pack(pady=(10, 0))
    in_stock_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    in_stock_entry.pack()

    def update_products_in_database():
        product_name = product_name_entry.get()
        new_price = price_entry.get()
        in_stock = in_stock_entry.get()

        data_tier.update_product(new_price, in_stock, product_name)
        result_label.config(text="Product has been updated.")

    update_button = Button(update_window, text="Update Product", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def update_product_description():
    update_window = Toplevel()
    update_window.title("Update Product Description")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    products = data_tier.get_product()
    update_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    update_text.pack(fill=BOTH, expand=True)

    update_text.insert(END, "\n\n{:<5} {:<30}\n".format("No.", "Product name"))
    update_text.insert(END, "-" * 115 + "\n")

    cislo = 0
    for product in products:
        cislo += 1
        update_text.insert(END, "{:<5} {:<30} {} \n{:<30}\n\n".format(str(cislo), product['Product_name'],
                                                                      "\nDescription: \n",
                                                                      product['Products_description']))
    update_text.config(state=DISABLED)
    product_name_label = Label(update_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_label.pack(pady=(10, 0))
    product_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    product_name_entry.pack()

    description_label = Label(update_window, text="New Description:", bg='gray10', fg="white", font=("Helvetica", 12))
    description_label.pack(pady=(10, 0))
    description_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    description_entry.pack()

    def update_products_in_database():
        product_name = product_name_entry.get()
        new_description = description_entry.get()

        data_tier.update_product_description(new_description, product_name)
        result_label.config(text="Product has been updated.")

    update_button = Button(update_window, text="Update Product", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def update_product_price():
    update_window = Toplevel()
    update_window.title("Update Product Price")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    products = data_tier.get_product()
    update_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    update_text.pack(fill=BOTH, expand=True)

    update_text.insert(END, "\n{:<5} {:<20} {:<30}\n".format("No.", "Product name", "Product price"))
    update_text.insert(END, "-" * 115 + "\n")

    cislo = 0
    for product in products:
        cislo += 1
        update_text.insert(END, "{:<5} {:<30} {} {}\n\n".format(str(cislo), product['Product_name'],
                                                                product['Products_price'], "Kč"))

    update_text.config(state=DISABLED)
    product_name_label = Label(update_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_label.pack(pady=(10, 0))
    product_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    product_name_entry.pack()

    price_label = Label(update_window, text="New Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    price_label.pack(pady=(10, 0))
    price_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    price_entry.pack()

    def update_products_in_database():
        product_name = product_name_entry.get()
        new_price = price_entry.get()

        data_tier.update_product_price(new_price, product_name)
        result_label.config(text="Product has been updated.")

    update_button = Button(update_window, text="Update Product", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def delete_product_window():
    delete_window = Toplevel()
    delete_window.title("Products")
    delete_window.geometry("1200x600+100+100")
    delete_window.configure(bg='gray10')

    products = data_tier.get_product()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END, "\n{:<5} {:<30} {:<10} {:<10} {:<20}\n".format("No.", "Product name", "Price", "In stock",
                                                                           "Category"))
    result_text.insert(END, "-" * 115 + "\n")

    cislo = 0
    for product in products:
        cislo += 1
        result_text.insert(END, "{:<5} {:<30} {:<10} {:<10} {:<20}\n\n".format(str(cislo), product['Product_name'],
                                                                               "$" + str(product['Products_price']),
                                                                               str(product['Products_in_stock']),
                                                                               product['Categories_name']))

    result_text.config(state=DISABLED)
    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    name_label = Label(delete_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 14))
    name_label.pack()
    name_entry = Entry(delete_window, font=("Helvetica", 14))
    name_entry.pack()

    def delete_product_from_controller():
        # Get the customer name from the entry field
        name = name_entry.get()

        # Delete the order from the controller
        data_tier.delete_product(name)

        # Show a message indicating that the order was deleted
        result_label.config(text="Product deleted successfully.")

    # Create a button to delete the order
    delete_button = Button(delete_window, text="Delete Product", command=delete_product_from_controller, bg="#4a4a4a",
                           fg="white", font=("Helvetica", 14))
    delete_button.pack()

    # Create a label to display the result of deleting the order
    result_label = Label(delete_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack()


def import_products():
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        data_tier.import_product_from_csv(filepath)
