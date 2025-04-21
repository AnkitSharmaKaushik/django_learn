# Build and Run 
<!-- docker-compose build
docker-compose up -->
<!-- docker-compose build
docker-compose up -d -->
# To view logs:
<!-- docker-compose logs -f web
docker-compose logs -f worker
docker-compose logs -f beat -->

# Run Celery in Docker
<!-- You already have this in your docker-compose.yml:

worker runs celery -A config worker

beat runs celery -A config beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -->

# You’re now ready to:
<!-- docker-compose up -d --build -->

# You Can Now:
<!-- Run async background jobs with .delay() or .apply_async()

Schedule tasks via Django Admin (from django_celery_beat)

Monitor logs with docker-compose logs -f worker -->

# Migrate Celery Beat Tables
<!-- python manage.py migrate django_celery_beat -->

#  Create an Interval & Periodic Task (Programmatically)
<!-- You can automate this with a script or via Django shell:
python manage.py shell
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# every 10 seconds
schedule, _ = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)

PeriodicTask.objects.create(
    interval=schedule,
    name='Print Time Every 10 Secs',
    task='myapp.tasks.print_current_time',
) -->

# Run Everything
# Your Docker Compose should already have:
  <!-- beat:
    command: celery -A config beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
docker-compose up -d --build
docker-compose logs -f beat -->
# from django_celery_beat.models import CrontabSchedule, PeriodicTask

# Runs every day at 9:30 AM
<!-- cron_schedule = CrontabSchedule.objects.create(minute='30', hour='9')

PeriodicTask.objects.create(
    crontab=cron_schedule,
    name='Daily Report Task',
    task='myapp.tasks.daily_report_task',
) -->


# Celery Beat Setup Complete!
<!-- You now have a full background + periodic task setup using:

Celery Worker

Redis Broker

Celery Beat Scheduler

Django Admin/DB to control schedules -->

# Start Everything
docker-compose up -d --build
# Access Flower UI
<!-- http://localhost:5555
You’ll see a dashboard with:

Worker status

Task names and count

Real-time log of executed tasks

Queues and scheduled tasks -->


# Secure Flower (Optional)
<!-- For production, you can set up:

Authentication with --basic_auth=user:password

Reverse proxy behind Nginx

SSL using Let’s Encrypt or Cloudflare -->

<!-- command: flower --broker=redis://redis:6379/0 --port=5555 --basic_auth=admin:admin123 -->

# Flower Monitoring Ready!
<!-- You can now:

Monitor task queues live

Retry/revoke tasks from UI

View task arguments/results

Filter by task names or status -->

# Let's gooo! 🔥 Time to build Async APIs using Celery and Django REST Framework to trigger long-running or background tasks from your API. This is super helpful when you don’t want the client to wait—like:

<!-- Sending emails

Processing uploaded files

Notifying users

Hitting 3rd-party APIs -->

# Test It Out
<!-- ➕ POST to trigger:

POST /api/process-user/
{
    "user_id": "123"
}
Response:

json
Copy
Edit
{
    "message": "Task has been queued.",
    "task_id": "09cb2a3a-xxxx-xxxx"
}
➕ GET status:

GET /api/task-status/09cb2a3a-xxxx-xxxx/ -->

# Why This Rocks?
<!-- Client gets immediate feedback: ✅

Task gets processed in background: ⚙️

Status is trackable via Task ID: 📈 -->

# Install Django Channels
<!-- Update Django Settings
Create asgi.py
Create a WebSocket Consumer
Setup Routing -->

# Frontend Connection (Example: JS/React)

<!-- const socket = new WebSocket('ws://localhost:8000/ws/notifications/');

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    alert(data.message);  // or show in toast
}; -->

# Boom! Real-Time Notifications Are Live
<!-- Worker finishes async task ✅

Sends event to WebSocket group ✅

Browser receives instant update ✅ -->

# Optional Enhancements:
<!-- Target individual users via dynamic groups: notifications_user_<id>

Also send email in task using send_mail

Push notification via Firebase or OneSignal -->

#  frontend WebSocket trigger
<!-- Let’s get the frontend WebSocket trigger ready! 🔥 We’ll use React here to create a simple real-time notification component that listens to the WebSocket server (powered by Django Channels) and shows notifications as they arrive. -->

<!-- Setup in React (Notification Component)
File: src/components/NotificationSocket.js
import React, { useEffect, useState } from "react";

const NotificationSocket = () => {
  const [messages, setMessages] = useState([]);
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/notifications/"); // Use actual domain on production

    socket.onopen = () => {
      console.log("WebSocket connected!");
      setConnected(true);
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data.message]);
    };

    socket.onclose = () => {
      console.warn("WebSocket disconnected.");
      setConnected(false);
    };

    socket.onerror = (err) => {
      console.error("WebSocket error:", err);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div className="fixed top-4 right-4 w-96 z-50">
      {messages.map((msg, index) => (
        <div
          key={index}
          className="bg-blue-500 text-white p-4 mb-2 rounded shadow-md animate-bounce"
        >
          🔔 {msg}
        </div>
      ))}
    </div>
  );
};

export default NotificationSocket; -->


# How to Use It
<!-- Import the component in your main App.js or wherever you want to trigger notifications: -->
<!-- import NotificationSocket from "./components/NotificationSocket";

function App() {
  return (
    <div className="App">
      <NotificationSocket />
      {/* Other components */}
    </div>
  );
} -->

#  Production Domain Handling
<!-- In production:
const socket = new WebSocket(
  `wss://${window.location.host}/ws/notifications/`
); -->

<!-- TailwindCSS for Styling (Optional)
Make sure you have TailwindCSS set up in your project. If not:
npm install -D tailwindcss
npx tailwindcss init -->

# Next Steps:
<!-- Wanna integrate with:

toasts (like react-toastify)

user-specific channels (e.g. notifications per logged-in user)

push notification (via Firebase or OneSignal) -->

# Trigger Task with Email
<!-- Wherever you're triggering the task:
process_user_data.delay(user.id, user.email) -->

# Local Testing Email Option (Optional)
<!-- In development, use Django’s console email backend:
process_user_data.delay(user.id, user.email) -->

# Bonus Ideas
<!-- Send rich HTML emails using EmailMultiAlternatives

Use templates for emails (render_to_string)

Track email send status in your database

Use SendGrid, Amazon SES, or Mailgun in production -->

# Would you like help with:

<!-- htmltemplateemail

mailproviderintegration (e.g., SES, SendGrid)

usernotificationsmodel to track sent notifications in DB -->


# ✅ Prerequisites Checklist
<!-- ✅ Dockerized Django project (already done)
✅ Celery & Redis setup (done)
✅ Channels (WebSockets) support
✅ Email notify (done)
✅ React frontend (optional) -->


# AWS Account with:
<!-- EC2 Access

IAM Role or access/secret keys

S3 bucket (optional for static/media)

RDS PostgreSQL (or any DB) -->

# Deployment (Production Setup)

<!-- Create & Setup EC2 Instance
Launch EC2 (Ubuntu 22.04)

Allow ports:

22 (SSH),

80 (HTTP),

443 (HTTPS),

8000 (WebSocket/testing)

6379 (if Redis on same instance) -->

# SSH into the instance:
<!-- ssh -i your-key.pem ubuntu@your-ec2-ip -->
# Install Docker & Docker Compose
<!-- sudo apt update && sudo apt install docker.io docker-compose -y
sudo usermod -aG docker ubuntu
newgrp docker -->
# Clone Your Repo & Set Environment Vars
<!-- git clone https://github.com/yourname/yourproject.git
cd yourproject
cp .env.example .env  # Or set your variables in .env -->
# Your .env should include:
<!-- DEBUG=False
ALLOWED_HOSTS=your-ec2-ip, your-domain.com
SECRET_KEY=your_secret
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=your-rds-host.amazonaws.com
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=... -->

# Run Docker Compose
<!-- docker-compose -f docker-compose.prod.yml up -d --build
if you have a single docker-compose.yml file:
docker-compose up -d --build -->

# Collect Static Files + Migrate
<!-- docker exec -it your_web_container python manage.py collectstatic --noinput
docker exec -it your_web_container python manage.py migrate -->

# Setup SSL (Let’s Encrypt + Nginx)
<!-- Use Nginx + Certbot, or use AWS ACM if behind ELB. -->
<!-- Run Celery and Beat in Production:
Update docker-compose.yml:
  celery:
    build: .
    command: celery -A core worker --loglevel=info
    volumes:
      - .:/app
    depends_on:
      - redis
      - db

  beat:
    build: .
    command: celery -A core beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    volumes:
      - .:/app
    depends_on:
      - redis
      - db -->

# Channels & Daphne/Gunicorn
<!-- If using Channels:
daphne -b 0.0.0.0 -p 8000 core.asgi:application -->

# Storage (Optional)
<!-- Use Amazon S3 for media/static: -->
# settings.py
<!-- DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = ...
AWS_SECRET_ACCESS_KEY = ...
AWS_STORAGE_BUCKET_NAME = ...
Install boto3 and django-storages. -->

# RDS Setup for Django (PostgreSQL)

<!-- Perfect! Let’s connect your Django project to AWS RDS (PostgreSQL) so your app runs on a managed, scalable database 📊 -->

<!-- Step 1: Create a PostgreSQL RDS Instance
Go to AWS Console → RDS → "Create database"

Choose:

Standard Create

Engine: PostgreSQL

Version: Preferably 14 or 15

Set DB instance identifier (e.g., my-django-db)

Set:

Master username: django

Master password: your_secure_password

Choose Free Tier if testing.

In connectivity section:

VPC: Default or create new

Public access: Enable ✅ (for testing)

VPC security group: Create or attach a group that allows inbound on port 5432

Create database and wait for it to become Available. -->

# Get DB Endpoint
<!-- Once RDS is ready, go to the instance → copy the Endpoint, e.g.:
my-django-db.abcdefghij.us-east-1.rds.amazonaws.com -->

# Update Django Settings (.env or settings.py)
<!-- Add the following in .env:
DEBUG=False
DB_ENGINE=django.db.backends.postgresql
DB_NAME=mydbname
DB_USER=django
DB_PASSWORD=your_secure_password
DB_HOST=my-django-db.abcdefghij.us-east-1.rds.amazonaws.com
DB_PORT=5432 -->

# And in settings.py (or wherever you parse env vars):
<!-- DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
} -->

# Run Migrations
<!-- Once Docker containers are running, apply migrations: -->
<!-- docker-compose exec web python manage.py migrate -->
# Optional: Harden Security
<!-- ✅ Make the RDS instance private (disable public access)

✅ Use bastion host or SSH tunneling to access

✅ Enable SSL connection in Django using: -->

<!-- OPTIONS = {
    'sslmode': 'require',
} -->

# Optional: Add RDS to VPC & EC2
<!-- If your EC2 app and RDS DB are in same VPC, you can:

Use private IP of RDS (recommended for security)

Avoid making DB public -->

# Bonus Tips
<!-- ✅ Enable automated backups in RDS

✅ Enable Multi-AZ failover in production

✅ Enable monitoring & alarms -->

# S3 Integration with Django
<!-- Install Required Packages
pip install boto3 django-storages
Also, update your requirements.txt or pyproject.toml. -->
# Update settings.py
<!-- First, make sure storages is in INSTALLED_APPS:
INSTALLED_APPS = [
    ...
    'storages',
] -->

<!-- Then add these settings: -->

<!-- import os

# Use S3 for default file storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Optional: You can also use S3 for static files
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "us-east-1")
AWS_QUERYSTRING_AUTH = False  # Optional: Makes file URLs publicly accessible

# Optional: media file settings
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/' -->


# Add AWS Credentials to .env
<!-- AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1 -->

# 🪣 Step 4: Create Your S3 Bucket
<!-- Go to AWS → S3 → Create Bucket

Choose a globally unique name: your-bucket-name

Disable "Block all public access" if you want media files to be publicly accessible

Enable static website hosting (optional)

Go to Permissions tab → Bucket policy: -->

<!-- {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::your-bucket-name/*"]
    }
  ]
} -->


# Test Uploads
<!-- Upload an image via the Django admin or a form, and check if it's saved to S3.
Use Custom Storage Classes
You can define your own storage for static and media: -->

# storage_backends.py

<!-- from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

class StaticStorage(S3Boto3Storage):
    location = 'static' -->


<!-- Then in settings.py: -->
<!-- DEFAULT_FILE_STORAGE = 'yourapp.storage_backends.MediaStorage'
STATICFILES_STORAGE = 'yourapp.storage_backends.StaticStorage' -->

# Add CloudFront (Set up CloudFront for CDN caching with S3?)
<!-- Let's integrate Amazon CloudFront with your S3 + Django project to serve media/static files via a super-fast CDN 🌍⚡

This improves performance, reduces latency, and adds caching + HTTPS support for your static and media files. -->

# CloudFront + S3 Integration for Django:
 <!-- Step 1: Create a CloudFront Distribution
Go to AWS Console → CloudFront

Click Create Distribution

Under Origin Settings:

Origin domain → select your S3 bucket

If bucket is private: enable Origin Access Control (OAC) (recommended)

Viewer Protocol Policy: Redirect HTTP to HTTPS

Cache Policy: Use default or create a custom one

Click Create Distribution -->
# After creation, note down the CloudFront Domain Name, e.g.:
<!-- d2f6abcd1234.cloudfront.net -->

#  Set Bucket Permissions for CloudFront
<!-- If you're using OAC:

Go to S3 bucket → Permissions → Bucket Policy

Add this (replace your-cloudfront-id and your-bucket-name): -->

<!-- {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontServicePrincipalReadOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::YOUR-AWS-ACCOUNT-ID:distribution/YOUR-DISTRIBUTION-ID"
        }
      }
    }
  ]
} -->

<!-- Or if using legacy public access, make files public (not recommended for secure apps). -->

# Update settings.py with CloudFront URLs
<!-- Replace MEDIA_URL and STATIC_URL: -->
<!-- CLOUDFRONT_DOMAIN = os.getenv("CLOUDFRONT_DOMAIN")

MEDIA_URL = f"https://{CLOUDFRONT_DOMAIN}/media/"
STATIC_URL = f"https://{CLOUDFRONT_DOMAIN}/static/" -->

# Optional Custom Storages (to separate static/media)
# storage_backends.py

<!-- class MediaStorage(S3Boto3Storage):
    location = 'media'
    custom_domain = os.getenv("CLOUDFRONT_DOMAIN")

class StaticStorage(S3Boto3Storage):
    location = 'static'
    custom_domain = os.getenv("CLOUDFRONT_DOMAIN") -->
<!-- 
In settings.py:
DEFAULT_FILE_STORAGE = 'yourapp.storage_backends.MediaStorage'
STATICFILES_STORAGE = 'yourapp.storage_backends.StaticStorage' -->

#  Collect & Upload Static Files
<!-- docker-compose exec web python manage.py collectstatic
Now open any media/static file and test with your CloudFront URL:
https://d2f6abcd1234.cloudfront.net/media/profile.png -->

# Optional Add-ons
<!-- ✅ Custom Domain for CloudFront: map your CDN to cdn.yourdomain.com

✅ SSL Certificate: via AWS ACM + CloudFront

✅ Cache Invalidation: for updated static files:

aws cloudfront create-invalidation \
  --distribution-id YOUR_DISTRIBUTION_ID \
  --paths "/static/*" -->

# GitHub Actions CI/CD
<!-- Set up GitHub Actions CI/CD to auto-deploy to EC2 or ECS? -->
<!-- Awesome! Let’s set up GitHub Actions CI/CD for your Django + Docker + AWS project 🚀

This setup will:

✅ Build and test your Django project
✅ Build and push Docker image to Amazon ECR
✅ SSH into EC2 and pull the image + restart container
✅ Keep secrets safe using GitHub Secrets
✅ Make deployments automated, clean, and repeatable -->

<!-- Project Structure (Recap)

.
├── .github/
│   └── workflows/
│       └── deploy.yml      👈 Our GitHub Actions file
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── app/
│   └── ... -->


# Step 1: AWS Setup
<!-- 🔑 Prerequisites:
Create an ECR repo (e.g., myproject-django)

Launch an EC2 instance and install Docker + Docker Compose

Add the EC2 SSH key + AWS creds to GitHub Secrets: -->

<!-- GitHub Secret Name    | Description
AWS_ACCESS_KEY_ID     | Your AWS access key
AWS_SECRET_ACCESS_KEY | Your AWS secret key
EC2_HOST              | Public IP or domain of your EC2
EC2_USER              | Usually ubuntu, ec2-user, etc.
EC2_KEY               | The private SSH key (multi-line)
ECR_REPO              | ECR repo URL (no https://)
REGION                | AWS region (e.g. us-east-1) -->


# github/workflows/deploy.yml

<!-- name: Deploy to EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: ${{ secrets.REGION }}

    - name: Log in to Amazon ECR
      id: login-ecr
      uses: aws-actions/amazon-ecr-login@v1

    - name: Build, Tag, and Push Docker Image
      run: |
        IMAGE="${{ secrets.ECR_REPO }}:latest"
        docker build -t $IMAGE .
        docker push $IMAGE

    - name: Copy SSH Key
      run: |
        echo "${{ secrets.EC2_KEY }}" > ec2_key.pem
        chmod 600 ec2_key.pem

    - name: SSH into EC2 and Deploy
      run: |
        ssh -o StrictHostKeyChecking=no -i ec2_key.pem ${{ secrets.EC2_USER }}@${{ secrets.EC2_HOST }} << 'EOF'
          aws ecr get-login-password --region ${{ secrets.REGION }} | docker login --username AWS --password-stdin ${{ secrets.ECR_REPO }}
          docker pull ${{ secrets.ECR_REPO }}:latest
          docker stop myapp || true && docker rm myapp || true
          docker run -d --name myapp -p 80:8000 ${{ secrets.ECR_REPO }}:latest
        EOF -->


#  Push to main
<!-- Now just commit and push to the main branch:
git add .
git commit -m "Add CI/CD with GitHub Actions"
git push origin main -->

<!-- 
It will:

Build & push Docker image to ECR

SSH into EC2

Pull and restart the container -->

# Extras

<!-- Auto-migrate on deploy: Add this inside the EC2 SSH block after container run:
docker exec myapp python manage.py migrate
✅ Use Docker Compose instead of docker run (if you have multiple services)

✅ Add Slack/Email Notification step if deployment fails or succeeds -->


# next we do 
<!-- Would you like to:

Setup GitHub Actions for tests + coverage?

Use ECS/Fargate instead of EC2 for scalable infra?

Setup Route53 + HTTPS certs via GitHub Actions?

Set environment-specific CI/CD (staging vs production)? -->













































