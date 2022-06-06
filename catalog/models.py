from django.db import models
from django.urls import reverse

class User(models.Model):

    id = models.AutoField(primary_key = True, verbose_name ='ID')
    name = models.CharField(max_length=45, verbose_name="Name", help_text="Enter your name (e.g. John Smith)")
    password = models.CharField(max_length=45, verbose_name="Password", help_text="Enter your password (e.g. fX$_g2i!)")
    email = models.EmailField(max_length=100, unique=True, verbose_name="E-mail", help_text="Enter your e-mail (e.g. johnsmith@gmail.com)")
    age = models.IntegerField(blank=True, null=True, verbose_name="Age", help_text="Enter your age (e.g. 18)")

    class Gender(models.TextChoices):
        man = 'man'
        woman = 'woman'

    gender = models.CharField(
        max_length=5,
        choices=Gender.choices,
        default=Gender.man,
        verbose_name="Gender"
    )
    followers = models.IntegerField(blank=True, null=True, verbose_name="Followers", help_text="Enter your number of followers (e.g. 100)", default=0)
    following = models.IntegerField(blank=True, null=True, verbose_name="Following", help_text="Enter your number of followed people (e.g. 100)", default=0)
    image = models.ImageField(blank=True, null=True, verbose_name="Image", help_text="Enter your image (e.g. .png, .jpg, .gif)")

    class Meta:
        ordering = ['followers', 'name']


    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Message(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=100, verbose_name="Title", help_text="Enter your title (e.g. School abroad)")
    message = models.TextField(blank=True, null=True, verbose_name="Message", help_text="Write something here...")
    date = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Date")
    likes = models.IntegerField(blank=True, null=True, verbose_name="Likes", help_text="Enter your number of likes (e.g. 20)", default=0)
    dislikes = models.IntegerField(blank=True, null=True, verbose_name="Dislikes", help_text="Enter your number of dislikes (e.g. 20)", default=0)

    class Meta:
        ordering = ['likes', 'title']


    def get_absolute_url(self):
        return reverse('message-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Room(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=100, verbose_name="Title", help_text="Enter your title (e.g. Sport discussing thread)")
    number_of_people = models.IntegerField(blank=True, null=True, verbose_name="Maximum number of people", help_text="Enter the maximum number of people (e.g. 30)", default=6)
    date = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description", help_text="Write something here...")
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    message_fk = models.ForeignKey(Message, on_delete=models.CASCADE)

    class Meta:
        ordering = ['number_of_people', 'title']


    def get_absolute_url(self):
        return reverse('room-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
