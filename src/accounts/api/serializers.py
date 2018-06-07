from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy

User = get_user_model()


class AccountModelSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "url",

        ]

    def get_url(self, obj):
        return reverse_lazy("profile:detail", kwargs={"username": obj.username })



