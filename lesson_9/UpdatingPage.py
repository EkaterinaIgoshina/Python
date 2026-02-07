from sqlalchemy import create_engine, inspect, text


class Updating:
    scripts = {
        "select": text("SELECT * FROM users"),
        "select_max_id": text("SELECT MAX(user_id) FROM users"),
        "delete_by_email": text("DELETE FROM users WHERE users.user_email = :new_user_email"),
        "insert_new": text("INSERT INTO users(user_email) VALUES (:new_user_email)"),
        "update_email": text("UPDATE users SET user_email = :new_email WHERE user_email = :old_email"),
    }


    def __init__(self):
        with open("pass.txt", "r") as file:
            self.connection_string = file.read()
        self.db = create_engine(self.connection_string)

    def get_tables(self):
        inspector = inspect(self.db)
        res = inspector.get_table_names()
        assert res[0] == 'users'

    def insert_new(self, value_new):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["insert_new"], value_new)
        transaction.commit()
        conn.close()

    def update_email(self, old_email, new_email):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["update_email"], {"old_email": old_email, "new_email": new_email})
        transaction.commit()
        conn.close()

    def delete_new(self, value_deleted):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["delete_by_email"], value_deleted)
        transaction.commit()
        conn.close()

    def get_max_id(self):
        conn = self.db.connect()
        result = conn.execute(self.scripts["select_max_id"])
        max_id = result.fetchone()[0]
        conn.close()
        return max_id

    def get_list(self):
        conn = self.db.connect()
        result = conn.execute(self.scripts["select"])
        rows = len(result.mappings().all())
        conn.close()
        return rows

