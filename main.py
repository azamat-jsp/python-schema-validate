import json
import jsonschema
from jsonschema import validate
import os
import logging

logging.basicConfig(filename='logFile.log', level=logging.DEBUG)

jsonFiles = os.listdir("event")
jsonschemas = os.listdir("schema")


def getJsonSchema(file):
    try:
        with open(os.path.abspath('schema') +'/'+ file) as f:
            fileName = os.path.basename(f.name)
            data = json.load(f)
            return data
    except ValueError as err:
        logging.debug(f'message:{err}, filename:{fileName}')
        return False
    return True

def getJsonData(file):
    try:
        with open(os.path.abspath('event') +'/'+ file) as f:
            fileName = os.path.basename(f.name)
            data = json.load(f)
    except ValueError as err:
        return False
    return True

def validateJson(jsonschemas, jsonFiles):
    try:
        for schema in jsonschemas:
            schemaFile = getJsonSchema(schema)
            for file in jsonFiles:
                jsonFile = getJsonData(file)
                validate(instance=jsonFile, schema=schemaFile)
    except jsonschema.exceptions.ValidationError as err:
        logging.debug(err.message)
        return False
    return True

validateJson(jsonschemas, jsonFiles)
