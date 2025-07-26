# Resume Website – Django + Docker Swarm + Traefik

This is the source code and infrastructure configuration for my personal resume website, built with Django and deployed using Docker Swarm and Traefik. The Django application is containerized and published to Docker Hub, then pulled by the server during deployment.

**Currently in development – not yet live.**

---

## Tech Stack

- **Backend**: Django (Python), containerized
- **Frontend**: Django templates (HTML/CSS)
- **Database**: PostgreSQL 17
- **Static files**: Served via NGINX (Alpine)
- **Reverse proxy & HTTPS**: Traefik v3 with Let's Encrypt
- **Orchestration**: Docker Swarm (with rollback support)
- **Image hosting**: [Docker Hub](https://hub.docker.com/)

Planned domains:
- Main site: `resume.steyaert.xyz`
- Blog: `blog.resume.steyaert.xyz`
- CDN: `cdn.resume.steyaert.xyz`

---

## Deployment

The app runs as a Docker Swarm stack using prebuilt images pulled from Docker Hub.

### Key services:

- `traefik`: TLS termination & routing
- `website`: Pulls latest Django image from Docker Hub
- `nginx_static`: Serves collected static assets
- `db`: PostgreSQL with persistent storage

### Rollback Support

Docker Swarm provides built-in rollback support. If an update fails:

```bash
docker service rollback resume_website
```

---

## Docker Image

The Django app is built and pushed to Docker Hub (e.g. `steyaertc23/resume:latest`).  
The production server pulls this image as defined in `docker-compose.yml`.

---

## Static Files

Before building the image, collect static files:

```bash
python manage.py collectstatic
```

These files are mounted into `nginx_static` and served at `cdn.basedomain`.

---

## Local Development

For development outside Docker:

```bash
# Sync and install dependencies using uv
uv sync

# Run the Django development server
python manage.py runserver
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

Stephen Steyaert
([Live site coming soon](#))
