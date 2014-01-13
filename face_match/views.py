#REST framework includes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import UnsupportedMediaType, MethodNotAllowed
#Django includes
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
#Python includes
from subprocess import Popen, PIPE
import os
import logging
import sys
#Project includes
from face_match import __file__
from face_match.serializers import IdSerializer
from face_match.Id import Id
from face_match.forms import ImageDetected



#root path to face_match app
path = os.path.dirname(__file__)
logger = logging.getLogger(__name__)

#Disabling csrf token since the request is from android
@csrf_exempt
#Final version supppose to have only POST method allowed
@api_view(['POST'])
def compare_faces(request):
    """
    Action that compares the given face with the given API 
    Request data: Image 
    Response: list of integer (facebook_ids)
    """

    if request.method == 'POST':
        data = ImageDetected(request.POST, request.FILES)
        ids = []
        if data.is_valid():
        ## Calling c++ function with output
            p = Popen([path + "/random", "42"], stdout=PIPE)
            code = p.wait()
            if code != 0:
                raise RuntimeError
            output = p.stdout.read()
            print output
            # Do whatever you need to do with the output
            logger.error('Unexpected error ', sys.exc_info()[1])


            # Generating JSON content
            for i in range(21,43):
                ids.append(Id(i))

            ids_response = IdSerializer(ids, many=True)

            #Loggin depending on face recognition algorithm used
            logger.info('Face recognition algorithm called')

            return Response(ids_response.data)
        else:
            ids_response = IdSerializer(ids, many=True)
            return Response(ids_response.data)
            #ext = data.get_extension()
            #logger.error('Unsupported media type ' + str(ext) + ' sent to the server')
            #raise UnsupportedMediaType(str(ext), "Supported media types: JPEG")
    else:
        method = str(request.method)
        logger.error('Not allowed method ' + method + ' called')
        # Raise method not allowed exception if the method isn't POST
        raise MethodNotAllowed(method, "Allowed methods: POST")
