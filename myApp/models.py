from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    rating = models.FloatField(default=0.0)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    university_major = models.CharField(max_length=100, null=True, blank=True)
    university_of_origin = models.CharField(max_length=100, null=True, blank=True)

    # Override the groups field with a unique related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='myapp_user_set',  # Changed related_name
        related_query_name='user',
    )

    # Override the user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='myapp_user_permissions_set',  # Changed related_name
        related_query_name='user',
    )

    def str(self):
        return self.username

class Class(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes_taught')
    students = models.ManyToManyField(User, related_name='classes_joined', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)

    def str(self):
        return f"Class by {self.tutor.username} on {self.date} at {self.time}"