from django.db import models

# Create your models here.

class WebsitePageviews(models.Model):
    website_pageview_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    website_session_id = models.PositiveBigIntegerField()
    pageview_url = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'website_pageviews'


class WebsiteSessions(models.Model):
    website_session_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    user_id = models.PositiveBigIntegerField()
    is_repeat_session = models.PositiveSmallIntegerField()
    utm_source = models.CharField(max_length=12, blank=True, null=True)
    utm_campaign = models.CharField(max_length=20, blank=True, null=True)
    utm_content = models.CharField(max_length=15, blank=True, null=True)
    device_type = models.CharField(max_length=15, blank=True, null=True)
    http_referer = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_sessions'