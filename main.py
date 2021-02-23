from tkinter import *

# Read the file containing Dewey Decimal Subject Headings and
# corosponding numbers. Then index them in to a list to be
# searched later
file = open("dewey_des.txt", "r")
content = file.read().split('\n')


def callback():
    search_terms = search_box.get()
    search_box.delete("0", END)

    if len(search_terms) > 0:
        # TODO: Search the list "content" to find the corosponding info
        results_list = []
        for i in content:
            if search_terms.lower() in i.lower():
                results_list.append(i + '\n')

        
        Content_Text.delete("1.0", END)

        if len(results_list) == 0:
            Content_Text.insert("0.0", "No resutls found.")
        elif len(results_list) > 50:
            Content_Text.insert("0.0", "Too many resutls found. Please narrow search terms.")
        else:
            for i  in results_list:
                Content_Text.insert('0.0', i)
    else:
        Content_Text.delete("1.0", END)
        Content_Text.insert('0.0', "Please enter a search term.")
        

# Create an instance of tkinter.
root = Tk()
root.minsize(500, 250)
root.maxsize(800, 800)
root.title("Dewey Decimal Reference")

# Create the frame to hold the search tools.
Search_Frame = Frame(root)
Search_Frame.pack(side='top')

Search_Label = Label(Search_Frame, text="Search Dewey Reference Numbers by Subject", font=("Times New Roman", 12))
Search_Label.pack(side='top')

# Create the search box.
search_box = Entry(Search_Frame, width=40, font=("Times New Roman", 12))
search_box.pack(side='left', padx=10)

# Create the search button.
s_button = Button(Search_Frame, text="Submit", font=("Times New Roman", 12), width=10, command=callback)
s_button.pack(side="right", padx=10)

#Create the frame in which content will be displayed.
Content_Frame = Frame(root)
Content_Frame.pack(side='bottom')

# Create the label that will display the search results.
Content_Text = Text(Content_Frame, relief='sunken', font=("Times New Roman", 14))
Content_Text.pack(side='bottom', fill='x', padx=10, pady=10)

root.mainloop()
