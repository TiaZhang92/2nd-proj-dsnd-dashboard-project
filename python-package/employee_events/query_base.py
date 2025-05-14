# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
import sqlite3
import pandas as pd
from pathlib import Path

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase:
    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE
    name = ""
    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names(self):
        
        # Return an empty list
        # YOUR CODE HERE
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    def event_counts(self, id):
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
        query = f"""
        SELECT 
            event_date,
            SUM(positive_events) as total_positive_events,
            SUM(negative_events) as total_negative_events
        FROM 
            employee_events
        WHERE 
            {self.name}_id = {id}
        GROUP BY 
            event_date
        ORDER BY 
            event_date
        """  
        # Execute the query and return as dataframe
        conn = sqlite3.connect('python-package/employee_events/employee_events.db')
        result = pd.read_sql_query(query, conn)
        conn.close()
        return result 
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE
        query = f"""
        SELECT 
            note_date,
            note
        FROM 
            notes
        WHERE 
            {self.name}_id = {id}
        ORDER BY 
            note_date DESC
        """
        # Execute the query and return as dataframe
        conn = sqlite3.connect('python-package/employee_events/employee_events.db')
        result = pd.read_sql_query(query, conn)
        conn.close()
        return result

