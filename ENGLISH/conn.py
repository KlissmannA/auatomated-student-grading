import psycopg2

### CONNECTION TO POSTGRESQL ###
def connection():
    try:
        # Read the file containing the credentials
        with open("key_db.txt", "r") as file:  
            content = [line.strip() for line in file.readlines()]  # Remove line breaks and extra spaces
        
        # Ensure the file has the expected format
        if len(content) < 5:
            raise ValueError("The key_db.txt file must contain at least 5 lines (database, user, password, host, port).")
        
        # Create the database connection
        conn = psycopg2.connect(
            database=content[0],  # Database name
            user=content[1],      # Database username
            password=content[2],  # Database password
            host=content[3],      # Database IP or hostname
            port=content[4]       # Database port
        )
        
        print("Connection to the database was successful.")
        return conn

    except FileNotFoundError:
        print("The file 'key_db.txt' does not exist. Please check the file name and path.")
    except ValueError as ve:
        print(f"Configuration error: {ve}")
    except psycopg2.OperationalError as oe:
        print(f"Database connection error: {oe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

