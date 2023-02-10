from django.shortcuts import render

# Create your views here.

def statistics(request):
    return render(request, 'vmip/statistics.html')

def gis(request):
    return render(request, 'vmip/gis.html')

def register(request):
    return render(request, 'vmip/register.html')

def login(request):
    return render(request, 'vmip/login.html')

def boat_details(request):
    return render(request, 'vmip/boat_details.html')
    
def idle_statistics(request):
    return render(request, 'vmip/idle_statistics.html')

def edit_comment(request):
    comments = ['法院沒入', '涉案扣押', '執照過期', '休漁', '其他']
    return render(request, 'vmip/edit_comment.html', {
        'comments': comments,
    })