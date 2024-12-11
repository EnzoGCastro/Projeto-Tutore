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

    def __str__(self):
        return self.username

class Class(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes_taught')
    students = models.ManyToManyField(User, related_name='classes_joined', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)

    def __str__(self):
        return f"Class by {self.tutor.username} on {self.date} at {self.time}"

class ClassPost(models.Model):
    """
    A model that represents a post about a class.
    It pulls from the Class model and includes all important information.
    """
    related_class = models.OneToOneField(Class, on_delete=models.CASCADE, related_name='post')
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tutor_name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return f"Post about class by {self.tutor_name} on {self.date} at {self.time}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Override the save method to ensure the post contains up-to-date information from the related class.
        """
        # Sync fields with the related class
        self.date = self.related_class.date
        self.time = self.related_class.time
        self.price = self.related_class.price
        self.tutor_name = self.related_class.tutor.username
        self.description = self.related_class.description
        self.image = self.related_class.image
        super(ClassPost, self).save(force_insert, force_update, using, update_fields)
