import pandas as pd
from mysql.connector import connect, Error
import uuid

# MySQL connection parameters
db_config = {
    'host': 'localhost',
    'database': 'world',
    'user': 'root',
    'password': 'root'
}

# CSV file path
csv_file_path = r'C:\Users\User\Downloads\Interview_dataset(1)\test\test1.csv'

try:
    # Connect to MySQL
    with connect(**db_config) as connection:
        # Create a cursor object
        cursor = connection.cursor()

        # Read CSV file into pandas DataFrame
        df = pd.read_csv('C:\\Users\\User\\Downloads\\Interview_dataset(1)\\test\\test1.csv')

        # Generate random IDs for each row
        df['School_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Assessment_Area_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Award_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Class_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Student_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Subject_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Category_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Answer_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]
        df['Correct_answer_Id'] = [str(uuid.uuid4()) for _ in range(len(df))]    

        # Define SQL query to create table based on DataFrame columns
        table_creation_query = """
        CREATE TABLE IF NOT EXISTS summary (
            School_Id VARCHAR(36),
            Assessment_Area_Id VARCHAR(36),
            Award_Id VARCHAR(36),
            Class_Id VARCHAR(36),
            Student_Id VARCHAR(36),
            Subject_Id VARCHAR(36),
            Category_Id VARCHAR(36),
            Answer_Id VARCHAR(36),
            Correct_answer_Id VARCHAR(36),
            Year_level_name VARCHAR(10),
            Correct_Answer CHAR,
            Sydney_Participant INT,
            Student_score DOUBLE,
            Participant INT,
            Correct_answer_percentage_per_class DOUBLE,
            Sydney_Percentile INT
        )"""

        # Execute table creation query
        cursor.execute(table_creation_query)

        # Insert DataFrame records into MySQL table
        for _, row in df.iterrows():
            insert_query = """
            INSERT INTO summary (
                School_Id, Assessment_Area_Id, Award_Id, Class_Id, Student_Id,
                Subject_Id, Category_Id, Answer_Id, Correct_answer_Id,
                Year_level_name, Correct_Answer, Sydney_Participant,
                Student_score, Participant, Correct_answer_percentage_per_class,
                Sydney_Percentile
            ) VALUES (
                %(School_Id)s, %(Assessment_Area_Id)s, %(Award_Id)s, %(Class_Id)s, %(Student_Id)s,
                %(Subject_Id)s, %(Category_Id)s, %(Answer_Id)s, %(Correct_answer_Id)s,
                %(Year_level_name)s, %(Correct_Answer)s, %(Sydney_Participant)s,
                %(Student_score)s, %(Participant)s, %(Correct_answer_percentage_per_class)s,
                %(Sydney_Percentile)s
            )"""
            row_dict = row.to_dict()
            row_dict['Year_Level_name'] = row['Year Level']
            row_dict['Correct_Answer'] = row['Correct Answers']
            row_dict['Sydney_Participant'] = row['sydney_participants']
            row_dict['Student_score'] = row['student_score']
            row_dict['Participant'] = row['participant']
            row_dict['Correct_answer_percentage_per_class'] = row['correct_answer_percentage_per_class']
            row_dict['Sydney_Percentile'] = row['sydney_percentile']
            cursor.execute(insert_query, row.to_dict())  # Convert DataFrame row to dictionary

        # Commit changes
        connection.commit()
        print("CSV data imported successfully into MySQL.")

except Error as e:
    print(f"Error: {e}")
