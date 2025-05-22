from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
from .serializers import InputSerializer

class SendRequest(APIView):
    """
    Validates incoming onboarding form data and forwards it to an n8n webhook
    with key names formatted as Title Case for compatibility with Google Sheets.
    """

    def post(self, request):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data

            # Convert to Title Case keys
            payload = {
                "First Name": validated["first_name"],
                "Last Name": validated["last_name"],
                "Email": validated["email"],
                "Budget": validated["budget"],
                "Message": validated["message"]
            }

            webhook_url = "https://arjunomia.app.n8n.cloud/webhook/77dd9080-6c7e-40a0-8435-7ba64d176874"
            headers = {'Content-Type': 'application/json'}
            print("hi1")
            try:
                response = requests.post(
                    webhook_url,
                    headers=headers,
                    data=json.dumps(payload)
                )
                print(response)
                response.raise_for_status()
                print("hi2")
                return Response({"message": "n8n workflow triggered successfully!"}, status=status.HTTP_200_OK)
            except requests.exceptions.RequestException as e:
                return Response({"error": f"Error triggering n8n workflow: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
