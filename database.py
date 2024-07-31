import os
import pymysql.cursors


class Database:

    def connect(self):
        """
        Creates a connection with the database.
        """
        db_host = os.environ.get("DB_HOST")
        db_username = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")
        db_name = os.environ.get("DB_NAME")

        try:
            conn = pymysql.connect(host=db_host,
                                   port=3306,
                                   user=db_username,
                                   password=db_password,
                                   db=db_name,
                                   charset="utf8mb4",
                                   cursorclass=pymysql.cursors.DictCursor)
            print("Bot connected to database {}".format(db_name))
            return conn
        except pymysql.err.OperationalError as err:
            print(f"An error has occurred: {err}")
            print("\n")
            return None

    def get_response(self, query, values=None, fetch=False):
        """
        Execute the SQL query and return the response.

        Args:
        - query: The SQL query with wildcards (if applicable) to avoid injection attacks.
        - values: The values passed in the query.
        - fetch: If set to True, then the method fetches data from the database (i.e., with SELECT).

        Returns:
        - response: The result of the SQL operation.
        """
        connection = self.connect()
        if connection is None:
            return None
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                response = cursor.fetchall() if fetch else None
                connection.commit()
                return response
        except pymysql.Error as e:
            print(f"Error executing query: {e}")
        finally:
            if connection is not None:
                connection.close()

    @staticmethod
    def fetch_data(query):
        """
        Fetch data from the database.

        Args:
        - query: The SQL query to execute.

        Returns:
        - data: The fetched data.
        """
        connection = Database().connect()
        if connection is None:
            return None
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()
                return data
        except pymysql.Error as e:
            print(f"Error executing query: {e}")
        finally:
            if connection is not None:
                connection.close()


class Users:

    @staticmethod
    def register_user(username, email, gender, mobile, dob, joining_date):
        return Database().get_response("INSERT INTO users (username, email, gender, mobile, dob, joiningDate) VALUES (%s, %s, %s, %s, %s, %s)", (username, email, gender, mobile, dob, joining_date))

    @staticmethod
    def fetch_users_with_address():
        return Database().fetch_data("SELECT u.userId, u.username, u.email, a.streetName, a.state, a.city, a.zipcode FROM users u JOIN addresses a ON u.userId = a.userId")


class Address:

    @staticmethod
    def add_address(user_id, street_name, state, city, zipcode):
        return Database().get_response("INSERT INTO addresses (userId, streetName, state, city, zipcode) VALUES (%s, %s, %s, %s, %s)", (user_id, street_name, state, city, zipcode))


class Admins:

    @staticmethod
    def add_admin(username, passkey, full_name):
        return Database().get_response("INSERT INTO admins (username, passKey, fullName) VALUES (%s, %s, %s)", (username, passkey, full_name))


class Plans:

    @staticmethod
    def add_plan(plan_name, description, validity, amount):
        return Database().get_response("INSERT INTO plans (planName, description, validity, amount) VALUES (%s, %s, %s, %s)", (plan_name, description, validity, amount))


class Subscriptions:

    @staticmethod
    def enroll_user(user_id, plan_id, purchase_date, expiration_date, renewal_status):
        return Database().get_response("INSERT INTO Subscriptions (userId, planId, purchaseDate, expirationDate, renewalStatus) VALUES (%s, %s, %s, %s, %s)", (user_id, plan_id, purchase_date, expiration_date, renewal_status))


class HealthStatus:

    @staticmethod
    def add_health_status(user_id, calorie, height, weight, fat_index, suggestions, date_recorded):
        return Database().get_response("INSERT INTO HealthStatus (userId, calorie, height, weight, fatIndex, suggestions, dateRecorded) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user_id, calorie, height, weight, fat_index, suggestions, date_recorded))

    @staticmethod
    def fetch_users_with_health_suggestions():
        return Database().fetch_data("SELECT u.username, h.suggestions FROM users u JOIN HealthStatus h ON u.userId = h.userId WHERE h.suggestions IS NOT NULL")


class LoginLogs:
    @staticmethod
    def add_login_log(user_id, action, timestamp):
        db = Database()
        query = "INSERT INTO LoginLogs (userId, action, timestamp) VALUES (%s, %s, %s)"
        values = (user_id, action, timestamp)
        db.get_response(query, values)
        return True 

    @staticmethod
    def fetch_last_login_details():
        db = Database()
        query = "SELECT userId, MAX(timestamp) AS lastLogin FROM LoginLogs GROUP BY userId"
        return db.fetch_data(query)

class SportsTimetable:

    @staticmethod
    def add_sports_event(event_name, description, start_time, end_time, location):
        return Database().get_response("INSERT INTO events (eventName, description, startTime, endTime, location) VALUES (%s, %s, %s, %s, %s)", (event_name, description, start_time, end_time, location))


class Managers:

    @staticmethod
    def add_manager(name):
        return Database().get_response("INSERT INTO managers (name) VALUES (%s)", (name,))

    @staticmethod
    def fetch_managers_and_agents():
        return Database().fetch_data("SELECT 'Manager' AS role, managerId AS id, name FROM managers UNION SELECT 'Agent' AS role, agentId AS id, name FROM agents")


class Scouts:

    @staticmethod
    def add_scout(name):
        return Database().get_response("INSERT INTO scouts (name) VALUES (%s)", (name,))


class Advertisements:

    @staticmethod
    def add_advertisement(name):
        return Database().get_response("INSERT INTO advertisements (name) VALUES (%s)", (name,))


class Agents:

    @staticmethod
    def add_agent(name):
        return Database().get_response("INSERT INTO agents (name) VALUES (%s)", (name,))
