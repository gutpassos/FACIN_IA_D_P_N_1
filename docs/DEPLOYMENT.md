# Deployment - FACIN_IA_D_P_N_1

Guia de deployment e publicação do projeto.

---

## 📦 Ambientes de Deployment

### 1. **Development**
- Local: `localhost:8501`
- Automático: push para branch `develop`
- Validação: Tipo "warning"

### 2. **Staging**
- URL: `staging-facin-ia.herokuapp.com` (exemplo)
- Automático: PR aprovada para `main`
- Validação: Tipo "error", obrigatória

### 3. **Production**
- URL: `facin-ia.herokuapp.com` (exemplo)
- Manual: Tag de versão (v1.0.0)
- Validação: Todas as checks devem passar

---

## 🚀 Pipeline de Deployment

```
Code → GitHub Push
   ↓
GitHub Actions Triggered
   ↓
1. Validation (Spec + Code Quality)
   ├─ Spec validation (MANDATORY)
   ├─ Code formatting
   ├─ Type checking
   └─ Tests
   ↓
2. Build & Artifacts
   ├─ Generate documentation
   └─ Create build artifacts
   ↓
3. Deploy Decision
   ├─ develop → Auto deploy to Staging
   ├─ main → Manual approval for Prod
   └─ tag → Auto deploy to Production
```

---

## 🔐 Secrets & Configurations

### GitHub Secrets (Required)

```yaml
OPENAI_API_KEY:           # OpenAI API key
GROQ_API_KEY:             # Groq API key
AGENTICOPS_API_KEY:       # AgenticOps key (optional)
HEROKU_API_KEY:           # Heroku deployment key
HEROKU_APP_NAME:          # Heroku app name
DATABASE_URL:             # Production database URL
```

### Environment Variables

```yaml
# .env.production
DEBUG=false
LOG_LEVEL=INFO
ENVIRONMENT=production
AGENTICOPS_ENABLED=true
```

---

## 🐳 Docker Deployment

### Dockerfile Example

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0"]
```

### Build & Run

```bash
# Build
docker build -t facin-ia:1.0.0 .

# Run locally
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=sk-... \
  -e GROQ_API_KEY=gsk-... \
  facin-ia:1.0.0

# Push to registry
docker push your-registry/facin-ia:1.0.0
```

---

## ☁️ Deployment Platforms

### Heroku

```bash
# Login
heroku login

# Create app
heroku create facin-ia

# Set environment variables
heroku config:set OPENAI_API_KEY=sk-...
heroku config:set GROQ_API_KEY=gsk-...

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### AWS/EC2

```bash
# SSH into instance
ssh -i key.pem ec2-user@instance-ip

# Clone repository
git clone https://github.com/gutpassos/FACIN_IA.git
cd FACIN_IA

# Setup environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure supervisor or systemd
sudo cp facin-ia.service /etc/systemd/system/
sudo systemctl enable facin-ia
sudo systemctl start facin-ia

# Nginx reverse proxy
sudo apt install nginx
sudo cp nginx.conf /etc/nginx/sites-available/facin-ia
```

### GCP/App Engine

```bash
# Initialize App Engine
gcloud app create

# Deploy
gcloud app deploy app.yaml

# View logs
gcloud app logs read
```

---

## 🔄 CI/CD Configuration

### GitHub Actions Workflow

O arquivo `.github/workflows/validate.yml` já está configurado com:

1. **Validation Stage**
   - Especificação JSON (OBRIGATÓRIO)
   - Code quality checks
   - Type checking
   - Tests with coverage

2. **Build Stage**
   - Generate documentation
   - Create artifacts
   - Build Docker image

3. **Deploy Stage**
   - Auto-deploy to staging on PR merge
   - Manual approval for production
   - Automated rollback on failure

---

## 📊 Monitoring Post-Deployment

### AgenticOps Dashboard

```bash
# URL: https://agenticops.io/dashboard
# Project: FACIN_IA
# Monitora:
# - LLM calls
# - Agent performance
# - Error rates
# - Latency metrics
```

### Application Logs

```bash
# Local logs
tail -f logs/app_YYYYMMDD.log
tail -f logs/error_YYYYMMDD.log
tail -f logs/agenticops.log

# Heroku logs
heroku logs --tail

# CloudWatch (AWS)
aws logs tail /aws/lambda/facin-ia --follow
```

### Health Checks

```bash
# Basic health endpoint
curl http://localhost:8501

# Health check path (if implemented)
curl http://localhost:8501/health
```

---

## 🔧 Database Migrations

### SQLite to PostgreSQL

```bash
# Export SQLite
sqlite3 folha_pagamento.db ".dump" > backup.sql

# Create PostgreSQL database
createdb facin_ia_prod

# Import (may need adjustments)
psql facin_ia_prod < backup.sql

# Update config
export DATABASE_URL=postgresql://user:pass@host:5432/facin_ia_prod
```

---

## 📋 Pre-Deployment Checklist

- [ ] All tests passing (70%+ coverage)
- [ ] Spec validation successful
- [ ] Code quality checks passing
- [ ] No security vulnerabilities detected
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped (if releasing)
- [ ] Environment variables configured
- [ ] Database backups created
- [ ] Monitoring configured
- [ ] Rollback plan in place

---

## 🚨 Rollback Procedures

### Heroku Rollback

```bash
# View releases
heroku releases

# Rollback to previous version
heroku rollback v42

# Deploy specific commit
git push heroku <commit-sha>:main
```

### Docker Rollback

```bash
# Use previous image tag
docker run -d \
  --name facin-ia \
  -p 8501:8501 \
  your-registry/facin-ia:1.0.0-previous
```

### Database Rollback

```bash
# Restore from backup
sqlite3 folha_pagamento.db < backup.sql

# PostgreSQL
psql facin_ia_prod < backup.sql
```

---

## 📞 Support & Troubleshooting

### Common Issues

**Port already in use**
```bash
lsof -i :8501
kill -9 <PID>
```

**Module not found**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

**Database connection error**
```bash
# Check connection string
echo $DATABASE_URL

# Test connection
python -c "import sqlite3; sqlite3.connect('folha_pagamento.db')"
```

### Escalation

1. Check logs: `logs/error_YYYYMMDD.log`
2. Review recent changes: `git log --oneline`
3. Check status page: GitHub Status
4. Contact: gut.passos@gmail.com

---

## 📚 Related Documentation

- [README.md](README.md) - Project overview
- [QUICKSTART.md](QUICKSTART.md) - Getting started
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development guide
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design

---

**Versão**: 1.0.0  
**Data**: 27/02/2026  
**Status**: Production Ready (Maturity Level 1)
