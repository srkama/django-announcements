'''
context processor for announcements
'''
__author__ = 'kamal.s'

from announcements.models import Announcement
import datetime


def announcements(request):
    """
    adds valid announcements to the context dict
    """
    announcement_objects = Announcement.objects.filter(
        publish_start__lte=datetime.datetime.now(),
        publish_end__gte=datetime.datetime.now())
    if not request.user.is_authenticated():
        announcement_objects = announcement_objects.filter(
            members_only__exact=False)
    return {'announcements': announcement_objects}