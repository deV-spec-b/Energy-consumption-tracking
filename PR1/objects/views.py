from django.shortcuts import render
from db.database import get_connection


def objects_list(request):
    conn = get_connection()
    objects = conn.execute(
        """
        SELECT id, address, object_type, area
        FROM accounting_objects
        ORDER BY address
        """
    ).fetchall()
    conn.close()
    return render(request, "objects/object_list.html", {"objects": objects})


def object_detail(request, object_id):
    conn = get_connection()
    accounting_object = conn.execute(
        """
        SELECT id, address, object_type, area
        FROM accounting_objects
        WHERE id = ?
        """,
        (object_id,),
    ).fetchone()
    conn.close()
    return render(
        request,
        "objects/object_detail.html",
        {"accounting_object": accounting_object},
        status=404 if accounting_object is None else 200,
    )