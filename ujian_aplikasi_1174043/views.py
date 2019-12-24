from django.shortcuts import render
from ujian_aplikasi_1174043.forms import NewUserForm


def index(request):
    return render(request, 'ujian_aplikasi_1174043/index_1174043.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'ujian_aplikasi_1174043/users_1174043.html',{'form':form})

# from ujian_aplikasi_1174043.models import User

# # Create your views here.
# def index(request):
#     return render(request,'ujian_aplikasi_1174043/index_1174043.html')

# def list_user(request):
#     users_list = User.objects.all()
#     return render(request,'ujian_aplikasi_1174043/users_1174043.html', {'users': users_list})