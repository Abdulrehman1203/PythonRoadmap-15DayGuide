import psycopg2


class Wrapper:
    def __init__(self, host, dbname, user, password, port):
        """
        Initialize the database wrapper class with connection parameters.

        :param host: Database host
        :param dbname: Database name
        :param user: Username for database connection
        :param password: Password for the user
        :param port: Port number for the database connection
        """
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.dbname = dbname
        self.cur = None
        self.conn = None

    def connect_db(self):
        """
        Establishes a connection to the PostgreSQL database.
        """
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cur = self.conn.cursor()
            print('Connected to PostgreSQL')
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def close_db(self):
        """
        Closes the connection and cursor for the database.
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Connection closed.")

    def create(self):
        """
        Creates the 'cars' table in the database with the specified schema.
        """
        try:
            self.cur.execute(
                """
                CREATE TABLE IF NOT EXISTS cars (
                    car_make varchar(255), 
                    car_model varchar(255), 
                    car_year int, 
                    car_type varchar(50)
                );"""
            )
            self.conn.commit()
            print("Table created successfully")
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
            self.conn.rollback()

    def insert(self, car_make: str, car_model: str, car_year: int, car_type: str) -> None:
        """
        Inserts a new record into the 'cars' table.

        :param car_make: Car manufacturer
        :param car_model: Car model
        :param car_year: Year of manufacture
        :param car_type: Type of the car
        """
        try:
            self.cur.execute(
                """INSERT INTO cars (car_make, car_model, car_year, car_type) 
                   VALUES (%s, %s, %s, %s);""",
                (car_make, car_model, car_year, car_type)
            )
            self.conn.commit()
            print("Data inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")
            self.conn.rollback()

    def update(self, car_make: str, car_model: str, car_year: int, car_type: str) -> None:
        """
        Updates an existing record in the 'cars' table based on user input.

        :param car_make: New car manufacturer to update
        :param car_model: New car model to update
        :param car_year: New year of manufacture to update
        :param car_type: New car type to update
        """
        temp_car_model = input("Enter car model you wish to update: ").lower()
        temp_car_year = int(input("Enter car year you wish to update: "))

        try:
            print(f"Updating record where model = {temp_car_model} and year = {temp_car_year}")
            self.cur.execute(
                """UPDATE cars 
                   SET car_make = %s, car_model = %s, car_year = %s, car_type = %s 
                   WHERE car_year = %s AND car_model = %s;""",
                (car_make, car_model, car_year, car_type, temp_car_year, temp_car_model)
            )
            self.conn.commit()
            print("Update successful.")
        except psycopg2.Error as e:
            print(f"Error updating record: {e}")
            self.conn.rollback()

    def delete(self):
        """
        Drops the 'cars' table from the database.
        """
        try:
            self.cur.execute("DROP TABLE IF EXISTS cars;")
            self.conn.commit()
            print("Table deleted successfully")
        except psycopg2.Error as e:
            print(f"Error deleting table: {e}")
            self.conn.rollback()

    def display(self):
        """
        Displays all records from the 'cars' table.
        """
        try:
            self.cur.execute("SELECT * FROM cars;")
            records = self.cur.fetchall()
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")
        except psycopg2.Error as e:
            print(f"Error displaying records: {e}")

    def close(self):
        """
        Closes the cursor and connection when the application is done.
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Connection closed.")


# Main execution loop
if __name__ == "__main__":
    wrapper = Wrapper('localhost', 'postgres', 'postgres', '5571', '5433')

    while True:
        print("\nMenu:")
        print("1. Connect to PostgreSQL")
        print("2. Create table")
        print("3. Insert record")
        print("4. Update record")
        print("5. Delete table")
        print("6. Display records")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            wrapper.connect_db()
        elif choice == 2:
            wrapper.create()
        elif choice == 3:
            car_make = input("Enter car make: ")
            car_model = input("Enter car model: ")
            car_year = int(input("Enter car year: "))
            car_type = input("Enter car type: ")
            wrapper.insert(car_make, car_model, car_year, car_type)
        elif choice == 4:
            car_make = input("Enter new car make: ")
            car_model = input("Enter new car model: ")
            car_year = int(input("Enter new car year: "))
            car_type = input("Enter new car type: ")
            wrapper.update(car_make, car_model, car_year, car_type)
        elif choice == 5:
            wrapper.delete()
        elif choice == 6:
            wrapper.display()
        elif choice == 7:
            wrapper.close()
            break
        else:
            print("Invalid choice. Please try again.")
