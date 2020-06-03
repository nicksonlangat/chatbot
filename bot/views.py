from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import datetime
import emoji
import random
import json

@csrf_exempt
def index(request):
    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()

        if incoming_msg == 'hello':
        	 response = emoji.emojize("""
*Ahoy! I am the NickyBot* I am created by RealNickyAdams to help with tasks :sunglasses:
Let's be friends :wink:
*You can give me the following commands although Nicky is still working on the features, all of them may not work correctly:*


:black_small_square: *'quote':* Hear an inspirational quote to start your day! :rocket:

:black_small_square: *'meta':* Send a warning message to a guy who asks meta questions in group! :rage:

:black_small_square: *'yw':* Send a you are welcome message when someone thanks you! :blush:

:black_small_square: *'mornin':* Greet people in the group! :wave:

:black_small_square: *'night':* Wish people a good night ! :dizzy_face:

:black_small_square: *'python':* Get links to download Python tutorials :snake:

:black_small_square: *'django':* Get links to download Django tutorials :snake:

""", use_aliases=True)
        	 msg.body(response)
        	 responded = True
            

            
            

        return HttpResponse(str(resp))