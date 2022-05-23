from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blocks, Pages
from .serializers import SerailizerPages, SerailizerBlocks


# Create your views here.
class PagesView(ListCreateAPIView):
    queryset = Pages.objects.all().order_by('sort')
    serializer_class = SerailizerPages


# class PageViewSingle(RetrieveUpdateDestroyAPIView):
#     blockIDs = []
#
#     blocks = Pages.objects.filter(slag=page_slag).values('blocks')
#
#     for block in blocks:
#         blockID = block['blocks']
#         blockIDs.append(blockID)
#
#     queryset = Blocks.objects.filter(id__in=blockIDs).order_by('sort')
#     serializer_class = SerailizerBlocks
