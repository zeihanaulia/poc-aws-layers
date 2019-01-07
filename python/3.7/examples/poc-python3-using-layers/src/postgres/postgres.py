
import psycopg2

def Database(dbstr):
    try:
        c = psycopg2.connect(dbstr)
        c.close()
        print(str(c))
        connection = True
    except (Exception, psycopg2.DatabaseError) as e :
        print(str(e))
        connection = False
        c.close()

    return connection