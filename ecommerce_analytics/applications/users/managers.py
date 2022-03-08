from django.db import models
from django.contrib.auth.models import BaseUserManager

class UsersManger(BaseUserManager, models.Manager):
    def _create_user(self, username: str, password: str, email: str, is_staff: bool, is_superuser: bool, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, username: str, email: str, password:str):
        self.create_user(username, password, email, False, False)

    def create_superuser(self, username: str, email: str, password=None, **extra_fields):
        self._create_user(username, password, email, True, True, **extra_fields)
