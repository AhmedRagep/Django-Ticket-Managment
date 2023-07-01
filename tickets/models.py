from django.db import models
import uuid
from users.models import User
# Create your models here.
STATUS_CHOICES = (
    ('Active','Active'),
    ('Completed','Completed'),
    ('Pending','Pending'),
)
class Tiecket(models.Model):
    tieckt_number = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    # متعملش حاجه
    assigned_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    resolved = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True,blank=True)
    closed_date = models.DateTimeField(null=True,blank=True)
    ticket_status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title