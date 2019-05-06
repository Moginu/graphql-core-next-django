from django.shortcuts import render
from django.http import HttpResponse
from graphql import graphql_sync

from .schema import schema


def test_graphql(request):
    result = graphql_sync(schema, """
        {
          hero(episode: EMPIRE) {
            name
            appearsIn
          }
        }
        """)
    return HttpResponse(result)
