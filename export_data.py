import sqlite3
import pandas as pd

connection = sqlite3.connect("iss.db")
df = pd.read_sql_query("SELECT * FROM iss_history", connection)
df.to_csv("iss_history.csv", index=False)
connection.close()

print("'iss_data' has been exported.")
print(f"Exported: {len(df)} rows of data.")
