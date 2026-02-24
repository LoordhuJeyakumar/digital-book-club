# 🚀 Free Deployment Guide: Render.com

It's time to show your Digital Book Club API to the world! We will deploy our backend using **Render**, a fantastic platform that offers free hosting for web services and databases.

> **Note:** Free tiers have limitations. The server will "go to sleep" if inactive for 15 minutes, meaning the first request after a break will take about 50 seconds to respond. This is perfect for portfolios and learning!

---

## 📦 Step 1: Preparation (Requirements)
Before we deploy, Render needs to know exactly what libraries our app uses.

1. Ensure your virtual environment is active.
2. In your terminal, run this command to generate a `requirements.txt` file automatically:
```bash
pip freeze > requirements.txt
```
3. Ensure your project is pushed to a **GitHub repository**.

---

## 🗄️ Step 2: Deploy the Database

**Teacher's Note:** Locally, we used **MySQL**. However, Render doesn't offer a free managed MySQL service. So, we are going to deploy a **PostgreSQL** database instead. 

Wait, won't that break our code? **NO!** 
Because we used **SQLAlchemy** (an Object Relational Mapper), our Python code doesn't care what dialect of SQL we use. SQLAlchemy translates our Python models into the correct SQL language automatically. This is the magic of ORMs!

1. Create an account at [Render.com](https://render.com/).
2. Click **New +** and select **PostgreSQL**.
3. Name it `book-club-db` (leave other settings as defaults).
4. Click **Create Database**.
5. Once created, copy the **Internal Database URL** (we'll need this soon). It looks like this: `postgresql://user:pass@host/dbname`

*(Note: In your `requirements.txt`, you will need to add `psycopg2-binary` to allow SQLAlchemy to talk to PostgreSQL).*


---

## 🕸️ Step 3: Deploy the FastAPI Web Service
1. Click **New +** and select **Web Service**.
2. Connect your GitHub account and select your `digital-book-club` repository.
3. Fill out the configuration:
    - **Name**: `my-digital-book-club-api`
    - **Language**: `Python 3`
    - **Branch**: `master`
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 10000` *(Render uses port 10000)*
    - **Instance Type**: Free

### 🔑 Step 4: Environment Variables
Render won't know your secrets unless you tell it. Scroll down to **Environment Variables** and add:
- `SECRET_KEY`: (Create a new long random string)
- `ALGORITHM`: `HS256`
- `ACCESS_TOKEN_EXPIRE_MINUTES`: `30`
- `DATABASE_URL`: (Paste the **Internal Database URL** you copied in Step 2!)
- `GOOGLE_CLIENT_ID`: (Your OAuth ID)
- `GOOGLE_CLIENT_SECRET`: (Your OAuth Secret)

*(Note: Since you change your URL, you will need to update your Google OAuth settings in the Google Cloud Console to add your new `https://my-app.onrender.com/auth/google/callback` URL)*.

---

## 🚀 Step 5: Launch!
1. Click **Create Web Service**.
2. Render will automatically pull your code from GitHub, install the requirements, and start Uvicorn.
3. Watch the logs. Once you see `Application startup complete.`, your API is live!

Click the link provided by Render (e.g., `https://my-digital-book-club-api.onrender.com/docs`) to view your live, public Swagger UI! 🎉
