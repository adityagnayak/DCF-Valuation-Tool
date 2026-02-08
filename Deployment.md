# Deployment Guide

## 🚀 Deploy to Streamlit Cloud (Free Hosting)

### Step 1: Prepare Your Repository

1. Create a new repository on GitHub
2. Upload these files to your repository:
   ```
   dcf_valuation_tool.py
   requirements.txt
   README.md
   QUICKSTART.md
   .gitignore
   dcf_template.xlsx (optional)
   ```

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set these parameters:
   - **Branch**: main (or master)
   - **Main file path**: dcf_valuation_tool.py
   - **Python version**: 3.9 or higher (recommended)
6. Click "Deploy!"

Your app will be live in a few minutes at:
`https://[your-app-name].streamlit.app`

### Step 3: Share Your App

- Copy the URL and share with colleagues
- Add the URL to your README.md
- Pin the repository on your GitHub profile

---

## 📝 GitHub Repository Setup

### Recommended Repository Structure

```
dcf-valuation-tool/
│
├── dcf_valuation_tool.py      # Main application
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
├── QUICKSTART.md              # Quick start guide
├── DEPLOYMENT.md              # This file
├── .gitignore                 # Git ignore rules
├── setup.sh                   # Setup script
├── test_dcf.py               # Test suite
├── dcf_template.xlsx         # Excel template
│
└── .streamlit/
    └── config.toml           # Streamlit config
```

### Setting Up Your Repository

```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit: DCF Valuation Tool"

# Connect to GitHub
git remote add origin https://github.com/yourusername/dcf-valuation-tool.git
git branch -M main
git push -u origin main
```

### Recommended GitHub Settings

1. **Add a description**: "Interactive DCF Business Valuation Tool with NPV/IRR calculations"
2. **Add topics**: `dcf`, `valuation`, `finance`, `streamlit`, `python`, `investment-analysis`
3. **Enable Issues**: For bug reports and feature requests
4. **Add a LICENSE**: MIT License recommended
5. **Create a .gitignore**: Already included in this project

---

## 🔧 Environment Variables (Optional)

If you need to add API keys or secrets:

### Local Development
Create a `.streamlit/secrets.toml` file:
```toml
# .streamlit/secrets.toml (DO NOT commit this file)
api_key = "your-secret-key"
database_url = "your-database-url"
```

### Streamlit Cloud
1. Go to your app settings
2. Click "Secrets"
3. Add your secrets in TOML format
4. Click "Save"

Access in your code:
```python
import streamlit as st
api_key = st.secrets["api_key"]
```

---

## 🔒 Security Best Practices

### Files to Never Commit

Already in .gitignore:
- `.env` files
- Virtual environments (`venv/`, `env/`)
- `__pycache__/`
- IDE files (`.vscode/`, `.idea/`)
- `.streamlit/secrets.toml`

### Sensitive Data

- Never hardcode API keys
- Don't commit real financial data
- Use environment variables for credentials
- Review `.gitignore` before first commit

---

## 📊 Monitoring Your App

### Streamlit Cloud Dashboard

Monitor your app at: [share.streamlit.io](https://share.streamlit.io)

**Available Metrics:**
- App status (online/offline)
- Number of viewers
- Resource usage (CPU, Memory)
- Error logs
- Deployment history

### View Logs

```bash
# From Streamlit Cloud dashboard
App Settings → Logs → View logs
```

### Restart Your App

If your app encounters issues:
1. Go to app dashboard
2. Click "Reboot app"
3. Or push a new commit to trigger redeployment

---

## 🔄 Updating Your Deployed App

### Method 1: GitHub Commit (Recommended)

```bash
# Make changes to your code
git add .
git commit -m "Update: description of changes"
git push
```

Your app will automatically redeploy!

### Method 2: Manual Redeploy

1. Go to Streamlit Cloud dashboard
2. Click your app
3. Click "Reboot app"

---

## ⚙️ Advanced Configuration

### Custom Domain

1. Go to app settings in Streamlit Cloud
2. Click "Custom domain"
3. Follow instructions to set up your domain
4. Update DNS records with your provider

### Resource Limits

**Streamlit Cloud Free Tier:**
- 1 GB RAM per app
- Shared CPU resources
- No custom requirements
- Public apps only

**Need More Resources?**
- Upgrade to Streamlit for Teams
- Or deploy to your own server (see below)

---

## 🖥️ Self-Hosting Options

### Deploy to Your Own Server

#### Option 1: Simple Server

```bash
# On your server
git clone https://github.com/yourusername/dcf-valuation-tool.git
cd dcf-valuation-tool
pip install -r requirements.txt
streamlit run dcf_valuation_tool.py --server.port 8501
```

#### Option 2: Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "dcf_valuation_tool.py"]
```

Build and run:
```bash
docker build -t dcf-valuation .
docker run -p 8501:8501 dcf-valuation
```

#### Option 3: Heroku Deployment

1. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

2. Create `Procfile`:
```
web: sh setup.sh && streamlit run dcf_valuation_tool.py
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

---

## 🐛 Troubleshooting Deployment

### Common Issues

**Issue: App won't start**
- Check requirements.txt has all dependencies
- Verify Python version compatibility
- Review error logs in Streamlit Cloud

**Issue: Module not found**
- Ensure all imports are in requirements.txt
- Check spelling of package names
- Verify package versions are compatible

**Issue: App crashes on large files**
- Check memory limits
- Optimize data processing
- Consider upgrading plan

**Issue: Slow performance**
- Use `@st.cache_data` for expensive operations
- Reduce chart complexity
- Optimize calculations

### Getting Help

1. Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
2. Visit Streamlit community: [discuss.streamlit.io](https://discuss.streamlit.io)
3. Review error messages in logs
4. Search GitHub issues
5. Create new issue with error details

---

## ✅ Pre-Deployment Checklist

- [ ] All code tested locally
- [ ] requirements.txt is complete
- [ ] README.md is updated
- [ ] .gitignore includes sensitive files
- [ ] No hardcoded secrets
- [ ] Test with sample data
- [ ] Mobile responsiveness checked
- [ ] Error handling implemented
- [ ] GitHub repository is public (for Streamlit Cloud)
- [ ] App runs without errors locally

---

## 📈 Post-Deployment

### Promote Your App

- Share on LinkedIn
- Tweet about it
- Add to your portfolio
- Write a blog post
- Submit to Streamlit gallery

### Gather Feedback

- Enable GitHub Issues
- Add feedback form in app
- Monitor usage metrics
- Iterate based on user needs

### Maintain Your App

- Keep dependencies updated
- Monitor for security vulnerabilities
- Add new features based on feedback
- Fix bugs promptly
- Update documentation

---

**Ready to deploy? Follow the steps above and your DCF Valuation Tool will be live!**

For questions, open an issue on GitHub or contact the maintainer.
