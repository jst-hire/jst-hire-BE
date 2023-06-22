
import os
import json
import hashlib
import sys
import traceback
from datetime import datetime
from django.http import HttpResponse
from JSTHIRE import settings
from rest_framework import generics
from api.registration import registration_queries as qry


class Registration(generics.GenericAPIView):
    """
        API Name                   : Register user
        Description                : This api is used to user registration. Return json object as response to
                                    display data in UI.
        Created By                 : JST-HIRE
        Created Date               : 03-06-2023
        Last Modified By           :
        Last Modified Date         :
        Modification Description   :
        """
    permission_classes = ()
    def __init__(self):
        # logger.info("Registration API Service Started")
        print("Registration API Service Started")

    # def post(self, request):
    #     try:
    #         first_name = request.data['first_nm']
    #         last_name = request.data['last_nm']
    #         rec_cre_ts = datetime.now()
    #         result={'first_name':first_name,'last_name':last_name,'rec_created_time':rec_cre_ts}
    #         return HttpResponse(json.dumps(result))
    #     except ValueError:
    #         return HttpResponse(result)
    #     except Exception as err:
    #         http_err = traceback.format_exc()
    #         data = sys.exc_info()[1]
    #         print(http_err)
    #         # return HttpResponse(json.dumps({"error": http_err}))
    #         return HttpResponse(err)