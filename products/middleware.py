from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that don't require authentication
        public_urls = [
            reverse('login'),
            reverse('signup'),
            reverse('password_reset'),
            reverse('password_reset_done'),
            reverse('password_reset_confirm'),
            reverse('password_reset_complete'),
        ]

        # Check if the user is not authenticated and trying to access a protected URL
        if not request.user.is_authenticated and request.path not in public_urls:
            # Store the original URL to redirect after login
            request.session['next'] = request.path
            return redirect('login')

        response = self.get_response(request)
        return response 