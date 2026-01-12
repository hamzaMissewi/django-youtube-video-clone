# Django YouTube Clone

A feature-rich YouTube clone built with Django 6.0, allowing users to upload, manage, and watch videos with modern web features.

## 🚀 Features

- **Video Upload & Management**: Upload videos with automatic thumbnail generation
- **User Authentication**: Complete user registration, login, and profile management
- **Video Streaming**: Optimized video streaming with multiple quality options
- **YouTube Integration**: Support for embedding YouTube videos
- **Engagement Metrics**: Track views, likes, and dislikes
- **Responsive Design**: Mobile-friendly interface using modern CSS
- **Image Processing**: Advanced image optimization using ImageKit.io

## 🛠️ Technology Stack

### Backend

- **Django 6.0**: High-level Python web framework
- **Python 3.13+**: Modern Python with latest features
- **SQLite**: Lightweight database for development
- **ImageKit.io**: Cloud-based image and video processing

### Frontend

- **HTML5**: Semantic markup for video content
- **CSS3**: Modern styling with responsive design
- **JavaScript**: Interactive features and video controls
- **Bootstrap**: UI framework for responsive components

### Development Tools

- **python-dotenv**: Environment variable management
- **Virtual Environment**: Isolated Python environment
- **Git**: Version control

## 📁 Project Structure

```
Django-YouTube-Clone/
├── youtube/                    # Main Django project directory
│   ├── youtube/                # Project settings and configuration
│   │   ├── settings.py        # Django settings
│   │   ├── urls.py           # Main URL configuration
│   │   └── wsgi.py           # WSGI configuration
│   ├── videos/                # Video management app
│   │   ├── models.py         # Video and related models
│   │   ├── views.py          # Video views and logic
│   │   ├── forms.py          # Video upload forms
│   │   ├── urls.py           # Video app URLs
│   │   ├── templates/        # Video templates
│   │   └── imagekit_client.py # ImageKit integration
│   ├── accounts/              # User authentication app
│   ├── static/               # Static files (CSS, JS, images)
│   ├── templates/             # Base templates
│   ├── manage.py             # Django management script
│   └── .env                  # Environment variables
├── .venv/                    # Virtual environment
├── pyproject.toml           # Project dependencies
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/hamzamissaoui/django-youtube-clone.git
   cd django-youtube-clone
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -e .
   ```

4. **Set up environment variables**
   Create a `.env` file in the `youtube/` directory:

   ```env
   SECRET_KEY=your-secret-key-here
   IMAGEKIT_PUBLIC_KEY=your-imagekit-public-key
   IMAGEKIT_PRIVATE_KEY=your-imagekit-private-key
   IMAGEKIT_URL_ENDPOINT=your-imagekit-url-endpoint
   ```

5. **Run database migrations**

   ```bash
   cd youtube
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser account**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📱 Usage

### For Users

1. **Register an account** or log in
2. **Upload videos** with titles and descriptions
3. **Browse and watch** videos from other users
4. **Like/dislike** videos and track views
5. **Manage your profile** and uploaded content

### For Administrators

1. **Access admin panel** to manage users and content
2. **Moderate videos** and user activity
3. **Configure settings** through Django admin

## 🔧 Configuration

### ImageKit.io Setup

1. Sign up for an ImageKit.io account
2. Get your API credentials from the dashboard
3. Add them to your `.env` file:
   ```env
   IMAGEKIT_PUBLIC_KEY=your_public_key
   IMAGEKIT_PRIVATE_KEY=your_private_key
   IMAGEKIT_URL_ENDPOINT=your_url_endpoint
   ```

### Django Settings

Key settings in `youtube/settings.py`:

- `DEBUG=True` for development (set to `False` in production)
- `SECRET_KEY` should be kept secret in production
- Database configuration (SQLite by default)

## 🎯 Key Features Explained

### Video Upload System

- Supports multiple video formats
- Automatic thumbnail generation
- Cloud storage integration via ImageKit
- Video optimization and compression

### User Management

- Django's built-in authentication system
- User profiles with video history
- Secure password handling

### Video Engagement

- View counting system
- Like/dislike functionality
- Video recommendations (can be extended)

## 🚀 Deployment

### Production Considerations

1. Set `DEBUG=False` in settings
2. Use a production database (PostgreSQL recommended)
3. Configure static files serving
4. Set up proper domain and SSL
5. Use environment variables for sensitive data

### Recommended Hosting

- **Heroku**: Easy Django deployment
- **DigitalOcean**: Full server control
- **AWS**: Scalable cloud infrastructure
- **PythonAnywhere**: Simple Python hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Django Documentation and Community
- ImageKit.io for image/video processing services
- Bootstrap for responsive UI components
- All contributors and users of this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/hamzamissaoui/django-youtube-clone/issues) page
2. Create a new issue with detailed information
3. Join the community discussions

---

**Built with ❤️ using Django 6.0**
