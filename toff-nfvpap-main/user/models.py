from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Group, PermissionsMixin
)
from django.utils import timezone


'''
                     |      漁港資訊      |     漁港船舶管理     |            停泊申請平台              |
                     |   瀏覽   |  編輯   |   查詢   |   統計    |  申請  |  批核  |  統計  |  稽核通知  |
------------------------------------------------------------------------------------------------------
 一般民眾             |    V    |         |          |          |        |        |       |           |
------------------------------------------------------------------------------------------------------
 進港申請者           |    V    |         |          |          |   V    |        |       |           |
 ------------------------------------------------------------------------------------------------------
 縣市政府(資料維護者)  |    V    |    V    |          |          |        |        |       |           |
 ------------------------------------------------------------------------------------------------------
 縣市政府(資料查詢者)  |    V    |         |     V    |     V    |        |        |       |           |
 ------------------------------------------------------------------------------------------------------
 縣市政府(資料批核者)  |    V    |         |          |          |        |    V   |   V   |     V     |
 ------------------------------------------------------------------------------------------------------
 漁業署(資料維護者)    |    V    |    V    |          |          |        |        |       |           |
 ------------------------------------------------------------------------------------------------------
 漁業署(資料查詢者)    |    V    |         |          |          |        |        |       |     V     |
 ------------------------------------------------------------------------------------------------------
 最高權限             |    V    |    V    |     V    |     V    |        |        |   V   |           |
 ------------------------------------------------------------------------------------------------------
'''


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('使用者必須填寫電子信箱')

        now = timezone.now()
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_active=True,
            last_login=now,
            date_joined=now,
            updated_at=now,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='電子信箱',max_length=100,unique=True,)
    username = models.CharField(verbose_name='帳號', max_length=30, unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE) # user刪除會連帶把profile一起刪除
    name = models.CharField(verbose_name='姓名', max_length=30, null=True, blank=True)
    id_no = models.CharField(verbose_name='身分證字號', max_length=30, null=True, blank=True)
    passport_no = models.CharField(verbose_name='護照號碼', max_length=30, null=True, blank=True)
    address = models.CharField(verbose_name='聯絡地址', max_length=50, null=True, blank=True)
    residential_no = models.CharField('市話', max_length=10, null=True, blank=True)
    mobile_no = models.CharField('行動電話', max_length=10, null=True, blank=True)
    fax_no = models.CharField('傳真', max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

