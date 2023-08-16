from django.db import models

from django.contrib.auth.models import User, Group, Permission
from user_proxy.managers import PersonManager


class Person(User):
    """
        Proxy - "representative" of the model User.
        The simplest strategy for extending a user model.
        Use to change the behavior of the model.
    """
    people = PersonManager()
    person_groups = models.ManyToManyField(Group, related_name='people')
    person_permissions = models.ManyToManyField(
        Permission, related_name='people'
    )

    class Meta:
        # It is possible to hide unnecessary fields and change the sorting
        proxy = True
        ordering = ('first_name',)
        swappable = 'AUTH_USER_MODEL'
    # It is possible to add custom methods
    def do_something(self):
        print(self.username)
