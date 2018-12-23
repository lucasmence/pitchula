#!/usr/bin/env python
# coding: utf-8

import constants
import json

def getValue(path, field):

    value = None
    try:    
        with open(path, constants.COMMAND_READ_MODE) as file:
            jsonFile = json.load(file)  

        value = format(jsonFile[field]) 
    except:
        return constants.FIELD_EMPTY_STRING

    if (value is None):        
        return  constants.FIELD_EMPTY_STRING
    else:
        return value
