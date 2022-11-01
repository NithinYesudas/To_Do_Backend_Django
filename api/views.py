from django.http import JsonResponse
from django.shortcuts import render


def getRoutes():
    routes = [
        {'Endpoint': '/notes/id/update/',
         'method': 'PUT',
         'body': {'body': ""},
         'description': 'Creates an existing note with data sent in'
         },

        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post req'
        },
    ]
    return JsonResponse(routes,safe= False)
