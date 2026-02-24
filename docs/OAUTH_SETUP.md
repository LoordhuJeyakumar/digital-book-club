# 🌍 Google OAuth Configuration Guide

To enable "Social Login" in your Digital Book Club API, you need to tell Google who you are. Google will give you two special keys: a **Client ID** and a **Client Secret**.

Here is the step-by-step process to get them for free!

---

## 🛠️ Step 1: Create a Project in Google Cloud
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Log in with your standard Google account.
3. In the top-left navigation bar, click the project dropdown (it might say "Select a project").
4. Click **New Project** in the top right of the modal window.
5. Name it something like `Book-Club-API` and click **Create**.
6. Wait a few seconds, then make sure your new project is selected in the top navigation bar.

---

## 🛡️ Step 2: Configure the OAuth Consent Screen
*This is the screen users see when Google asks "Do you want to share your data with Book Club API?"*

1. In the left sidebar, go to **APIs & Services** > **OAuth consent screen**.
2. Select **External** (this allows anyone with a Google account to log in) and click **Create**.
3. Fill out the required App information:
    - **App Name**: Digital Book Club
    - **User Support Email**: Select your email.
    - **Developer Contact Information**: Enter your email.
4. Click **Save and Continue** at the bottom.
5. On the **Scopes** screen, just click **Save and Continue** (we only need the default email and profile scopes).
6. On the **Test Users** screen, click **Save and Continue**.
7. Click **Back to Dashboard**.

---

## 🔑 Step 3: Generate your Credentials
1. In the left sidebar, click **Credentials**.
2. Click **+ CREATE CREDENTIALS** at the top and select **OAuth client ID**.
3. **Application Type**: Select **Web application**.
4. **Name**: "Book Club Local testing"
5. **Authorized JavaScript origins**: 
    - Click `+ ADD URI`
    - Enter: `http://127.0.0.1:8000` *(Change the port if you run Uvicorn on a different one, e.g., 3341)*
6. **Authorized redirect URIs** (CRITICAL! This must match the code in `app/routers/auth.py`):
    - Click `+ ADD URI`
    - Enter: `http://127.0.0.1:8000/auth/google/callback` *(Update the port to match your local server if needed)*
7. Click **Create**.

---

## ⚙️ Step 4: Update your `.env` File!
A modal will pop up displaying your keys. 
1. Copy the **Client ID**.
2. Copy the **Client Secret**.
3. Open your project's `.env` file and paste them in:

```env
GOOGLE_CLIENT_ID="your-long-client-id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="your-secret-code"
```

> **⚠️ Security Warning for Students:** Never commit your `.env` file to GitHub! The `.gitignore` file ensures your secret keys stay safe on your computer.

Restart your FastAPI server, and your "Login with Google" button will now work perfectly! 🎉
