from django.shortcuts import render
from .models import ContactMessage 

def home(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        success = True  

    
    user_data = {
        'name': 'Jayasree',
        'first_name': 'Jaya',
        'full_name': 'Jayasree Amudala',
        'email': 'jayasree@example.com',
        'location': 'Hyderabad, India',
        'linkedin': 'https://linkedin.com/in/jayasree-amudala-9411952bb',
        'github': 'https://github.com/jayasree-007',
        'instagram': 'https://instagram.com/yourprofile',
        'resume_url': '/static/resume/Report.pdf',
        'about': 'I am a passionate B.Tech student specializing in Data Science. My interests include data visualization, machine learning, and building cool Python projects.'
    }

    skills = [
        {'name': 'Python', 'icon': 'devicon-python-plain'},
        {'name': 'Machine Learning', 'icon': 'fas fa-brain'},
        {'name': 'SQL', 'icon': 'fas fa-database'},
        {'name': 'Power BI', 'icon': 'fas fa-chart-bar'},
        {'name': 'HTML', 'icon': 'devicon-html5-plain'},
        {'name': 'CSS', 'icon': 'devicon-css3-plain'},
        {'name': 'JavaScript', 'icon': 'devicon-javascript-plain'},
        {'name': 'GitHub', 'icon': 'devicon-github-original'},
    ]

    education = [
        {'degree': 'B.Tech in Data Science', 'institution': 'NNRGI', 'year': '2022 - Present'},
        {'degree': 'MPC','institution': 'SR Junior College', 'year':'2020 - 2022'}
    ]

    projects = [
    {
        'title': 'Weather App',
        'description': 'A weather forecasting web app using JavaScript and Chart.js',
        'demo_url': 'https://github.com/jayasree-007/Weather-App.git',
        'code_url': 'https://github.com/jayasree-007/Weather-App.git',
        'image_url': 'static/images/hyderabad.png' 
    },
    {
        'title': 'Eye Guardian',
        'description': 'A web-based eye health monitoring system that uses computer vision and reinforcement learning to help users maintain healthy screen viewing habits.',
        'demo_url': 'https://github.com/jayasree-007/eye-guardian.git',
        'code_url': 'https://github.com/jayasree-007/eye-guardian.git',
        'image_url': 'static/images/homepage.png' 
    }
]



    context = {
        'user': user_data,
        'skills': skills,
        'education': education,
        'projects': projects,
        'success': success
    }

    return render(request, 'home/index.html', context)
