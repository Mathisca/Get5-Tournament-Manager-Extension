from allauth.account.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def social_login_fname_lname_profilepic(sociallogin, user):
    pass
