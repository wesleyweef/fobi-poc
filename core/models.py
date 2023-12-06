from django.db import models


class Dados(models.Model):
    email = models.CharField("Email", blank=False, null=False, max_length=80)
    job_zone = models.TextField("Job Zone", blank=True, null=True)
    carrer = models.TextField("Career", blank=True, null=True)
    answers = models.TextField("Answers", blank=True, null=True)
    created_at = models.DateTimeField(
        "Criado em", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        "Alterado em", editable=False, auto_now=True)

    class Meta:
        verbose_name = "Dados"
        verbose_name_plural = "Dados"
        ordering = ['-pk']

    def __str__(self):
        return self.email
