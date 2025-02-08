from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response


def test_add_number(api_client):
    url = reverse('calculator-list')
    data = {
        'query': "10+20"
    }
    response = api_client.post(path=url, data=data, format='json', HTTP_ACCEPT='application/json')
    expected_rsp = Response("20",
                            status=status.HTTP_200_OK)
    assert response.status_code == 200
    assert response.json() == expected_rsp.data


def test_subtract_number(api_client):
    url = reverse('calculator-list')
    data = {
        'query': "30-10"
    }
    response = api_client.post(path=url, data=data, format='json', HTTP_ACCEPT='application/json')
    expected_rsp = Response("20",
                            status=status.HTTP_200_OK)
    assert response.status_code == 200
    assert response.json() == expected_rsp.data


def test_multiply_number(api_client):
    url = reverse('calculator-list')
    data = {
        'query': "4*5"
    }
    response = api_client.post(path=url, data=data, format='json', HTTP_ACCEPT='application/json')
    expected_rsp = Response("20",
                            status=status.HTTP_200_OK)
    assert response.status_code == 200
    assert response.json() == expected_rsp.data


def test_divide_number(api_client):
    url = reverse('calculator-list')
    data = {
        'query': "40%2"
    }
    response = api_client.post(path=url, data=data, format='json', HTTP_ACCEPT='application/json')
    expected_rsp = Response("20",
                            status=status.HTTP_200_OK)
    assert response.status_code == 200
    assert response.json() == expected_rsp.data
