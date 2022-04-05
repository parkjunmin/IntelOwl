# flake8: noqa E501

from datetime import timedelta

from .commons import VERSION

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    # Auth
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",  # django-oauth-toolkit >= 1.0.0
        "rest_framework_social_oauth2.authentication.SocialAuthentication",
        "durin.auth.CachedTokenAuthentication",
    ],
    # Pagination
    "DEFAULT_PAGINATION_CLASS": "certego_saas.ext.pagination.CustomPageNumberPagination",
    "PAGE_SIZE": 10,
    # Permission
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    # Exception Handling
    "EXCEPTION_HANDLER": "certego_saas.ext.exceptions.custom_exception_handler",
    # Filter
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework_filters.backends.RestFrameworkFilterBackend",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "387157645539-fplh8sracssg61f6bfqo6bf96cbp3mlh.apps.googleusercontent.com"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"
# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

# Django-Rest-Durin
REST_DURIN = {
    "DEFAULT_TOKEN_TTL": timedelta(days=14),
    "TOKEN_CHARACTER_LENGTH": 32,
    "USER_SERIALIZER": "certego_saas.user.serializers.UserSerializer",
    "AUTH_HEADER_PREFIX": "Token",
    "TOKEN_CACHE_TIMEOUT": 300,  # 5 minutes
    "REFRESH_TOKEN_ON_LOGIN": True,
    "API_ACCESS_CLIENT_NAME": "PyIntelOwl",
    "API_ACCESS_EXCLUDE_FROM_SESSIONS": True,
    "API_ACCESS_RESPONSE_INCLUDE_TOKEN": True,
    # not part of durin but used in data migration
    "API_ACCESS_CLIENT_TOKEN_TTL": timedelta(days=3650),
}

# drf-spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "IntelOwl API specification",
    "VERSION": VERSION,
}

# drf-recaptcha (not used in IntelOwl but required by certego-saas pkg)
DRF_RECAPTCHA_SECRET_KEY = ""
DRF_RECAPTCHA_TESTING = True
DRF_RECAPTCHA_TESTING_PASS = True
