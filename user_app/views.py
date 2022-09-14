from django.shortcuts import render
from django.views import View
from user_app.forms import RegisterForm
def index_view(request):
    return render(request, 'user_app/index.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'user_app/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            phone = register_form.cleaned_data.get('phone')
            email = register_form.cleaned_data.get('email')
            user_avatar = register_form.cleaned_data.get('user_avatar')
            user_gender = register_form.cleaned_data.get('user_gender')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    phone=phone,
                    email=email,
                    user_avatar=user_avatar,
                    user_gender=user_gender,
                    is_active=True,)
                new_user.set_password(user_password)
                new_user.save()
                message = 'در سایت ثبت نام شدید. برای ورود به پنل کاربری اطلاعات خواسته شده را وارد کنید.'
        context = {
            'login_form': login_form,
            'showMessage': message
        }

        return render(request, 'userAccountApp/loginPage.html', context)