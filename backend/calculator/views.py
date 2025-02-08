from rest_framework import parsers, renderers
from rest_framework.response import Response
from rest_framework.views import APIView

from .math_utils import perform_math_operations
from .serializers import MathQuerySerializer


class CalculatorView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = MathQuerySerializer

    def get_serializer_context(self):
        """
        :return: MathQuerySerializer context
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        """
        Initialize serializer
        :param args:
        :param kwargs:
        :return: MathQuerySerializer
        """
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        The method accept math expression in payload and evaluate using numexpr
        :param request: Django Request
        :param args:
        :param kwargs:
        :return: Expression result
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        query = serializer.validated_data['query']
        result = perform_math_operations(query)
        return Response(result)
