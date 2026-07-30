from django.shortcuts import get_object_or_404, render

from .models import Scientific

def index(request):
    all_names = Scientific.objects.prefetch_related(
        "english_names",
        "japanese_names"
    )
    context = {'all_names': all_names}
    return render(request, "check/index.html", context)

def edit(request, scientific_id):
    scientific = get_object_or_404(Scientific, pk=scientific_id)
    return render(request, "check/edit.html", {"scientific": scientific})

def update(request, scientific_id):
    scientific = get_object_or_404(Scientific, pk=scientific_id)
    return render(request, "check/index.html", {"scientific": scientific})

# Create your views here.
