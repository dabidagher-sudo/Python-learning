#SQLite Data Source

import sqlite3

from src.data_source import DataSource

class SQLiteDataSource(DataSource):

    def __init__(self, database_file):
        self.database_file = database_file
    
    def get_connection(self):
        return sqlite3.connect(self.database_file)
    
    def get_total_records(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM machine_data"
        )

        result = cursor.fetchone()[0]

        conn.close()

        return result
    
    def get_total_alarms(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM machine_data
            WHERE result != 'Ok'
            """
        )

        result = cursor.fetchone()[0]

        conn.close()

        return result
    
    def get_critical_alarms(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM machine_data
            WHERE result LIKE '%Critical%'
            """
        )

        result = cursor.fetchone()[0]

        conn.close()

        return result
    
    def get_alarm_summary(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT result, COUNT(*)
            FROM machine_data
            WHERE result != 'Ok'
            GROUP BY result
            ORDER BY COUNT(*) DESC
            """
        )

        result = cursor.fetchall()

        conn.close()

        return result
    
    def get_factory_inventory(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT machine_id,
                   machine_type,
                    status
            FROM machine_data
            GROUP BY machine_id
            ORDER BY machine_id
            """
        )

        result = cursor.fetchall()

        conn.close()

        return result
    
    def get_running_machines(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
        """
        SELECT COUNT(*)
        FROM machine_data
        WHERE status = 'RUNNING'
        """
        )

        result = cursor.fetchone()[0]
        conn.close()

        return result