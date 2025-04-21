# ├── .env                          # Environment variables
# ├── docker-compose.yml           # Docker compose config for services
# ├── docker
# │   ├── django.Dockerfile        # Dockerfile for Django app
# │   ├── celery.Dockerfile        # Dockerfile for Celery workers
# │   ├── nginx.conf               # Nginx reverse proxy config
# │   └── rabbitmq.conf            # Optional custom RabbitMQ config
# │
# ├── config                       # Django core project
# │   ├── __init__.py
# │   ├── asgi.py                  # For Channels/WebSocket
# │   ├── celery.py                # Celery app initialization
# │   ├── urls.py
# │   └── settings
# │       ├── __init__.py
# │       ├── base.py              # Common settings
# │       ├── local.py             # Dev environment settings
# │       └── production.py        # Production/AWS settings
# │
# ├── requirements
# │   ├── base.txt                 # Django, DRF, Celery, etc.
# │   ├── dev.txt                  # Debug toolbar, pytest
# │   └── production.txt           # gunicorn, boto3, psycopg2
# │
# ├── .github
# │   └── workflows
# │       └── ci-cd.yml            # GitHub Actions CI/CD
# │
# ├── infrastructure
# │   ├── terraform/               # Terraform for AWS infra
# │   └── cloudformation/         # CloudFormation templates (optional)
# │
# ├── static/                      # Collected static files
# ├── media/                       # Media files from users
# │
# ├── services
# │   ├── auth/                    # JWT Auth, user management
# │   │   ├── models.py
# │   │   ├── views.py
# │   │   ├── serializers.py
# │   │   └── urls.py
# │   ├── survey/                  # Survey logic
# │   │   ├── models.py
# │   │   ├── views.py
# │   │   ├── tasks.py             # Celery async logic
# │   │   └── urls.py
# │   ├── notifications/          # WebSocket + Celery + Email
# │   │   ├── consumers.py        # Channels WebSocket consumer
# │   │   ├── routing.py
# │   │   ├── tasks.py
# │   │   └── urls.py
# │   ├── analytics/              # MongoDB Integration
# │   │   ├── models.py
# │   │   ├── views.py
# │   │   └── mongodb.py
# │
# ├── templates/
# │   └── base.html                # Template rendering
# │
# ├── logs/
# │   └── gunicorn.log             # Production logs
# │
# └── manage.py
