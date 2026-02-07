from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

def home(request):
    """
    Home page view with featured and recent posts
    """
    # Featured posts data
    featured_posts = [
        {
            'title': 'Drone Software and Development',
            'date': '04 Apr 2022',
            'image': 'drone.jpg',
            'category': 'Technology'
        },
        {
            'title': 'How to make toys from old Oldpaper',
            'date': '04 Apr 2022',
            'image': 'toys.jpg',
            'category': 'DIY'
        },
        {
            'title': 'My work from home workstation',
            'date': '29 Apr 2022',
            'image': 'workstation.jpg',
            'category': 'Lifestyle'
        },
    ]
    
    # Recent posts data
    recent_posts = [
        {
            'title': 'How to make toys from old Oldpaper',
            'author': 'steveongera',
            'date': '24 July 2022',
            'excerpt': 'Nemo vel ad consectetur namkd etfd ium voluptatibus volupt enim ipsum, voluptas ut totam, quisquamm beatae.',
            'image': 'robot.jpg',
            'category': 'DIY'
        },
        {
            'title': 'What you need to know about Programming',
            'author': 'steveongera',
            'date': '24 July 2022',
            'excerpt': 'Nemo vel ad consectetur namkd etfd ium voluptatibus volupt enim ipsum, voluptas ut totam.',
            'image': 'programming.jpg',
            'category': 'Geeky'
        },
        {
            'title': 'Why you need to learn PHP',
            'author': 'steveongera',
            'date': '24 July 2022',
            'excerpt': 'Nemo vel ad consectetur namkd etfd ium voluptatibus volupt enim ipsum, voluptas ut totam.',
            'image': 'php.jpg',
            'category': 'Programming'
        },
        {
            'title': 'What is a Virtual Assistant',
            'author': 'steveongera',
            'date': '24 July 2022',
            'excerpt': 'Nemo vel ad consectetur namkd etfd ium voluptatibus volupt enim ipsum, voluptas ut totam.',
            'image': 'virtual_assistant.jpg',
            'category': 'Geeky'
        },
        {
            'title': 'Robotic world is growing very fast',
            'author': 'steveongera',
            'date': '24 July 2022',
            'excerpt': 'Nemo vel ad consectetur namkd etfd ium voluptatibus volupt enim ipsum, voluptas ut totam.',
            'image': 'robotics.jpg',
            'category': 'Technology'
        },
        {
            'title': 'My work from home workstation',
            'author': 'steveongera',
            'date': '24 July 2022',
            'excerpt': 'Nemo vel ad consectetur namkd etfd ium voluptatibus volupt enim ipsum, voluptas ut totam.',
            'image': 'workspace.jpg',
            'category': 'Programming'
        },
    ]
    
    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'page_title': 'Home',
    }
    
    return render(request, 'index.html', context)


def about(request):
    """
    About page view
    """
    skills = [
        {'name': 'Python/Django', 'percentage': 95},
        {'name': 'JavaScript/React', 'percentage': 85},
        {'name': 'HTML/CSS/Bootstrap', 'percentage': 95},
        {'name': 'PostgreSQL/MySQL', 'percentage': 90},
        {'name': 'REST API Development', 'percentage': 88},
        {'name': 'Cloud Deployment', 'percentage': 80},
    ]
    
    context = {
        'skills': skills,
        'page_title': 'About',
    }
    
    return render(request, 'about.html', context)


def projects(request):
    """
    Projects page view
    """
    projects_list = [
        {
            'title': 'E-Commerce Platform',
            'description': 'A full-featured e-commerce platform built with Django, featuring payment integration, product management, and order tracking.',
            'technologies': ['Django', 'PostgreSQL', 'Stripe', 'Bootstrap'],
            'image': 'ecommerce.jpg',
            'link': '#',
            'github': '#'
        },
        {
            'title': 'Task Management System',
            'description': 'A collaborative task management application with real-time updates, user authentication, and project tracking.',
            'technologies': ['Django', 'Django Channels', 'Redis', 'React'],
            'image': 'task_manager.jpg',
            'link': '#',
            'github': '#'
        },
        {
            'title': 'Blog Platform',
            'description': 'A modern blogging platform with markdown support, comment system, and social sharing features.',
            'technologies': ['Django', 'SQLite', 'TailwindCSS', 'JavaScript'],
            'image': 'blog.jpg',
            'link': '#',
            'github': '#'
        },
        {
            'title': 'REST API for Mobile App',
            'description': 'A robust REST API built with Django REST Framework for a mobile application with authentication and data synchronization.',
            'technologies': ['Django', 'DRF', 'JWT', 'PostgreSQL'],
            'image': 'api.jpg',
            'link': '#',
            'github': '#'
        },
    ]
    
    context = {
        'projects': projects_list,
        'page_title': 'Projects',
    }
    
    return render(request, 'projects.html', context)


def contact(request):
    """
    Contact page view
    """
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you would typically save to database or send email
        # For now, we'll just pass a success message
        context = {
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.',
            'page_title': 'Contact',
        }
        return render(request, 'contact.html', context)
    
    context = {
        'page_title': 'Contact',
    }
    
    return render(request, 'contact.html', context)


def resume(request):
    """
    Resume page view
    """
    education = [
        {
            'degree': 'Bachelor of Science in Computer Science',
            'institution': 'University of Nairobi',
            'year': '2018 - 2022',
            'description': 'Specialized in Software Engineering and Web Development'
        },
    ]
    
    experience = [
        {
            'position': 'Senior Django Developer',
            'company': 'Tech Solutions Ltd',
            'period': '2023 - Present',
            'responsibilities': [
                'Lead development of enterprise web applications',
                'Architected scalable REST APIs',
                'Mentored junior developers',
                'Implemented CI/CD pipelines'
            ]
        },
        {
            'position': 'Full Stack Developer',
            'company': 'Digital Agency',
            'period': '2022 - 2023',
            'responsibilities': [
                'Developed client websites and web applications',
                'Built responsive frontends with React and Bootstrap',
                'Managed database design and optimization',
                'Deployed applications to AWS and Heroku'
            ]
        },
    ]
    
    certifications = [
        'AWS Certified Developer - Associate',
        'Django Web Framework - Advanced',
        'Python for Data Science',
    ]
    
    context = {
        'education': education,
        'experience': experience,
        'certifications': certifications,
        'page_title': 'Resume',
    }
    
    return render(request, 'resume.html', context)


# Class-based views alternative
class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = [
            {
                'title': 'Drone Software and Development',
                'date': '04 Apr 2022',
                'image': 'drone.jpg',
                'category': 'Technology'
            },
            # Add more posts...
        ]
        context['recent_posts'] = [
            {
                'title': 'How to make toys from old Oldpaper',
                'author': 'steveongera',
                'date': '24 July 2022',
                'excerpt': 'Nemo vel ad consectetur namkd etfd ium voluptatibus volupt enim ipsum.',
                'image': 'robot.jpg',
                'category': 'DIY'
            },
            # Add more posts...
        ]
        return context
