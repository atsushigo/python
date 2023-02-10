from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm, ProfileChangeForm

class RegisterView(View):
    form_class = UserCreationForm
    initial = {'key': 'value'}
    template_name = 'user/customer_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            generic_public_group = Group.objects.get(name='一般民眾')
            generic_public_group.user_set.add(user)
            messages.success(request, f'Account created for {username}')

            return redirect(to='/user/login')

        return render(request, self.template_name, {'form': form})

def applyhome(request):
    return render(request, 'user/apply_homepage.html')

# def register(request):
#     return render(request, 'user/customer_register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect(to='/parking/apply')
            
    return render(request, 'user/customer_login.html')

def logout_view(request):
    logout(request)
    return redirect(to='/user/login')
    
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileChangeForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '個人資料已更新')
            return redirect(to='/user/profile')
    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = ProfileChangeForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def entrance(request):
    return render(request, 'user/entrance.html')

def news_list(request):
    class News:
        def __init__(self, type, title, date, unit, color):
            self.type = type
            self.title = title
            self.date = date
            self.unit = unit
            self.color = color
    new1 = News(
        '公告類型1',
        '非漁船進出第一類漁港停泊申請平台之公告測試測試測試測試測試測試測試測試測試試測試測',
        '2022/11/24',
        '行政院農委會漁業署',
        'gray'
    )
    new2 = News(
        '公告類型2',
        '非漁船進出第一類漁港停泊申請平台之公告測試2',
        '2022/11/24',
        '海洋委員會海巡署',
        'purple'
    )
    new3 = News(
        '公告類型3',
        '非漁船進出第一類漁港停泊申請平台之公告測試3',
        '2022/11/24',
        '基隆市政府',
        'orange'
    )

    news = [new1, new2, new3]
    return render(request, 'user/news_list.html', {'news': news})

def new(request):
    return render(request, 'user/new.html')