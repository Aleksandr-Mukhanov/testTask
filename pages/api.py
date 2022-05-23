from django.http import JsonResponse
from .models import Blocks, Pages
from .serializers import SerailizerPages, SerailizerBlocks


def get_pages(request):
    pages = SerailizerPages(
        Pages.objects.all().order_by('sort'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'pages': pages})


def get_blocks(request, page_slag):
    blockIDs = []

    blocks = Pages.objects.filter(slag=page_slag).values('blocks')

    for block in blocks:
        blockID = block['blocks']
        blockIDs.append(blockID)
        # счетчик просмотров
        block_object = Blocks.objects.get(id=blockID)
        block_object.qntView += 1
        block_object.save()

    blocksAll = SerailizerBlocks(
        Blocks.objects.filter(id__in=blockIDs).order_by('sort'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'blocks': blocksAll})
