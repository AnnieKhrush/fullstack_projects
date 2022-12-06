from application.celery import app
from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from users.models import User
from utils import user_count


@app.task(time_limit=80.0)
def send_admin_email(user_id, chats_id):
    admins = User.objects.filter(chats_admin__id__in=chats_id)
    emails = []
    for admin in admins:
        if admin.email in emails:
            pass
        else:
            emails.append(admin.email)
    send_mail(
        subject = "Добавление в чат",
        message = f'Новый пользователь {user_id} добавлен в чаты {chats_id}!',
        from_email = EMAIL_HOST_USER,
        recipient_list = emails,
        auth_user = EMAIL_HOST_USER,
        auth_password = EMAIL_HOST_PASSWORD,
    )


@app.task()
def user_login_count():
    #количество пользователей, которые логинились в системе за последний день
    data = user_count()
    return data
    
