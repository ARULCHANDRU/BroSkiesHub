# BroSkiesHub
Tasks from BroSkiesHub on Python

# DAY 1 
## Calculator CLI App - BH Python Developer Internship Task 1

[cite_start]This project is a simple command-line interface (CLI) calculator built with Python. 

## Objective
[cite_start]The main objective was to create a calculator that supports basic arithmetic operations: addition, subtraction, multiplication, and division. 

## How it Works
- [cite_start]The script uses functions for each mathematical operation. 
- [cite_start]It runs in a loop that continuously prompts the user to select an operation. 
- [cite_start]The user's input is captured to perform the calculation, and the result is displayed. 
- [cite_start]The loop terminates when the user chooses to exit. 

## How to Run
1. Make sure you have Python installed.
2. Clone this repository or download the `calculator.py` file.
3. Open your terminal and navigate to the project directory.
4. Run the command: `python calculator.py`

# DAY 2
# Task 2: Python Console To-Do List

This repository contains the solution for the BH Python Developer Internship Task 2.

## Objective
The objective is to implement a simple, console-based to-do list manager using Python.

## Features
- **View Tasks:** Users can view all their current tasks.
- **Add Tasks:** Users can add new tasks to their list.
- **Remove Tasks:** Users can remove a task from the list.
- **Persistence:** The application stores all tasks in a `tasks.txt` file, so the data is not lost when the program closes.

## How to Run
1.  Ensure you have Python installed.
2.  Clone this repository or download the `todo.py` file.
3.  Open your terminal and navigate to the project directory.
4.  Run the command: `python todo.py`

# Day 3
# Task 3: Web Scraper for News Headlines

This repository contains the solution for the BH Python Developer Internship Task 3.

## Objective
[cite_start]The objective is to create a Python script that scrapes the top news headlines from a website and saves them to a text file.  [cite_start]This project uses the `requests` and `BeautifulSoup` libraries. 

## How it Works
- The script sends a GET request to the BBC News website.
- [cite_start]It uses BeautifulSoup to parse the HTML content of the page. 
- It finds all the `<h2>` tags, which typically contain the main headlines.
- [cite_start]The extracted headlines are cleaned up and saved into a `headlines.txt` file. [cite:1]

## Files
- `scraper.py`: The Python script that performs the web scraping.
- [cite_start]`headlines.txt`: The output file containing the scraped headlines. 

## How to Run
1.  Ensure you have Python, `requests`, and `beautifulsoup4` installed.
2.  Run the script from your terminal: `python scraper.py`

# Day 4
# Task 4: REST API with Flask

This repository contains a simple REST API built with Python and Flask for managing user data.

## Objective
The objective is to create a REST API that supports GET, POST, PUT, and DELETE operations for a collection of users stored in memory.

## Endpoints
The API provides the following endpoints:

| Method | URL                | Description                 |
|--------|--------------------|-----------------------------|
| `GET`    | `/users`           | Get all users.              |
| `GET`    | `/users/<id>`      | Get a single user by ID.    |
| `POST`   | `/users`           | Create a new user.          |
| `PUT`    | `/users/<id>`      | Update an existing user.    |
| `DELETE` | `/users/<id>`      | Delete a user by ID.        |

### `POST /users` Request Body Example
```json
{
    "name": "Your Name",
    "email": "your.email@example.com"
}
```
# Day 5
# Task 5: Data Analysis with Pandas

This repository contains the solution for the BH Python Developer Internship Task 5.

## Objective
The objective was to perform a basic analysis of a sales dataset using Python's Pandas and Matplotlib libraries.

## Analysis Performed
- The `sales_data.csv` file was loaded into a Pandas DataFrame.
- A new column, `Total_Sales`, was calculated by multiplying the price and quantity of each transaction.
- The data was grouped by product to calculate the total sales for each unique product.
- A bar chart was created to visually represent the total sales per product.

## Files
- `Sales_Analysis_Notebook.ipynb`: The Jupyter/Colab notebook containing all the Python code, analysis steps, and the final chart.
- `sales_data.csv`: The sample dataset used for the analysis.

# Day 6
# Task 6: Personal Portfolio with Flask

This repository contains a simple, one-page personal portfolio website built with Python and Flask.

## Objective
The objective is to create a personal portfolio site that showcases basic information, projects, and includes a functional contact form.

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS

## Features
- A single, responsive page layout.
- Sections for "About Me," "Projects," and "Contact."
- A contact form that sends data to the Flask backend.

## Project Structure
