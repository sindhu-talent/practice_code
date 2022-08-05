import psycopg2
query = 'SELECT * FROM public."Euregion" '
con = psycopg2.connect(
            host = "localhost",
            database = "sindhu",
            user =  "postgres",
            password = sindhu@166
          )

#cursor
cur = con.cursor()
#execute query
cur.execute(query)
rows = cur.fetchall()
for i in rows:
     print(i)
#close the cursor
cur.close()
#close the connection
con.close()

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:sindhu@166localhost:5432/sindh')