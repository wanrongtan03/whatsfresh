import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        """Connect to the SQLite database."""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        # Ensure tables are created upon initialization
        self.create_tables()

    def create_tables(self):
        """Create tables in the database if they don't exist already."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                expiry_date DATE NOT NULL
            )
        ''')
        self.connection.commit()

    def add_item(self, item):
        """Add an item to the inventory."""
        self.cursor.execute('''
            INSERT INTO inventory (name, quantity, expiry_date) 
            VALUES (?, ?, ?)
        ''', (item['name'], item['quantity'], item['expiry_date']))
        self.connection.commit()

    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        self.cursor.execute('''
            DELETE FROM inventory WHERE id = ?
        ''', (item_id,))
        self.connection.commit()

    def update_item(self, item):
        """Update an item's details in the inventory."""
        self.cursor.execute('''
            UPDATE inventory
            SET name = ?, quantity = ?, expiry_date = ?
            WHERE id = ?
        ''', (item['name'], item['quantity'], item['expiry_date'], item['id']))
        self.connection.commit()

    def get_inventory(self):
        """Retrieve the current inventory from the database."""
        self.cursor.execute('SELECT * FROM inventory')
        return self.cursor.fetchall()

# Example usage:
db_manager = DatabaseManager('inventory.db')

# Adding an item
db_manager.add_item({
    'name': 'Apples',
    'quantity': 10,
    'expiry_date': '2024-01-20'
})

# Updating an item
db_manager.update_item({
    'id': 1,  # Assuming the item has ID 1
    'name': 'Apples',
    'quantity': 5,
    'expiry_date': '2024-01-25'
})

# Removing an item
db_manager.remove_item(1)

# Getting the inventory
inventory = db_manager.get_inventory()
print(inventory)
