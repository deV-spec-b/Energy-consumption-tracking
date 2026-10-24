import json
from db.database import get_connection

OBJECTS_FILE = "data/objects.json"
METERS_FILE = "data/meters.json"
READINGS_FILE = "data/readings.json"
PERIODS_FILE = "data/periods.json"


def load_json(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def import_objects(conn):
    objects = load_json(OBJECTS_FILE)
    conn.executemany(
        """
        INSERT INTO accounting_objects (id, address, object_type, area)
        VALUES (?, ?, ?, ?)
        """,
        [
            (
                obj["id"],
                obj["address"],
                obj["object_type"],
                obj.get("area"),
            )
            for obj in objects
        ],
    )


def import_meters(conn):
    meters = load_json(METERS_FILE)
    conn.executemany(
        """
        INSERT INTO meters (id, number, meter_type, object_id, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (
                meter["id"],
                meter["number"],
                meter["meter_type"],
                meter["object_id"],
                meter.get("status"),
            )
            for meter in meters
        ],
    )


def import_periods(conn):
    periods = load_json(PERIODS_FILE)
    conn.executemany(
        """
        INSERT INTO periods (id, name, start_date, end_date)
        VALUES (?, ?, ?, ?)
        """,
        [
            (
                period["id"],
                period["name"],
                period["start_date"],
                period["end_date"],
            )
            for period in periods
        ],
    )


def import_readings(conn):
    readings = load_json(READINGS_FILE)
    conn.executemany(
        """
        INSERT INTO readings (id, meter_id, value, reading_date)
        VALUES (?, ?, ?, ?)
        """,
        [
            (
                reading["id"],
                reading["meter_id"],
                reading["value"],
                reading["reading_date"],
            )
            for reading in readings
        ],
    )


def main():
    conn = get_connection()
    try:
        import_objects(conn)
        import_meters(conn)
        import_periods(conn)
        import_readings(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()