from django.shortcuts import render

from models.objects import find_object_by_id
from storage import load_objects


def objects_list(request):
    objects_list_data = load_objects("data/objects.json")
    context = {
        "objects": objects_list_data,
    }
    return render(request, "objects/object_list.html", context)


def object_detail(request, object_id):
    objects_list_data = load_objects("data/objects.json")
    accounting_object = find_object_by_id(objects_list_data, object_id)
    context = {
        "accounting_object": accounting_object,
    }
    return render(
        request,
        "objects/object_detail.html",
        context,
        status=404 if accounting_object is None else 200,
    )