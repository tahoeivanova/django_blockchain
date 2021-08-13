from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

import hashlib
from .forms import BlockForm
from .models import Block

# Create your views here.
def show_form(request):
    if request.method == 'GET':
        form = BlockForm
        return render(request, 'blockchain/home.html', {'form':form})
    else:
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blockchain:succeded'))
        else:
            return render(request, 'blockchain/home.html', {'form': form})

def success(request):
    return render(request, 'blockchain/succeded.html')
def get_hash(info):
    hash_for_data = hashlib.md5(info).hexdigest()
    return hash_for_data

def check_integrity(request):
    out = {}
    blocks = Block.objects.all()
    for i in range(1, len(blocks)):
        if blocks[i].prev_hash == get_hash(blocks[i-1].infofile.info):
            out[(blocks[i])] = 'ok'
        else:
            out[blocks[i]] = 'Corrupted'

    return render(request, 'blockchain/integrity.html', {'out':(out.items())})

