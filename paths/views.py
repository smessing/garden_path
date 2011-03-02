from paths.models import Path
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
  paths = Path.objects.all()
  return render_to_response('paths/index.html', {'paths':paths})

def detail(request, path_nick):
  path = get_object_or_404(Path, nick=path_nick)
  return render_to_response('paths/detail.html', {'path':path})
