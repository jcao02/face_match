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
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
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

            # Remove file if exists
            try: 
                os.remove("./tmp/input_image.jpeg")
            except:
                print "File wasn't there"

            img = data.cleaned_data.get('photo')
            path = default_storage.save('./tmp/input_image.jpeg', ContentFile(img.read()))

            ## Calling c++ function with output
            p = Popen(["./main", "./tmp/input_image.jpeg", "./facedata_fourth.xml"], stdout=PIPE)
            code = p.wait()

            print "Exit code: ", code

            # If return code is OK, we read the output
            if code == 0:
                output = p.stdout.read()
                ids = output.split('\n') 
            else:
                print "Algorithm error"
                logger.error('Unexpected error ', sys.exc_info()[1])


            print output
            print ids

            # Converting strings to ints
            ids = filter(is_number, ids)
            ids = map(int, ids)
            ids = map(Id, ids)

            # Generating JSON content
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


def is_number(x):
    """Checks if a string is a number"""
    try:
        int(x)
        return True
    except ValueError:
        return False
