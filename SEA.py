import tkinter as tk
from tkinter import filedialog, ttk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def perform_searches(sentence, keyword, file_path):
    # Initialize the web driver with options to keep the browser open
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    with open(file_path, 'r') as file:
        for line in file:
            modified_sentence = sentence.replace(keyword, line.strip())
            search_query = modified_sentence
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(f"https://www.google.com/search?q={search_query}")

def start_search():
    repeating_sentence = repeating_sentence_entry.get()
    special_keyword = special_keyword_entry.get()
    file_path = file_path_label.cget("text")
    perform_searches(repeating_sentence, special_keyword, file_path)

def open_file():
    file_path = filedialog.askopenfilename()
    file_path_label.config(text=file_path)

root = tk.Tk()
root.title("Search Engine Automation")
style = ttk.Style(root)
style.theme_use('clam')

large_font = ('Verdana', 12)
small_font = ('Verdana', 10)

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(expand=True, fill="both")

ttk.Label(main_frame, text="Enter your sentence template:", font=small_font).pack(pady=5)
repeating_sentence_entry = ttk.Entry(main_frame, font=large_font)
repeating_sentence_entry.pack(padx=10, pady=5, fill="x")

ttk.Label(main_frame, text="Enter the special keyword (e.g., SHS):", font=small_font).pack(pady=5)
special_keyword_entry = ttk.Entry(main_frame, font=large_font)
special_keyword_entry.pack(padx=10, pady=5, fill="x")

ttk.Label(main_frame, text="Select your file with words/sentences:", font=small_font).pack(pady=5)
open_file_button = ttk.Button(main_frame, text="Open File", command=open_file)
open_file_button.pack(padx=10, pady=5)

file_path_label = ttk.Label(main_frame, text="", font=small_font)
file_path_label.pack(padx=10, pady=5, fill="x")

start_button = ttk.Button(main_frame, text="Start Search", command=start_search)
start_button.pack(padx=10, pady=10, fill="x")

root.eval('tk::PlaceWindow . center')

root.mainloop()
