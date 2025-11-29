import json
from decimal import Decimal, InvalidOperation
from json import JSONDecodeError

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

        if not (Decimal("-90") <= latitude <= Decimal("90")):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (Decimal("-180") <= longitude <= Decimal("180")):
            raise ValueError("Longitude must be between -180 and 180.")

        location = Location.objects.create(latitude=latitude, longitude=longitude)

        context = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "created_at": location.created_at,
        }
        return render(request, "stock/location_saved.html", context)
    except (
        JSONDecodeError,
        AttributeError,
        TypeError,
        ValueError,
        InvalidOperation,
    ) as e:
        context = {"error": f"Invalid request data: {e}"}
        return render(request, "stock/location_error.html", context, status=400)
