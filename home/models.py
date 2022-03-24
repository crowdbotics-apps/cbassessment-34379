from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class App(models.Model):
    # Type choices
    TYPE_WEB = 'web'
    TYPE_MOBILE = 'mobile'
    TYPE_CHOICES = (
        (TYPE_WEB, "Web"),
        (TYPE_MOBILE, "Mobile")
    )

    # Framework choices
    FRAMEWORK_DJANGO = 'django'
    FRAMEWORK_REACT_NATIVE = 'react_native'
    FRAMEWORK_CHOICES = (
        (FRAMEWORK_DJANGO, "Django"),
        (FRAMEWORK_REACT_NATIVE, "React Native")
    )

    name = models.CharField(max_length=50, blank=False, verbose_name="Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10, verbose_name="Type")
    framework = models.CharField(choices=FRAMEWORK_CHOICES, max_length=20, verbose_name="Framework")
    domain_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Domain name")
    screenshot = models.URLField(blank=True, null=True, verbose_name="Screenshot")
    subscription = models.IntegerField(verbose_name="Subscription", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="User")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Updated at")

    def __str__(self) -> str:
        return f"App: {self.name}"

class Plan(models.Model):
    name = models.CharField(max_length=20, blank=False, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(verbose_name="Price", default=0.00, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Updated at")

    def __str__(self) -> str:
        return f"App: {self.name}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="User")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plan_subscriptions", verbose_name="Plan")
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name="app_subscriptions", verbose_name="App")
    active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Updated at")

    def __str__(self) -> str:
        return f"Subscription - App: {self.app.name} - Plan: {self.plan.name}"

