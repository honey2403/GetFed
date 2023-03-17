import googlemaps
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


def post(request):
    # current_location = request.data.get('current_location')
    # destination = request.data.get('destination')
    
    current_location='ShantaPuri'
    destination='Shanus'  
        # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        
        # Get the route between the two points
    directions_result = gmaps.directions(current_location, destination, mode="driving")
        
        # Parse the route information and return it as JSON
    route = []
    for leg in directions_result[0]['legs']:
        for step in leg['steps']:
            route.append(step['html_instructions'])
    return Response({'route': route})