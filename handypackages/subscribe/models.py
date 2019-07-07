from django.core import signing
from django.db import models
from django.utils.translation import gettext_lazy as _


class SubscribeAbstractModel(models.Model):
    email = models.EmailField(
        _("Email"),
        max_length=255,
        db_index=True,
        unique=True,
    )
    create_time = models.DateTimeField(
        _("Subscribe Time"),
        auto_now_add=True,
    )

    def __str__(self):
        return self.email

    class Meta:
        abstract = True
        verbose_name = _('Subscribe Email')
        verbose_name_plural = _('Subscribe Emails')


class SubscribeModel(SubscribeAbstractModel):
    """Email Subscribe Model"""

    @property
    def generate_hash(
        self,
        key=None,
        salt='django.core.signing',
        compress=False,
    ):
        """Generate url safe hash for Subscribe Email objects."""
        data = {
            "email": self.email,
            "id": self.id,
            "create_time": str(self.create_time),
        }
        value = signing.dumps(
            data,
            key=key,
            salt=salt,
            compress=compress,
        )
        return value

    @staticmethod
    def unsign_hash(
        hash_string,
        key=None,
        salt='django.core.signing',
        max_age=None,
    ):
        """Unsign hash for Subscribe Email objects."""
        try:
            value = signing.loads(
                hash_string,
                key=key,
                salt=salt,
                max_age=max_age,
            )
            return value
        except signing.BadSignature:
            return False


class Subscribe(SubscribeModel):
    class Meta:
        proxy = True
        app_label = 'handypackages'
        auto_created = True
        verbose_name = _('Subscribe Email')
        verbose_name_plural = _('Subscribe Emails')
