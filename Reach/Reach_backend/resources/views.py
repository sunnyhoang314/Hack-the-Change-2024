from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AskForHelp
from .utils import calculate_distance
from django.db.models import Avg
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .models import User
from .models import GlobalLeaderboard
from django.core.serializers import serialize
from ..Reach_backend.serializer import TaskRequestSerializer
from rest_framework import status

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

@csrf_exempt
def get_user_rank(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_rank = user.get_rank()
        return JsonResponse({'user_name': user.user_name, 'points': user.points, 'rank': user_rank})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def get_global_leaderboard(request):
    leaderboard = []
    countries = GlobalLeaderboard.objects.all()
    for country in countries:
        leaderboard.append({
            'country': country.country,
            'city': country.city,
            'total_points': country.total_points,
            'average_rank': country.average_rank,
        })
    return JsonResponse({'leaderboard': leaderboard})

@csrf_exempt
def get_user_leaderboard(request):
    users = User.objects.all().order_by('-points')  # Sort users by total points
    leaderboard = []
    for user in users:
        leaderboard.append({
            'user_name': user.user_name,
            'points': user.points,
            'rank': user.get_rank(),
        })
    return JsonResponse({'leaderboard': leaderboard})

@csrf_exempt
def get_user_asks(request):
    asks = AskForHelp.objects.filter(status='open')
    asks_json = serialize('json', asks)
    return JsonResponse(asks_json)

def has_task_request(request):
    user_name = request.data.get('user_name')
    
    if not user_name:
        return Response({'message': 'No user provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ask = AskForHelp.objects.get(user_name=user_name)
        
        return Response({'exists': True, 'status': ask.status}, status=status.HTTP_200_OK)

    except AskForHelp.DoesNotExist:
        return Response({'exists': False}, status=status.HTTP_200_OK)

def 


@api_view(['DELETE'])
def cancel_task_request(request):
    user_name = request.data.get('user_name')
    
    if not user_name:
        return Response({'message': 'No user'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ask = AskForHelp.objects.get(user_name=user_name)
        
        ask.delete()
        
        return Response({'message': 'Ask for help deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    except AskForHelp.DoesNotExist:
        return Response({'message': 'Ask for help not found for the given user.'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def create_task_request(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        task_image = request.FILES.get('task_image')

        task_request_data = {
            'user_name': request.data.get('user_name'),
            'people_needed': request.data.get('people_needed'),
            'task_description': request.data.get('task_description'),
            'latitude': request.data.get('latitude'),
            'longitude': request.data.get('longitude'),
            'profile_image': profile_image,
            'task_image': task_image,
        }
        
        if not all([task_request_data.user_name, task_request_data.task_description, task_request_data.people_needed, task_request_data.latitude, task_request_data.longitude]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TaskRequestSerializer(data=task_request_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task request submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    