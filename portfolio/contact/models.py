from django.db import models

# ContactMessage Model.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.subject}"
    


