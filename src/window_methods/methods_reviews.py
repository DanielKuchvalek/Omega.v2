import re
from tkinter import Button, Toplevel, Text, BOTH, END, Label, Entry, Frame, BOTTOM, DISABLED, Y, TOP
from src.datatier import Datatier
from src.model import Review

data_tier = Datatier()


def show_review():
    result_window = Toplevel()
    result_window.title("Review")
    result_window.geometry("1450x600+100+100")
    result_window.configure(bg='gray10')

    reviews = data_tier.get_review()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Review ID", "Customer ID", "Product id", "Rating", "Comment", "Review Date", "Customer Name"]
    col_widths = [10, 25, 15, 15, 10, 25, 15, 15]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
        *col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, review in enumerate(reviews, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
            *col_widths)
        review_date = review['review_date'].strftime('%Y-%m-%d')
        row_values = [i, review['review_id'], review['customer_id'], review['product_id'], review['rating'],
                      review['comment'], review_date, review['customer_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))
    result_label = Label(result_window, text="Reviews are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def update_review():
    update_window = Toplevel()
    update_window.title("Update Review+100+100")
    update_window.geometry("1200x750")
    update_window.configure(bg='gray10')

    reviews = data_tier.get_review()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END,
                       "\n{:<5} {:<25} {:<25} {:<25} {:<35} {:<35} {:<25} {:<25} \n".format("No.", "Review_id",
                                                                                            "customer_id",
                                                                                            "product_name",
                                                                                            "rating", "comment",
                                                                                            "review_date",
                                                                                            "customer_name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for review in reviews:
        cislo += 1
        review_date = review['review_date'].strftime('%Y-%m-%d')
        result_text.insert(END, "{:<5} {:<35} {:<35} {:<30} {:<35} {:<35} {:<25} {:<25} \n\n".format(str(cislo),
                                                                                                     review[
                                                                                                         'review_id'],
                                                                                                     str(review[
                                                                                                             'customer_id']),
                                                                                                     str(review[
                                                                                                             'product_id']),
                                                                                                     review['rating'],
                                                                                                     review['comment'],
                                                                                                     review_date,
                                                                                                     review[
                                                                                                         'customer_name'], ))
        result_text.insert(END, "-" * 225 + "\n")

    review_id_label = Label(update_window, text="Review id:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_id_label.pack(pady=(10, 0))
    review_id_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    review_id_entry.pack()

    review_rating_label = Label(update_window, text="New Rating:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_rating_label.pack(pady=(10, 0))
    review_rating_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    review_rating_entry.pack()

    review_comment_label = Label(update_window, text="New Comment:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_comment_label.pack(pady=(10, 0))
    review_comment_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    review_comment_entry.pack()

    def update_products_in_database():
        review_id = review_id_entry.get()
        new_rating = review_rating_entry.get()
        new_comment = review_comment_entry.get()

        data_tier.update_review_rating_comment(new_rating, new_comment, review_id)
        result_label.config(text="Review has been updated.")

    update_button = Button(update_window, text="Update Review", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def delete_review_window():
    # Vytvoření nového okna pro zadání jména zákazníka
    delete_window = Toplevel()
    delete_window.title("Delete Review")
    delete_window.geometry("1200x750+100+100")
    delete_window.configure(bg='gray10')

    reviews = data_tier.get_review()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END,
                       "\n{:<5} {:<25} {:<25} {:<25} {:<35} {:<35} {:<25} {:<25} \n".format("No.", "Review_id",
                                                                                            "customer_id",
                                                                                            "product_name",
                                                                                            "rating", "comment",
                                                                                            "review_date",
                                                                                            "customer_name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for review in reviews:
        cislo += 1
        review_date = review['review_date'].strftime('%Y-%m-%d')
        result_text.insert(END, "{:<5} {:<35} {:<35} {:<30} {:<35} {:<35} {:<25} {:<25} \n\n".format(str(cislo),
                                                                                                     review[
                                                                                                         'review_id'],
                                                                                                     str(review[
                                                                                                             'customer_id']),
                                                                                                     str(review[
                                                                                                             'product_id']),
                                                                                                     review['rating'],
                                                                                                     review['comment'],
                                                                                                     review_date,
                                                                                                     review[
                                                                                                         'customer_name'], ))
        result_text.insert(END, "-" * 225 + "\n")

    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    review_id_label = Label(delete_window, text="Review id:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_id_label.pack()
    review_id_entry = Entry(delete_window, font=("Helvetica", 14))
    review_id_entry.pack()

    def delete_customer_from_controller():
        # Get the customer name from the entry field
        review_id = review_id_entry.get()

        # Delete the order from the controller
        data_tier.delete_review(review_id)

        # Show a message indicating that the order was deleted
        result_label.config(text="Review deleted successfully.")

    # Create a button to delete the order
    delete_button = Button(delete_window, text="Delete Review", bg='gray10', fg="white",
                           command=delete_customer_from_controller, font=("Helvetica", 12))
    delete_button.pack()

    # Create a label to display the result of deleting the order
    result_label = Label(delete_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack()


def add_review():
    add_window = Toplevel()
    add_window.title("Add Review")
    add_window.geometry("1200x800+100+100")
    add_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    products = data_tier.get_product()

    # Create output text box
    result_text = Text(add_window, bg='gray10', fg="white", font=("Helvetica", 9))
    result_text.pack(side=TOP, fill=BOTH, expand=False)

    # Display list of customers
    result_text.insert(END, "\n{:<5} {:<30} \n".format("Id.", "Name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for customer in customers:
        cislo += 1
        result_text.insert(END, "{:<5} {:<30}\n\n".format(str(cislo), customer['name']))

    # Display list of products
    result_text.insert(END, "\n{:<5} {:<30} \n".format("No.", "Product Name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for product in products:
        cislo += 1
        result_text.insert(END, "{:<5} {:<30}\n\n".format(str(cislo), product['Product_name']))

    # Create input form
    input_frame = Frame(add_window, bg='gray10')
    input_frame.pack(side=BOTTOM, fill=Y, pady=5)

    customer_id_label = Label(input_frame, text="Customer id:", bg='gray10', fg="white", font=("Helvetica", 12))
    customer_id_entry = Entry(input_frame, font=("Helvetica", 12))
    customer_id_label.pack(pady=5)
    customer_id_entry.pack()

    product_id_label = Label(input_frame, text="Product id:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_id_entry = Entry(input_frame, font=("Helvetica", 12))
    product_id_label.pack(pady=5)
    product_id_entry.pack()

    rating_label = Label(input_frame, text="Rating:", bg='gray10', fg="white", font=("Helvetica", 12))
    rating_entry = Entry(input_frame, font=("Helvetica", 12))
    rating_label.pack(pady=5)
    rating_entry.pack()

    comment_label = Label(input_frame, text="Comment:", bg='gray10', fg="white", font=("Helvetica", 12))
    comment_entry = Entry(input_frame, font=("Helvetica", 12))
    comment_label.pack(pady=5)
    comment_entry.pack()

    result_label = Label(input_frame, text="", bg='gray10', fg="white", font=("Helvetica", 12))
    result_label.pack(pady=5)

    # Create submit button
    def submit_review():
        customer_id = customer_id_entry.get()
        product_id = product_id_entry.get()
        rating = rating_entry.get()
        comment = comment_entry.get()

        if not customer_id or not product_id or not rating or not comment:
            result_label.configure(text="Please fill all fields.", fg="red")
            return

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError
        except ValueError:
            result_label.configure(text="Rating must be a number between 1 and 5.", fg="red")
            return

        review = Review(customer_id, product_id, rating, comment)
        data_tier.add_review(review)

        # Clear input fields
        customer_id_entry.delete(0, END)
        product_id_entry.delete(0, END)
        rating_entry.delete(0, END)
        comment_entry.delete(0, END)

        # Display success message
        result_label.configure(text="Review added successfully.", fg="green")

    submit_button = Button(input_frame, text="Submit", bg="#4a4a4a",
                           fg="white", command=submit_review, font=("Helvetica", 14))
    submit_button.pack(pady=5)
