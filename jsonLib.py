#!/usr/bin/env python
# coding: utf-8

import json

class JsonLib():

    def __init__(self, constants):
        self._constants = constants

    def getValue(self, path, field):

        value = None
        try:    
            with open(path, self._constants._COMMAND_READ_MODE) as file:
                jsonFile = json.load(file)  

            value = format(jsonFile[field]) 
        except:
            return self._constants._FIELD_EMPTY_STRING

        if (value is None):        
            return  self._constants._FIELD_EMPTY_STRING
        else:
            return value
