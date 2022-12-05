from application.celery import app
from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER, ADMINS, EMAIL_HOST_PASSWORD
from utils import return_chat_admins



@app.task(time_limit=80.0)
def send_admin_email(user_id, chats_id):
    recipient_list = return_chat_admins
    send_mail(
        subject = "Добавление в чат",
        message = f'Новый пользователь {user_id} добавлен в чаты {chats_id}!',
        from_email = EMAIL_HOST_USER,
        recipient_list = recipient_list,
        fail_silently = False,
        auth_user = EMAIL_HOST_USER,
        auth_password = EMAIL_HOST_PASSWORD,

    )