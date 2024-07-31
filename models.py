from database import Database

class Users:
    @staticmethod
    def register_user(username, email, gender, mobile, dob, joining_date):
        db = Database()
        query = "INSERT INTO users (username, email, gender, mobile, dob, joiningDate) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (username, email, gender, mobile, dob, joining_date)
        db.get_response(query, values)
        return True 


    @staticmethod
    def fetch_users_with_address():
        db = Database()
        query = "SELECT u.userId, u.username, u.email, a.streetName, a.state, a.city, a.zipcode FROM users u JOIN addresses a ON u.userId = a.userId"
        return db.fetch_data(query)

class Address:
    @staticmethod
    def add_address(user_id, street_name, state, city, zipcode):
        db = Database()
        query = "INSERT INTO addresses (userId, streetName, state, city, zipcode) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id, street_name, state, city, zipcode)
        db.get_response(query, values)
        return True
        return "Address added successfully."

    @staticmethod
    def fetch_users_with_address():
        query = "SELECT u.userId, u.username, u.email, a.streetName, a.state, a.city, a.zipcode FROM users u JOIN addresses a ON u.userId = a.userId"
        return Database.fetch_data(query)

class Admins:
    @staticmethod
    def add_admin(username, passkey, full_name):
        db = Database()
        query = "INSERT INTO admins (username, passKey, fullName) VALUES (%s, %s, %s)"
        values = (username, passkey, full_name)
        db.get_response(query, values)
        return "Admin added successfully."


class Plans:
    @staticmethod
    def add_plan(plan_name, description, validity, amount):
        db = Database()
        query = "INSERT INTO plans (planName, description, validity, amount) VALUES (%s, %s, %s, %s)"
        values = (plan_name, description, validity, amount)
        db.get_response(query, values)
        return "Plan added successfully."


class Subscriptions:
    @staticmethod
    def enroll_user(user_id, plan_id, purchase_date, expiration_date, renewal_status):
        db = Database()
        query = "INSERT INTO Subscriptions (userId, planId, purchaseDate, expirationDate, renewalStatus) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id, plan_id, purchase_date, expiration_date, renewal_status)
        db.get_response(query, values)
        return "User enrolled successfully."
        
class EnrollTo:
    @staticmethod
    def enroll_to_sports_timetable(evenr_Id, event_name, description, start_time, end_time, location):
        db = Database()
        query = "INSERT INTO events (eventId, eventName, description, startTime, endTime, location) VALUES (%s, %s, %s, %s, %s)"
        values = (event_name, description, start_time, end_time, location)
        db.get_response(query, values)
        return "Event enrolled successfully."

class HealthStatus:
    @staticmethod
    def add_health_status(user_id, calorie, height, weight, fat_index, suggestions, date_recorded):
        db = Database()
        query = "INSERT INTO HealthStatus (userId, calorie, height, weight, fatIndex, suggestions, dateRecorded) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (user_id, calorie, height, weight, fat_index, suggestions, date_recorded)
        db.get_response(query, values)(query, values)
        return "Health status added successfully."

    @staticmethod
    def fetch_users_with_health_suggestions():
        db = Database()
        query = "SELECT u.username, h.suggestions FROM users u JOIN HealthStatus h ON u.userId = h.userId WHERE h.suggestions IS NOT NULL"
        return db.fetch_data(query)


class LoginLogs:
    @staticmethod
    def add_login_log(user_id, action):
        db = Database()
        query = "INSERT INTO LoginLogs (userId, action) VALUES (%s, %s)"
        values = (user_id, action)
        db.get_response(query, values)(query, values)
        return "Login log added successfully."

    @staticmethod
    def fetch_last_login_details():
        db = Database()
        query = "SELECT userId, MAX(timestamp) AS lastLogin FROM LoginLogs GROUP BY userId"
        return db.fetch_data(query)
        
class Events:
    @staticmethod
    def add_event(event_name, description, start_time, end_time, location):
        db = Database()
        query = "INSERT INTO events (eventName, description, startTime, endTime, location) VALUES (%s, %s, %s, %s, %s)"
        values = (event_name, description, start_time, end_time, location)
        db.get_response(query, values)
        return "Event added successfully."

    @staticmethod
    def fetch_events():
        db = Database()
        query = "SELECT * FROM events"
        return db.fetch_data(query)

class SportsTimetable:
    @staticmethod
    def add_sports_event(event_name, description, start_time, end_time, location):
        db = Database()
        query = "INSERT INTO events (eventName, description, startTime, endTime, location) VALUES (%s, %s, %s, %s, %s)"
        values = (event_name, description, start_time, end_time, location)
        db.get_response(query, values)
        return "Sports event added successfully."


class Managers:
    @staticmethod
    def add_manager(name):
        db = Database()
        query = "INSERT INTO managers (name) VALUES (%s)"
        values = (name,)
        db.get_response(query, values)
        return "Manager added successfully."

    @staticmethod
    def fetch_managers_and_agents():
        db = Database()
        query = "SELECT 'Manager' AS role, managerId AS id, name FROM managers UNION SELECT 'Agent' AS role, agentId AS id, name FROM agents"
        return db.fetch_data(query)


class Scouts:
    @staticmethod
    def add_scout(name):
        db = Database()
        query = "INSERT INTO scouts (name) VALUES (%s)"
        values = (name,)
        db.get_response(query, values)
        return "Scout added successfully."


class Advertisements:
    @staticmethod
    def add_advertisement(name):
        db = Database()
        query = "INSERT INTO advertisements (name) VALUES (%s)"
        values = (name,)
        db.get_response(query, values)
        return "Advertisement added successfully."


class Agents:
    @staticmethod
    def add_agent(name):
        db = Database()
        query = "INSERT INTO agents (name) VALUES (%s)"
        values = (name,)
        db.get_response(query, values)
        return "Agent added successfully."