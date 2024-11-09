from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AskForHelp
from .utils import calculate_distance

@csrf_exempt  # Disable CSRF protection for this view if you're handling it via an API (use with caution)
def get_distance_from_user(request, ask_id):
    try:
        # Get the current user's location from request (assuming it's sent in the request body or query params)
        user_lat = float(request.GET.get('user_latitude', 0))
        user_lon = float(request.GET.get('user_longitude', 0))
        
        # Get the AskForHelp request
        ask = AskForHelp.objects.get(id=ask_id)
        
        # Calculate distance using the helper function
        distance = calculate_distance(user_lat, user_lon, ask.latitude, ask.longitude)
        
        # Return the distance as a JSON response
        return JsonResponse({'distance': distance})
    except AskForHelp.DoesNotExist:
        return JsonResponse({'error': 'AskForHelp request not found'}, status=404)
    except ValueError:
        return JsonResponse({'error': 'Invalid latitude or longitude'}, status=400)
