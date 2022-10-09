from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from shop.mixins.models_mixins import PKMixin
from django.contrib.auth import get_user_model


class Feedback(PKMixin):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(5))
    )

    def reformat_text(self):
        delete = set("""@/*#$%^\[]-_)+=;`~<>\|""")    # noqa
        user_text = self.text
        new_text = ''
        for i in user_text:
            if i not in delete:
                new_text += i
        self.text = new_text
        return self.text
