# GenAIWebApplication

![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Mobusshar/GenAIWebApplication)
![GitHub last commit](https://img.shields.io/github/last-commit/Mobusshar/GenAIWebApplication)
![GitHub top language](https://img.shields.io/github/languages/top/Mobusshar/GenAIWebApplication)
![GitHub language count](https://img.shields.io/github/languages/count/Mobusshar/GenAIWebApplication)
![GitHub License](https://img.shields.io/github/license/Mobusshar/GenAIWebApplication)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Mobusshar/GenAIWebApplication)
![GitHub repo size](https://img.shields.io/github/repo-size/Mobusshar/GenAIWebApplication)
![GitHub forks](https://img.shields.io/github/forks/Mobusshar/GenAIWebApplication)
![GitHub Repo stars](https://img.shields.io/github/stars/Mobusshar/GenAIWebApplication)

GenAIWebApplication is a full-stack web application designed to support collaborative sketching and AI-assisted design learning activities. The system includes:

- **Frontend**: Developed using Angular
- **Backend**: Built with Flask and served via Gunicorn
- **Database**: PostgreSQL (optional, not included in this setup)
- **Web Server**: Nginx

---

## 📁 Project Structure

```
GenAIWebApplication/
├── backend/          # Flask backend API
│   ├── app/          # Application package
│   ├── venv/         # Python virtual environment
│   └── ...
├── frontend/         # Angular frontend
│   ├── src/
│   └── dist/gen-aiui/
└── ...
```

---

## 🚀 Deployment Overview

### ✅ Prerequisites

- Ubuntu 20.04+ (or compatible Linux system)
- Node.js (v18+) and npm
- Angular CLI
- Git
- Python 3.8+ and virtualenv
- Gunicorn
- Nginx

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
cd /home/ubuntu/projects
git clone git@github.com:Mobusshar/GenAIWebApplication.git
```

### 2. Frontend Setup (Angular)

```bash
cd GenAIWebApplication/frontend
npm install

# Set backend API URL in environment.prod.ts
nano src/environments/environment.prod.ts
# Replace with your backend URL:
export const environment = {
  production: true,
  apiUrl: 'http://your-server-ip-or-domain/api'
};

# Build the project
ng build --configuration=production

# Copy the build to the Nginx HTML directory:
sudo rm -rf /var/www/html/gen-aiui
sudo cp -r dist/gen-aiui /var/www/html/gen-aiui
```

### 3. Backend Setup (Flask + Gunicorn)

```bash
cd GenAIWebApplication/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create systemd unit files:

`/etc/systemd/system/genai.socket`
```ini
[Unit]
Description=genai socket

[Socket]
ListenStream=/run/genai.sock
SocketMode=0666

[Install]
WantedBy=sockets.target
```

`/etc/systemd/system/genai_backend.service`
```ini
[Unit]
Description=Gunicorn instance to serve Flask backend
Requires=genai.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/projects/GenAIWebApplication/backend
ExecStart=/home/ubuntu/projects/GenAIWebApplication/backend/venv/bin/gunicorn -w 4 --bind unix:/run/genai.sock "app:create_app()"

[Install]
WantedBy=multi-user.target
```

Start the services:

```bash
sudo systemctl daemon-reload
sudo systemctl enable genai.socket
sudo systemctl start genai.socket
sudo systemctl enable genai_backend.service
sudo systemctl start genai_backend.service
```

### 4. Nginx Configuration

Create a new Nginx config:

```bash
sudo nano /etc/nginx/sites-available/genaiui
```

Paste:

```nginx
server {
    listen 80;
    server_name your-server-ip-or-domain;

    root /var/www/html/gen-aiui;
    index index.html;

    location / {
        try_files $uri /index.html;
    }

    location /api/ {
        proxy_pass http://unix:/run/genai.sock;
        include proxy_params;
    }
}
```

Enable it:

```bash
sudo ln -s /etc/nginx/sites-available/genaiui /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🔁 Updating Code

When new code is pushed:

```bash
cd /home/ubuntu/projects/GenAIWebApplication
git pull origin main

# Frontend
cd frontend
npm install
ng build --configuration=production
sudo rm -rf /var/www/html/gen-aiui
sudo cp -r dist/gen-aiui /var/www/html/gen-aiui
sudo systemctl restart nginx

# Backend
cd ../backend
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart genai_backend.service
```

---

## 🛠️ Troubleshooting

Check Gunicorn backend logs:

```bash
sudo journalctl -u genai_backend.service --no-pager
```

Check socket status:

```bash
sudo systemctl status genai.socket
```

Check Nginx logs:

```bash
sudo tail -f /var/log/nginx/error.log
```

---

## 👨‍💻 Author

Maintained by Mobusshar.

---

## 📄 License

MIT License (or as applicable)
