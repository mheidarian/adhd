# ADHD Assessment Web Application

A comprehensive web application for ADHD (Attention-Deficit/Hyperactivity Disorder) assessment, providing a user-friendly platform with RTL (Right-to-Left) support for Persian language.

## Features

- **User Authentication**: Complete login, signup, password reset functionality
- **ADHD Assessment Test**: Interactive questionnaire to assess ADHD probability
- **Result Analysis**: Detailed interpretation of test scores
- **RTL Support**: Full Right-to-Left support for Persian language
- **Contact Form**: User feedback and inquiry system with admin dashboard
- **Responsive Design**: Works well on all devices (desktop, tablet, mobile)
- **Admin Panel**: Comprehensive admin interface for test management
- **Customizable Thresholds**: Administrators can adjust ADHD assessment thresholds

## Technology Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Django Allauth
- **Styling**: Custom RTL-compatible CSS
- **Fonts**: Google Fonts (Vazirmatn)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/adhd_project.git
   cd adhd_project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in your browser.

## Admin Panel

Access the admin panel at `/admin` and log in with your superuser credentials to:
- Manage tests and questions
- View test results
- Configure ADHD assessment thresholds
- Manage contact form submissions

## Deployment

This project is configured for easy deployment on platforms like:
- Heroku
- PythonAnywhere
- DigitalOcean

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Bootstrap for the responsive UI components
- Google Fonts for Vazirmatn font
- Django and Python communities for excellent documentation
