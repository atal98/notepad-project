from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import NoteSerializer
from .models import Note

class Routes(APIView):
    def get(self, request):
        response = [
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
                'description': 'Creates new note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/update/',
                'method': 'PUT',
                'body': {'body': ""},
                'description': 'Creates an existing note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/delete/',
                'method': 'DELETE',
                'body': None,
                'description': 'Deletes and exiting note'
            }
        ]
        
        return Response(response)


class NotesAPI(APIView):
    
    def get(self,request):
        note_qs = Note.objects.all()

        serializer = NoteSerializer(note_qs, many=True)
        return Response(serializer.data)
    
class NoteAPI(APIView):
    
    def get(self,request,pk):
        note_qs = Note.objects.get(id=pk)
        serializer = NoteSerializer(note_qs, many=False)
        return Response(serializer.data)
