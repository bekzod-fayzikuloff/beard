from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Beard


@api_view(["GET"])
def index(
        request: Request,
        width: int,
        height: int
) -> HttpResponse:
    import random
    queryset = list(Beard.objects.all())
    colored = "g" not in set(request.path.split("/"))

    if not queryset:
        return Response(dict())

    beard = random.choice(queryset)
    image = beard.resize_image(width, height, colored=colored)

    response = HttpResponse(content_type="image/png")
    image.save(response, "JPEG")
    return response
