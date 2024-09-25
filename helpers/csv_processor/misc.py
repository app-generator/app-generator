# -*- encoding: utf-8 -*-

import base64
import os
import random
import string

from django.conf import settings

def cfg_val( aVarName ): 

    return getattr(settings, aVarName, None)
