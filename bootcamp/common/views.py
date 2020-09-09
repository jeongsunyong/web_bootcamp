from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm, CustomUserChangeForm

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(data = request.POST, instance=request.user)
        if user_change_form.is_valid():
            user = user_change_form.save()
            messages.success(request, "변경되었습니다.")
            return redirect('common:mypage')
    else:
        user_change_form=CustomUserChangeForm(instance=request.user)
        return render(request, 'common/update.html',{'user_change_form':user_change_form})


@login_required
def change_password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            changed_user = password_change_form.save()
            update_session_auth_hash(request, changed_user)
            messages.success(request, "비밀번호를 변경하였습니다")
            return redirect('common:mypage')
        else:
            messages.error(request, 'error')
    else:
        password_change_form=PasswordChangeForm(request.user)

    return render(request, 'common/change_password.html', {'password_change_form':password_change_form})

def signup(request):
    """
    계정생성
    """

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('sunyong:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})