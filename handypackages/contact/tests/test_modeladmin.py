from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from handypackages.contact.admin import ContactAdminPanel
from handypackages.contact.models import Contact


class MockRequest:
    def __init__(self, user=None):
        self.user = user


request = MockRequest()


class ModelAdminTests(TestCase):
    def test_has_add_permission(self):
        """
        has_add_permission returns True for users who can add objects and
        False for users who can't.
        """
        ma = ContactAdminPanel(Contact, AdminSite())
        request = MockRequest()
        self.assertEqual(ma.has_add_permission(request), False)

    def test_has_change_permission(self):
        """
        has_change_permission returns True for users who can change objects and
        False for users who can't.
        """
        ma = ContactAdminPanel(Contact, AdminSite())
        request = MockRequest()
        self.assertEqual(ma.has_change_permission(request), False)
