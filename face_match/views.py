#from rest_framework.parsers import JSONParser
from rest_framework.views import APIVIEW
from rest_framework.response import Response
from face_match.serializers import IdSerializer

def compare_faces(request):
    """
    Action that compare the given face with the given API 
    Request data: Image 
    Response: list of integer (facebook_ids)
    """
    if request.method == 'POST':
        # We get the image
        image = request.FILES['image'] 

        ## For facebook
        # dicc = JSONParser(request.DATA)
        # token = dicc['access_token']
        # Getting facebook faces.


        # Do the face recognition
        # ...
        #

        ids = [] #This suppose to have the resulting id list

        ids_response = IdSerializer(ids, many=True)

        return Response(ids_response)
