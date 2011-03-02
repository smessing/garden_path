from paths.models import Path, Blob
from django.shortcuts import render_to_response, get_object_or_404,\
  get_list_or_404

def index(request):
  paths = Path.objects.all()
  return render_to_response('paths/index.html', {'paths':paths})

def detail(request, path_nick):
  _path = get_object_or_404(Path, nick=path_nick)
  blobs = get_list_or_404(Blob, path=_path)
  return render_to_response('paths/detail.html', {'path':_path, 'blobs':blobs})
