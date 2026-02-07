"""
Django management command to seed the database with sample data.

Usage:
    python manage.py seed_data
    python manage.py seed_data --clear  # Clear existing data first
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime, timedelta
import random

from portfolio.models import (
    Category, Post, Project, Skill, Experience,
    Education, Certification, Contact, Testimonial
)


class Command(BaseCommand):
    help = 'Seeds the database with sample data for the portfolio'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            self.clear_data()
            self.stdout.write(self.style.SUCCESS('✓ Data cleared'))

        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))
        
        # Create data
        user = self.create_users()
        categories = self.create_categories()
        self.create_posts(user, categories)
        self.create_projects()
        self.create_skills()
        self.create_experience()
        self.create_education()
        self.create_certifications()
        self.create_contacts()
        self.create_testimonials()
        
        self.stdout.write(self.style.SUCCESS('\n✓ Database seeded successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now login to admin with:'))
        self.stdout.write(self.style.SUCCESS('  Username: admin'))
        self.stdout.write(self.style.SUCCESS('  Password: admin123'))

    def clear_data(self):
        """Clear all existing data"""
        Category.objects.all().delete()
        Post.objects.all().delete()
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Contact.objects.all().delete()
        Testimonial.objects.all().delete()

    def create_users(self):
        """Create admin user"""
        self.stdout.write('Creating users...')
        
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'first_name': 'Steve',
                'last_name': 'Ongera',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created admin user'))
        else:
            self.stdout.write(self.style.WARNING(f'  - Admin user already exists'))
        
        return user

    def create_categories(self):
        """Create blog categories"""
        self.stdout.write('Creating categories...')
        
        categories_data = [
            {'name': 'Technology', 'description': 'Latest tech trends and innovations'},
            {'name': 'Programming', 'description': 'Coding tutorials and best practices'},
            {'name': 'Django', 'description': 'Django framework tutorials'},
            {'name': 'Python', 'description': 'Python programming guides'},
            {'name': 'JavaScript', 'description': 'JavaScript and frameworks'},
            {'name': 'Tutorial', 'description': 'Step-by-step tutorials'},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'slug': slugify(cat_data['name']),
                    'description': cat_data['description']
                }
            )
            categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created category: {category.name}'))
        
        return categories

    def create_posts(self, user, categories):
        """Create blog posts"""
        self.stdout.write('Creating blog posts...')
        
        posts_data = [
            {
                'title': 'What is a Virtual Assistant',
                'excerpt': 'Discover how virtual assistants are revolutionizing the way we work.',
                'content': 'Virtual assistants are AI-powered software programs that help automate tasks...',
                'category': 'Technology',
                'is_featured': True,
            },
            {
                'title': 'Django Best Practices',
                'excerpt': 'Learn essential best practices for building Django applications.',
                'content': 'Django is a powerful framework. Following best practices ensures...',
                'category': 'Django',
                'is_featured': True,
            },
            # Add more posts as needed
        ]
        
        for post_data in posts_data:
            category = next((c for c in categories if c.name == post_data['category']), categories[0])
            
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'slug': slugify(post_data['title']),
                    'author': user,
                    'category': category,
                    'excerpt': post_data['excerpt'],
                    'content': post_data['content'],
                    'is_featured': post_data['is_featured'],
                    'views': random.randint(50, 500),
                    'published': True,
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created post: {post.title}'))

    def create_projects(self):
        """Create projects"""
        self.stdout.write('Creating projects...')
        
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'Full-featured e-commerce platform with Django and React.',
                'technologies': 'Django, React, PostgreSQL, Stripe',
                'is_featured': True,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'slug': slugify(project_data['title']),
                    'description': project_data['description'],
                    'technologies': project_data['technologies'],
                    'is_featured': project_data['is_featured'],
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created project: {project.title}'))

    def create_skills(self):
        """Create skills"""
        self.stdout.write('Creating skills...')
        
        skills_data = [
            {'name': 'Python/Django', 'percentage': 95, 'category': 'backend', 'order': 1},
            {'name': 'JavaScript/React', 'percentage': 85, 'category': 'frontend', 'order': 2},
            {'name': 'PostgreSQL', 'percentage': 90, 'category': 'database', 'order': 3},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created skill: {skill.name}'))

    def create_experience(self):
        """Create experience"""
        self.stdout.write('Creating experience...')
        
        experience_data = [
            {
                'position': 'Senior Django Developer',
                'company': 'Tech Solutions Ltd',
                'start_date': datetime(2023, 1, 1).date(),
                'description': 'Leading web development projects.',
                'responsibilities': 'Lead development\nMentor juniors\nCode reviews',
                'is_current': True,
            },
        ]
        
        for exp_data in experience_data:
            exp, created = Experience.objects.get_or_create(
                position=exp_data['position'],
                company=exp_data['company'],
                defaults=exp_data
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created experience: {exp.position}'))

    def create_education(self):
        """Create education"""
        self.stdout.write('Creating education...')
        
        edu_data = {
            'degree': 'BSc Computer Science',
            'institution': 'University of Nairobi',
            'start_year': 2016,
            'end_year': 2020,
        }
        
        edu, created = Education.objects.get_or_create(**edu_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created education: {edu.degree}'))

    def create_certifications(self):
        """Create certifications"""
        self.stdout.write('Creating certifications...')
        
        cert_data = {
            'name': 'AWS Developer Associate',
            'issuing_organization': 'Amazon',
            'issue_date': datetime(2023, 1, 1).date(),
        }
        
        cert, created = Certification.objects.get_or_create(**cert_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created certification: {cert.name}'))

    def create_contacts(self):
        """Create sample contacts"""
        self.stdout.write('Creating contacts...')
        
        contact_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Project Inquiry',
            'message': 'Hi, I would like to discuss a project.',
        }
        
        contact, created = Contact.objects.get_or_create(
            email=contact_data['email'],
            defaults=contact_data
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created contact: {contact.name}'))

    def create_testimonials(self):
        """Create testimonials"""
        self.stdout.write('Creating testimonials...')
        
        test_data = {
            'name': 'Jane Smith',
            'position': 'CEO',
            'company': 'Tech Corp',
            'content': 'Steve is an excellent developer!',
            'rating': 5,
            'is_featured': True,
        }
        
        test, created = Testimonial.objects.get_or_create(
            name=test_data['name'],
            company=test_data['company'],
            defaults=test_data
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'  ✓ Created testimonial: {test.name}'))