from fastapi import FastAPI
import mysql.connector


credential = {'user':'name',
        'password':'paswd',
        'host':'ip',
        'database':'db_name'}
connection = mysql.connector.connect(**credential)
cursor = connection.cursor()



app = FastAPI()
@app.get("/")
def fetch_details():
        query = "SELECT * FROM student"
        cursor.execute(query)
        result = cursor.fetchall()
        return result



@app.post("/reverse")
def reverse_string(inp_string: str):
    rev_string = inp_string[::-1]
    return {"output": rev_string}