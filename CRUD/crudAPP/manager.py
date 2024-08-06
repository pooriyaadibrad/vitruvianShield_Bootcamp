from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    the manager class inherits from BaseUserManager
    this class created for build new user and save it
    """
    def create_user(self, email, username, password=None):
        """
        Creates and saves a new user
        :param email: primary email
        :param username: primary username
        :param password: password field
        :return: the created user
        """
        if not email and not username:
            raise ValueError('Users must have an email address and username')

        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a new superuser
        :param email: primary email
        :param username: primary username
        :param password: password field
        :return: created superuser
        """
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
