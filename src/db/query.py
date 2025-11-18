# src/db/query.py
from sqlite3 import Error

def execute_query(connection, query, params=None):
    """
    Executes an INSERT, UPDATE, or DELETE query on the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    query : str
        The SQL query to execute.
    params : tuple or list, optional
        Optional parameters to prevent SQL injection.

    Returns
    -------
    int
        The number of rows affected by the query, or 0 if an error occurred.
    """
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        # Save changes to the database
        connection.commit()
        return cursor.rowcount
    except Error as e:
        print(f"The error '{e}' occurred")
        return 0


def execute_read_query(connection, query, params=None):
    """
    Executes a SELECT query on the database and returns the results.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    query : str
        The SQL SELECT query to execute.
    params : tuple or list, optional
        Optional parameters to prevent SQL injection.

    Returns
    -------
    list of tuple
        A list of rows returned by the query. Returns an empty list if an error occurred.
    """
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        # Fetch all rows from the result set
        return cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
        return []