from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from currency_app.ml.CheckCurrency import CheckCurrency

# Create your views here.

def home(request):
    return render(request, 'camera.html')  # Renders index.html from templates


@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]

        # Process image and generate audio
        check = CheckCurrency()
        audio_buffer = check.checkCurrency(image)

        # Return the audio file directly
        return HttpResponse(audio_buffer, content_type="audio/mpeg")

    return JsonResponse({"error": "Invalid request"}, status=400)

