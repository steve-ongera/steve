# Django Portfolio Setup Guide

## Quick Start

1. **Install Python** (3.8 or higher)
   - Download from python.org
   - Verify: `python --version`

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup Database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Site**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Template Customization

### Update base.html
- Change logo and branding
- Update navigation links
- Modify footer content
- Add social media links

### Update index.html
- Customize hero section
- Add your personal information
- Update skills and technologies
- Add your projects

### Update CSS
- Edit `static/css/style.css`
- Modify color scheme
- Adjust responsive breakpoints
- Add custom animations

### Update JavaScript
- Edit `static/js/main.js`
- Add custom interactions
- Modify animations
- Add tracking scripts

## Adding Content via Admin

1. **Blog Posts**
   - Go to Admin > Posts > Add Post
   - Fill in title, content, category
   - Upload featured image
   - Check "Featured" for homepage display

2. **Projects**
   - Go to Admin > Projects > Add Project
   - Add project details
   - List technologies (comma-separated)
   - Add demo and GitHub links

3. **Skills**
   - Go to Admin > Skills > Add Skill
   - Enter skill name and percentage
   - Set category (Frontend/Backend/etc.)

4. **Experience**
   - Go to Admin > Experience > Add Experience
   - Enter job details
   - Add responsibilities (one per line)

## Deployment Checklist

- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up PostgreSQL database
- [ ] Configure static files serving
- [ ] Set up media files storage
- [ ] Configure email backend
- [ ] Set up SSL certificate
- [ ] Configure backup system
- [ ] Set up monitoring
- [ ] Test all functionality

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic
```

### Database errors
```bash
python manage.py flush
python manage.py migrate
```

### Permission errors
```bash
chmod +x manage.py
```

## Support

For issues or questions:
- Check README.md
- Review Django documentation
- Check Bootstrap 5 documentation
- Contact: steve.ongera@example.com
