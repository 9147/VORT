from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    # Other event-related fields...

class CertificateManager(models.Manager):
    def get_certificates_for_event(self, event_id):
        return self.filter(event_id=event_id)

    def verify_certificate_hash(self, event_id, provided_hash):
        certificates = self.filter(event_id=event_id)
        for certificate in certificates:
            if certificate.hash_value == provided_hash:
                return True  # Certificate hash found and verified
        return False  # Certificate hash not found or doesn't match

class Certificate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    hash_value = models.CharField(max_length=64)  # Assuming 64 characters for a SHA-256 hash
    objects = CertificateManager()

    def __str__(self):
        return self.hash_value
    # Other certificate-related fields...

# Function to add hash value for a certificate related to an event
def add_certificate_hash(event_id, hash_value):
    event = Event.objects.get(pk=event_id)
    Certificate.objects.create(event=event, hash_value=hash_value)
