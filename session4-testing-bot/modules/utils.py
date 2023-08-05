# utils.py
import json
import pandas as pd


def get_endpoints(swagger_file):
    return swagger_file["paths"].keys()


def get_endpoint_type(swagger_file, endpoint):
    return list(swagger_file["paths"][endpoint].keys())[0]


def get_test_types(endpoint):
    return ["GET", "POST", "PUT", "DELETE", "PATCH"]


def create_test_data(endpoint):
    return {
        "GET": {
            "url": f"/api/{endpoint}",
            "method": "GET"
        },
        "POST": {
            "url": f"/api/{endpoint}",
            "method": "POST",
            "data": {
                "foo": "bar"
            }
        },
        "PUT": {
            "url": f"/api/{endpoint}",
            "method": "PUT",
            "data": {
                "foo": "bar"
            }
        },
        "DELETE": {
            "url": f"/api/{endpoint}",
            "method": "DELETE"
        },
        "PATCH": {
            "url": f"/api/{endpoint}",
            "method": "PATCH",
            "data": {
                "foo": "bar"
            }
        }

    }


def get_endpoint_color(endpoint_type):
    endpoint_type = endpoint_type.lower()
    if endpoint_type == "get":
        return "lightgreen"
    elif endpoint_type == "post":
        return "lightblue"
    elif endpoint_type == "put":
        return "lightred"
    elif endpoint_type == "patch":
        return "lightyellow"
    elif endpoint_type == "delete":
        return "red"
    else:
        return "lightgray"


def convert_swagger_to_dataframe(swagger_dict):
    endpoints = swagger_dict['paths'].keys()
    df = pd.DataFrame(columns=['Tag', 'EndpointType', 'Endpoint', 'Description', 'Parameters'])

    for endpoint in endpoints:
        endpoint_type = get_endpoint_type(swagger_dict, endpoint)
        path = swagger_dict['paths'][endpoint][endpoint_type]
        tag = path['tags'][0]
        description = path['summary']
        params = path['parameters']
        parameters = []

        for parameter in params:
            required = str(parameter['required'])
            name = str(parameter['name'])
            try:
                type = str(parameter['type'])
            except KeyError:
                type = 'NA'
            parameters.append((name, type, required))

        df = df.append({'Tag': tag, 'EndpointType': endpoint_type, 'Endpoint': endpoint, 'Description': description, 'Parameters': parameters},
                   ignore_index=True)
    return df


def convert_string_to_df(str_to_convert, sep):
    df = pd.read_csv(str_to_convert, sep=sep)

    return df

