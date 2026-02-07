# Steve Ongera - Django Portfolio

A modern, responsive portfolio website built with Django, Bootstrap 5, and Tailwind CSS. This portfolio showcases projects, blog posts, skills, and professional experience.

## Features

- 🎨 Modern and responsive design
- 📱 Mobile-friendly with responsive sidebar
- 🎯 Featured and recent blog posts
- 💼 Project showcase
- 📝 Contact form
- 🎓 Resume/CV section
- 📊 Skills with progress bars
- 💬 Testimonials
- 🔍 SEO optimized
- ⚡ Fast and lightweight

## Technologies Used

- **Backend**: Django 4.2
- **Frontend**: 
  - Bootstrap 5
  - Tailwind CSS
  - Bootstrap Icons
  - Vanilla JavaScript
- **Database**: SQLite (development) / PostgreSQL (production)
- **Deployment**: Gunicorn + Whitenoise

## Installation

### Prerequisites

- Python 3.8 or higher
- pip
- virtualenv (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/steveongera/portfolio.git
cd portfolio_project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Run the development server:
```bash
python manage.py runserver
```

9. Access the website at `http://localhost:8000`

## Project Structure

```
portfolio_project/
├── portfolio/              # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   └── __init__.py
├── portfolio_project/     # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   └── index.html         # Home page
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Custom CSS
│   └── js/
│       └── main.js        # Custom JavaScript
├── media/                 # User uploaded files
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Usage

### Admin Panel

Access the admin panel at `http://localhost:8000/admin` using your superuser credentials.

You can manage:
- Blog posts and categories
- Projects
- Skills
- Experience and education
- Certifications
- Contact form submissions
- Testimonials

### Customization

1. **Colors**: Edit CSS variables in `static/css/style.css`
2. **Logo**: Replace the logo in the navigation
3. **Content**: Update content through the Django admin panel
4. **Images**: Add images to the `media/` directory

## Deployment

### Using Heroku

1. Install Heroku CLI
2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Add PostgreSQL:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Set environment variables:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
```

5. Deploy:
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Using AWS/DigitalOcean

1. Set up a server with Ubuntu
2. Install Python, PostgreSQL, and Nginx
3. Clone the repository
4. Set up virtual environment and install dependencies
5. Configure Gunicorn and Nginx
6. Set up SSL with Let's Encrypt

## Features to Add

- [ ] Dark mode toggle
- [ ] Blog comment system
- [ ] Search functionality
- [ ] Tags for blog posts
- [ ] Social media integration
- [ ] Analytics dashboard
- [ ] Newsletter subscription
- [ ] Multi-language support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- **Email**: steve.ongera@example.com
- **LinkedIn**: [Steve Ongera](https://linkedin.com/in/steveongera)
- **GitHub**: [steveongera](https://github.com/steveongera)
- **Twitter**: [@steveongera](https://twitter.com/steveongera)

## Acknowledgments

- Design inspired by modern portfolio websites
- Icons by Bootstrap Icons
- Fonts by Google Fonts
- Color palette inspired by Tailwind CSS

---

Made with ❤️ by Steve Ongera
