from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import json
from .models import Profile
from .forms import ProfileForm
from .serializers import ProfileSerializer
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

class profileMapView(TemplateView):
    template_name = "profilepage/profile_list.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            profiles = Profile.objects.all()
        else:
            profiles = [Profile.objects.get(user=self.request.user)]
        serializer = ProfileSerializer(profiles, many=True)
        context["profiles"]= json.loads(json.dumps(serializer.data))
        return context

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return super().get(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('profile_detail', kwargs={'pk': self.request.user.profile.id}))
        return HttpResponseRedirect(reverse('login'))

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profilepage/profile_detail.html', {'profile': profile})

def profile_edit(request,pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.published_date = timezone.now()
            profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profilepage/profile_edit.html', {'form': form})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        self.object.save()
        login(self.request, self.object)
        return reverse_lazy('profile_edit', kwargs={'pk': self.object.profile.id})
