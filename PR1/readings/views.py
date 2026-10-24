from django.shortcuts import render
from db.database import get_connection


def readings_list(request):
    conn = get_connection()
    readings = conn.execute(
        """
        SELECT 
            r.id,
            r.value,
            r.reading_date,
            m.meter_type,
            m.number,
            o.address
        FROM readings r
        JOIN meters m ON r.meter_id = m.id
        JOIN accounting_objects o ON m.object_id = o.id
        ORDER BY r.reading_date DESC
        """
    ).fetchall()
    conn.close()
    return render(request, "readings/reading_list.html", {"readings": readings})


def reading_detail(request, reading_id):
    conn = get_connection()
    reading = conn.execute(
        """
        SELECT 
            r.id, r.value, r.reading_date,
            m.meter_type, m.number, o.address
        FROM readings r
        JOIN meters m ON r.meter_id = m.id
        JOIN accounting_objects o ON m.object_id = o.id
        WHERE r.id = ?
        """,
        (reading_id,),
    ).fetchone()
    conn.close()
    return render(
        request,
        "readings/reading_detail.html",
        {"reading": reading},
        status=404 if reading is None else 200,
    )