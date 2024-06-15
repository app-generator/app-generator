# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string

def h_random(aLen=32):
    letters = string.ascii_letters
    digits  = string.digits
    chars   = '_<>,.+'
    return ''.join(random.choices( letters + digits + chars, k=aLen))

def h_random_ascii(aLen=32):
    letters = string.ascii_letters
    digits  = string.digits
    return ''.join(random.choices( letters + digits, k=aLen))
