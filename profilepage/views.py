from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import json
from django.core.serializers import serialize
from .models import Profile
from .forms import ProfileForm
from django.views.generic import TemplateView

class profileMapView(TemplateView):
    template_name = "profilepage/base.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        profiles = Profile.objects.filter(published_date__lte=timezone.now())
        context["profiles"] = json.loads(serialize("geojson", profiles))
        return context

# def profile_list(request):
#     users = UserProfile.objects.filter(published_date__lte=timezone.now())
#     return render(request, 'profilepage/profile_list.html', {'users': users})


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profilepage/profile_detail.html', {'profile': profile})

def profile_edit(request,pk):
    profile = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(request.POST, instance=profile)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.published_date = timezone.now()
        profile.save()
        return redirect('profile_detail', pk=profile.pk)
    return render(request, 'profilepage/profile_edit.html', {'form': form})
