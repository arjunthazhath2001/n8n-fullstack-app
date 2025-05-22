from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import requests
from .serializers import InputSerializer

class SendRequest(APIView):
    """
    API endpoint to receive onboarding form data, validate it, and forward to n8n webhook.
    """

    def post(self, request):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            webhook_url = "https://arjunomia.app.n8n.cloud/webhook/77dd9080-6c7e-40a0-8435-7ba64d176874"
            headers = {'Content-Type': 'application/json'}

            try:
                response = requests.post(
                    webhook_url,
                    headers=headers,
                    data=json.dumps(serializer.validated_data)
                )
                response.raise_for_status()
                return Response({"message": "n8n workflow triggered successfully!"}, status=status.HTTP_200_OK)
            except requests.exceptions.RequestException as e:
                return Response({"error": f"Error triggering n8n workflow: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
