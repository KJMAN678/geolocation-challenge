import json
from decimal import Decimal

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Location


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "stock/index.html")


def clicked(request: HttpRequest) -> HttpResponse:
    context = {"message": "Button clicked!"}
    return render(request, "stock/clicked.html", context)


@csrf_exempt
@require_POST
def save_location(request: HttpRequest) -> HttpResponse:
    try:
        data = json.loads(request.body)
        latitude = Decimal(str(data.get("latitude")))
        longitude = Decimal(str(data.get("longitude")))

        location = Location.objects.create(latitude=latitude, longitude=longitude)

        context = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "created_at": location.created_at,
        }
        return render(request, "stock/location_saved.html", context)
    except (json.JSONDecodeError, TypeError, ValueError) as e:
        context = {"error": str(e)}
        return render(request, "stock/location_error.html", context, status=400)
