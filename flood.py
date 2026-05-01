import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')  # change project name
django.setup()

from django.contrib.auth.models import User
from blog.models import Article

users = list(User.objects.filter(id__in=range(1, 10)))

titles = [
    "Exploring AI Trends",
    "Healthy Morning Habits",
    "Mastering Python",
    "Future of Web Apps",
    "Django Best Practices",
    "Clean Code Principles",
    "Fitness for Busy People",
    "Debugging Like a Pro",
    "Cloud Computing Basics",
    "Writing Better Code",
]

contents = [
    "This is a sample article content discussing various important aspects of the topic.",
    "A detailed explanation that helps readers understand the subject better.",
    "Practical insights and real-world examples are covered in this article.",
    "An easy guide to help beginners get started quickly.",
]

categories = ['technology', 'lifestyle', 'coding']

users = list(User.objects.filter(id__in=range(1, 10)))

articles = []

for i in range(25):
    article = Article(
        title=random.choice(titles) + f" #{i+1}",
        content=random.choice(contents),
        author=random.choice(users),
        category=random.choice(categories),
    )
    articles.append(article)

Article.objects.bulk_create(articles)

print("✅ 25 Articles created successfully!")