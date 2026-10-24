from django.shortcuts import render
from db.database import get_connection


def meters_list(request):
    conn = get_connection()
    meters = conn.execute(
        """
        SELECT 
            m.id,
            m.number,
            m.meter_type,
            m.status,
            o.address
        FROM meters m
        JOIN accounting_objects o ON m.object_id = o.id
        ORDER BY o.address
        """
    ).fetchall()
    conn.close()
    return render(request, "meters/meter_list.html", {"meters": meters})


def meter_detail(request, meter_id):
    conn = get_connection()
    meter = conn.execute(
        """
        SELECT m.id, m.number, m.meter_type, m.status, o.address
        FROM meters m
        JOIN accounting_objects o ON m.object_id = o.id
        WHERE m.id = ?
        """,
        (meter_id,),
    ).fetchone()
    conn.close()
    return render(
        request,
        "meters/meter_detail.html",
        {"meter": meter},
        status=404 if meter is None else 200,
    )