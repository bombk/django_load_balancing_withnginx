from django.http import HttpResponse
import socket
import os

def home(request):
    container_id = socket.gethostname()
    return HttpResponse(f"Handled by: {container_id}")