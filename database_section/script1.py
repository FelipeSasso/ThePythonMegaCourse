# import psycopg2
import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='porzarquon1442' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='porzarquon1442' host='localhost' port='5432'")
    cur=conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='porzarquon1442' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    cur.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='porzarquon1442' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item, ))
    conn.commit()
    cur.close()

def update(quantity, price, item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='porzarquon1442' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    cur.close()

create_table()
insert("Agua", 10, 5.0)
# delete("Agua")
print view()
print "\n"
update(555, 1.0, "Agua")
print view()
# print view()
# update(11, 0, "Wine Glass")
# print view()
