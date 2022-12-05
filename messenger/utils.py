from users.models import User

def return_chat_admins(chats_id):

    admins = User.objects.filter(chats_admin__id__in=chats_id)
    emails = []
    for admin in admins:
        if admin.email in emails:
            pass
        else:
            emails.append(admin.email)
    return emails
