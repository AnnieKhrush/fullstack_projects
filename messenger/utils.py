from users.models import User
import datetime
from django.utils import timezone


def user_count():
    users = User.objects.all()
    login_last_day = []
    now = timezone.now()
    for user in users:
        if user.last_login is not None:
            if abs(now - user.last_login) < datetime.timedelta(days=1):
                login_last_day.append(user)
        else:
            pass
    return len(login_last_day)
        