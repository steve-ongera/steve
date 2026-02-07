# Steve Ongera - Django Portfolio Project

## 📋 Project Overview

This is a complete Django portfolio website based on the Geeky blog theme design. It includes:

✅ **Fully responsive design** (Bootstrap 5 + Tailwind CSS)
✅ **Mobile-friendly navigation** with collapsible sidebar
✅ **Django backend** with admin panel
✅ **Blog functionality** with featured/recent posts
✅ **Project showcase** section
✅ **Skills & experience** display
✅ **Contact form** with database storage
✅ **SEO optimized** structure

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Setup Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Step 3: Run Server
```bash
python manage.py runserver
```

Visit: **http://localhost:8000**

## 📁 Project Structure

```
portfolio_project/
│
├── templates/
│   ├── base.html          # Main template with navbar & footer
│   └── index.html         # Homepage with all sections
│
├── static/
│   ├── css/
│   │   └── style.css      # Custom styles + animations
│   └── js/
│       └── main.js        # Interactive features
│
├── portfolio/             # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions with data
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin panel config
│
├── portfolio_project/     # Project settings
│   ├── settings.py        # Django configuration
│   └── urls.py            # Main URL config
│
├── manage.py              # Django CLI
├── requirements.txt       # Python packages
└── README.md             # Documentation
```

## 🎨 Features from Original Design

### ✓ Navigation Bar
- Logo with brand name "steveongera"
- Menu items: Home, About, Projects, Contact, Pages (dropdown)
- Social media icons (Facebook, Twitter, LinkedIn, Instagram, YouTube, GitHub)
- Dark mode toggle icon
- "Hire Me" CTA button
- Responsive mobile menu

### ✓ Hero Section
- Large welcome heading with green accent
- Professional photo placeholder
- Floating icons (camera, images, PDF, search)
- Call-to-action button

### ✓ Featured Posts
- Large featured post card with "Geeky" badge
- Side featured posts (3 items)
- "Thank you for staying home" banner

### ✓ Recent Posts
- 6 post cards in grid layout
- Category badges
- Author and date information
- "Read More" buttons
- Pagination (Previous, 1, 2, 3, Next)

### ✓ Footer
- About section with logo
- Featured posts preview
- Newsletter signup form
- Social media links
- Bottom links (Home, About, Contact, Privacy Policy)
- Copyright notice

## 🎯 Customization Guide

### 1. Update Personal Information

**In `templates/base.html`:**
- Line 15: Change "steveongera" to your name
- Lines 27-33: Update navigation links
- Lines 36-41: Add your social media URLs

**In `templates/index.html`:**
- Lines 11-13: Update hero heading
- Line 15: Change welcome text
- Lines 189-192: Update contact information

### 2. Change Colors

**In `static/css/style.css`:**
```css
:root {
    --primary-color: #10b981;    /* Change to your color */
    --secondary-color: #059669;   /* Darker shade */
}
```

### 3. Add Your Photo

Replace placeholder images in `templates/index.html`:
- Line 23: Hero image
- Lines throughout for blog post images

### 4. Configure Skills

**In `portfolio/views.py` (home function):**
Update the skills list with your actual skills:
```python
skills = [
    {'name': 'Your Skill', 'percentage': 90},
]
```

### 5. Add Blog Posts

**Via Django Admin:**
1. Go to `http://localhost:8000/admin`
2. Click "Posts" → "Add Post"
3. Fill in details and upload image
4. Check "Featured" for homepage display

**Via Code (views.py):**
Update `featured_posts` and `recent_posts` dictionaries

## 💻 Django Features

### Models Available:
- **Post** - Blog posts with categories
- **Project** - Portfolio projects
- **Skill** - Technical skills
- **Experience** - Work history
- **Education** - Academic background
- **Certification** - Professional certifications
- **Contact** - Form submissions
- **Testimonial** - Client reviews

### Admin Panel:
Access at `/admin` to manage all content

### URLs:
- `/` - Homepage
- `/about/` - About page
- `/projects/` - Projects showcase
- `/contact/` - Contact form
- `/resume/` - Resume/CV

## 🎨 Design Features

### Responsive Design:
- Desktop: Full navigation + sidebar
- Tablet: Collapsible menu
- Mobile: Off-canvas sidebar

### Animations:
- Floating hero icons
- Card hover effects
- Progress bar animations
- Smooth scrolling
- Button transitions

### Bootstrap 5 Components:
- Cards
- Navbar
- Buttons
- Forms
- Badges
- Pagination
- Offcanvas sidebar

### Custom Features:
- Sticky navigation
- Back to top button
- Loading animations
- Form validation
- Newsletter signup

## 📱 Responsive Breakpoints

```css
/* Mobile: < 576px */
/* Tablet: 576px - 768px */
/* Desktop: 768px - 992px */
/* Large: > 992px */
```

## 🔧 Development Commands

```bash
# Create new app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Django shell
python manage.py shell
```

## 📦 Technologies Used

### Backend:
- Django 4.2
- Python 3.8+
- SQLite (dev) / PostgreSQL (prod)

### Frontend:
- HTML5
- CSS3
- JavaScript (ES6+)
- Bootstrap 5.3
- Tailwind CSS
- Bootstrap Icons

### Tools:
- Gunicorn (WSGI server)
- Whitenoise (static files)
- Pillow (image processing)

## 🚀 Deployment Options

### Heroku:
```bash
heroku create your-app
heroku addons:create heroku-postgresql
git push heroku main
```

### Railway:
1. Connect GitHub repo
2. Add PostgreSQL
3. Deploy automatically

### DigitalOcean:
1. Create droplet
2. Install dependencies
3. Configure Nginx + Gunicorn
4. Set up SSL

### PythonAnywhere:
1. Upload code
2. Configure web app
3. Set static files path

## 🐛 Troubleshooting

### Static files not showing:
```bash
python manage.py collectstatic --clear
```

### Database errors:
```bash
python manage.py flush
python manage.py migrate
```

### Import errors:
```bash
pip install -r requirements.txt --upgrade
```

### Port already in use:
```bash
python manage.py runserver 8080
```

## 📝 To-Do List

- [ ] Add dark mode functionality
- [ ] Implement blog search
- [ ] Add comment system
- [ ] Create API endpoints
- [ ] Add testing suite
- [ ] Set up CI/CD
- [ ] Add Google Analytics
- [ ] Implement caching
- [ ] Add sitemap
- [ ] Configure email notifications

## 📄 License

MIT License - Free to use and modify

## 👤 Author

**Steve Ongera**
- Email: steve.ongera@example.com
- GitHub: [@steveongera](https://github.com/steveongera)
- LinkedIn: [Steve Ongera](https://linkedin.com/in/steveongera)

## 🙏 Acknowledgments

- Design inspired by Geeky NextJS template
- ThemeWagon for design reference
- Bootstrap team for amazing framework
- Django community for excellent documentation

---

**Happy Coding! 🚀**

For questions or support, open an issue or contact me directly.
