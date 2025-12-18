# 🛰️ ISS Real-Time Data Pipeline

## Overview
An automated ETL (Extract, Transform, Load) pipeline that tracks the International Space Station in real-time. The system ingests telemetry data from the OpenNotify API, stores it in a SQLite warehouse, and exports it for visualization in Tableau.

<img width="1009" height="578" alt="Dashboard" src="https://github.com/user-attachments/assets/d5b5ae54-904c-40c0-9bef-06664d1d36b4" />

## Architecture
* **Extraction:** Python `requests` module polls the ISS API every 5 seconds.
* **Storage:** Data is normalized and stored in a local `sqlite3` database (`iss.db`).
* **Export:** Pandas script converts SQL tables to CSV for consumption by BI tools.
* **Visualization:** Connected to Tableau for geospatial mapping.

## How to Run
1.  **Start the Tracker:**
    ```bash
    python iss_tracker.py
    ```
    *The script will initialize the database and begin logging coordinates.*

2.  **Export Data:**
    ```bash
    python export_data.py
    ```
    *Generates `iss_history.csv` for analysis.*

## Tools Used
* Python 3.x
* SQLite / SQL
* Pandas
* Tableau
