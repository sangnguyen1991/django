from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .models import Users as UsersModel
from .forms import UserForm


class Users(View):
    template_name = 'users.html'

    def get(self, request):
        user_list = []
        form_user = UserForm()
        users = UsersModel.objects.all()[:50]

        for user in users:
            user_list.append({'id': user.id, 'name': user.name, 'status': user.status, 'create_at': user.create_at})

        return render(request, self.template_name, {
            'title': 'User List',
            'user_list': user_list,
            'form_user': form_user
        })

    def post(self, request):
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return HttpResponseRedirect('/user/')
