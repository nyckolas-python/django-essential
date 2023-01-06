from django.db import models


class PersonManager(models.Manager):
    """
        The custom manager serves to add methods for all models.
        Or to change the basic queryset when we work with table level functionality.
    """

    def get_staff_users(self):
        return super(PersonManager, self).get_queryset().filter(is_staff=False)
