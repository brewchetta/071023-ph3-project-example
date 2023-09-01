from . import CONN, CURSOR

class CaveProperty:

    # MAGIC METHODS #

    def __init__(self, name, price_in_rocks, id=None):
        self.name = name
        self.price_in_rocks = price_in_rocks
        self.id = id

    def __repr__(self):
        return f"CaveProperty(id={self.id}, name={self.name}, price_in_rocks={self.price_in_rocks})"

    # TABLE METHODS #

    @classmethod
    def create_table(cls):
        sql="""
        CREATE TABLE IF NOT EXISTS cave_properties (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price_in_rocks INTEGER
        )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql="DROP TABLE cave_properties"
        CURSOR.execute(sql)

    # SQL CREATE METHODS #

    # creates new property based on instance attributes
    def create(self):
        sql="INSERT INTO cave_properties (name, price_in_rocks) VALUES (?,?)"
        CURSOR.execute(sql, [self.name, self.price_in_rocks])
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self

    # SQL SELECT METHODS #

    # returns one property by id
    @classmethod
    def select_by_id(cls, id):
        sql="SELECT * FROM cave_properties WHERE id = ?"
        row = CURSOR.execute(sql, [id]).fetchone()
        if row:
            return CaveProperty(id=row[0], name=row[1], price_in_rocks=row[2])

    # returns one property by name
    @classmethod
    def select_by_name(cls, name):
        sql="SELECT * FROM cave_properties WHERE name = ?"
        row = CURSOR.execute(sql, [name]).fetchone()
        if row:
            return CaveProperty(id=row[0], name=row[1], price_in_rocks=row[2])

    # returns list of all properties
    @classmethod
    def select_all(cls):
        sql="SELECT * FROM cave_properties"
        rows=CURSOR.execute(sql),fetchall()

        return [CaveProperty(id=r[0], name=r[1], price_in_rocks=r[2]) for r in rows]
