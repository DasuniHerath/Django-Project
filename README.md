# Django-Project

This is a PHP-based web application that interacts with a MySQL database to search and display data stored in the 'summary','school','class','Assesment_Areas','student','Answers','Awards','Subject'  tables. It also includes a Python script to import data from CSV files into the MySQL database.


## Features

- Search functionality to retrieve data from the MySQL database.
- Data import from CSV files into the MySQL database.
- Basic error handling feature.


## Requirements

- PHP (version 8.2.0) - to create web browser
- Apache - local web server 
- MySQL  - store database
- Python (version 3.11.3) with pandas library - only used for data import.


## Setup

1. Clone the repository from GitHub.
2. Ensure that required versions of PHP, XAMPP server,Python and MySQL are installed.
3. Update the MySQL connection parameters(host,database name,user,password) in the `frontEnd.php`and `import_csv_to_mysql.py` to match your database.
4. Place the `frontEnd.php` in XAMPP server's root directory (like \xampp\htdocs).

## Usage

1. Open a web browser and navigate to the location where you placed the `frontEnd.php` file.
2. Enter the table name and click on the "Show Details" button.

