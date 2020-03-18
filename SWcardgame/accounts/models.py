from django.db.models import *
from django.contrib.auth.models import User
# # Create your models here.
type_choices = [('jedi', 'Jedi'),('sith', 'Sith'),('hutt', 'Hutt'), ('bh', 'Bounty Hunter'), ('tr', 'Tusken Raider')]
class Type(Model):
    name = CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
class Profile(Model):
    name = CharField(max_length=100, unique=True)
    type = ForeignKey(Type, null=True, on_delete=SET_NULL)
    user = OneToOneField(User, on_delete=CASCADE)
    # avatar = ImageField(upload_to=)
    credits = IntegerField(null=True, blank=True, default=10)
    bio = TextField(null=True, blank=True, default='May the Shwartz be with yous')



