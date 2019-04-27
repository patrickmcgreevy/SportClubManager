from django.shortcuts import render
from django.views import generic
from django.views.generic import edit
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from .models import Club
#from django.contrib.auth.models import User
from users.models import CustomUser as User

# Create your views here.
login_redirect_url = 'login'
login_redirect_field_name = 'redirect_to'

class AllClubs(LoginRequiredMixin, generic.ListView):
    login_url = login_redirect_url
    redirect_field_name = login_redirect_field_name
    template_name = 'teammanager/clubs.html'
    context_object_name = 'user_clubs'

    def get_queryset(self):
        #clubs = Club.objects.all()
        #return Club.objects.all()
        #return filterClubList(list(Club.objects.all()), self.request.user)
        return list(Club.objects.all())

class UserClubs(LoginRequiredMixin, generic.ListView):
    login_url = login_redirect_url
    redirect_field_name = login_redirect_field_name
    template_name = 'teammanager/clubs.html'
    context_object_name = 'user_clubs'

    def get_queryset(self):
        return filterClubList(Club.objects.all(), self.request.user) # request is a member of superclass ListView, user gets the current user object from the request

def filterClubList(clubList, rUser):

    return [club for club in clubList if rUser.groups.filter(name__in=[club.club_name])] # name__in is using the __in function. The list is all the groups we're checking
    """newList = []
    
    for club in clubList:
        if rUser.groups.filter(name__in=[club.club_name]):
            newList.append(club)

    return newList"""

class ClubDetails(LoginRequiredMixin, generic.DetailView):
    login_url = login_redirect_url
    redirect_field_name = login_redirect_field_name
    template_name = 'teammanager/clubdetails.html'
    model = Club

    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        #context['club'] = Club.objects.get(self.pk)
        context['club'] = self.object
        context['officers'] = get_club_officers(self.object)
        context['members'] = get_club_members(self.object)
        return context


class ClubOfficerDetails(UserPassesTestMixin, ClubDetails):
    login_url = login_redirect_url
    redirect_field_name = login_redirect_field_name
    template_name = 'teammanager/officerdetails.html'
    #super(UserPassesTestMixin).permission_denied_message = "You're not an officer... GTFO"

    def test_func(self):
        return self.request.user in get_club_officers(self.get_object())

    def get_funds(self):
        return self.object.funds

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.test_func():
    #         return redirect('/clubs')
    #def get_login_url(self):
     #   return '/clubs/'

class ClubMemberChange(edit.UpdateView):
    model = Group
    fields = ['name']
    template_name = 'teammanager/group_update_form.html'

# class ClubMemberChange(edit.UpdateView):
#     model = Club
#     #fields = ['name']
#     fields = ['club_name', 'funds']
#     #template_name_suffix = '_update_form'
#     template_name = 'teammanager/group_update_form.html'

#     def group_members(self):
#         return list(User.objects.filter(groups__name=self.model.club_name))

#     def group_name(self):
#         return self.model.club_name
    
    # def get(self, request, *args, **kwargs):
    #     #super.get_context_data(**kwargs)
    #     self.context.update({'model_name' : self.model.name, 'group_members' : list(User.objects.filter(groups__name=self.model.name))})
    #     return super(edit.UpdateView, self).post(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     # if 'group_members' not in kwargs:
    #     #     kwargs['group_members'] = list(User.objects.filter(groups__name=self.model.name))
    #     # kwargs['model_name'] = self.model.name
    #     # return super().get_context_data(**kwargs)

    #     context = super().get_context_data(**kwargs)
    #     context.update({'model_name' : self.model.name, 'group_members' : list(User.objects.filter(groups__name=self.model.name))})

    #     return context


def get_club_officers(club):
    group_name = club.club_name + ' Officers'

    return list(User.objects.filter(groups__name=group_name))

def get_club_members(club):
    return list(User.objects.filter(groups__name=club.club_name))