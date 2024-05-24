from locust import HttpUser

from UserRouterLoadTest import user_composto


class WebsiteUser(HttpUser):
    tasks = [
        user_composto
    ]