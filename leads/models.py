from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username  

class LeadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        "Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    converted_date = models.DateTimeField(null=True, blank=True)

    objects = LeadManager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    # New, Contacted, Converted, Unconverted
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Agent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email
   
def handle_upload_follow_ups(instance, filename):
    return f"lead_followups/lead_{instance.lead.pk}/{filename}"

class FollowUp(models.Model):
    lead = models.ForeignKey(
        Lead, related_name="followups", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    file = models.FileField(null=True, blank=True,
                            upload_to=handle_upload_follow_ups)

    def __str__(self):
        return f"{self.lead.first_name} {self.lead.last_name}"

def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
    
'''
La función post_user_created_signal es un "signal handler" que se ejecuta cada vez que se crea un nuevo usuario (User) en la base de datos. Este signal handler está conectado al evento post_save del modelo User, lo que significa que se activará después de que se guarde un nuevo usuario en la base de datos.
Dentro de la función post_user_created_signal, se verifica si el usuario ha sido creado (created) y, en caso afirmativo, se crea un nuevo perfil de usuario (UserProfile) asociado a ese usuario.
En resumen, este código garantiza que cada vez que se crea un nuevo usuario, también se creará automáticamente un perfil de usuario correspondiente. Esto es útil para mantener la integridad de los datos y asegurarse de que cada usuario tenga un perfil asociado.
'''