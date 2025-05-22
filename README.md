# 🧠 User Onboarding Automation with Django, React, n8n & Google Sheets

## 📝 Project Documentation

### 1. The Business Problem I'm Solving

When businesses collect onboarding or inquiry data from users through forms, they often end up doing a lot of manual work — like copying details into spreadsheets or CRMs. This not only takes time but also increases the chances of human errors and doesn't scale well.

So, I decided to automate this entire process. The goal is simple:  
**User fills a form → Data gets validated → Automatically sent to Google Sheets using n8n.**  

No manual entry. Everything works like a pipeline.

---

### 2. Architecture & Workflow (How I Built It)

This project is built using the following:

- **Frontend:** React (Vite)  
- **Backend:** Django REST Framework  
- **Automation:** n8n (workflow automation tool)  
- **Storage:** Google Sheets (used like a lightweight database)

#### 🔄 Workflow:

1. The user lands on a React-based form and fills in their details.
2. When the form is submitted, it sends a `POST` request to my Django backend.
3. The Django backend validates the data using a custom serializer.
4. Once validated, it sends this data to an n8n webhook.
5. n8n receives the data and pushes it to a Google Sheet — neatly sorted in columns.

```
User → React Form → Django API → n8n Webhook → Google Sheets
```

---

### 3. (Optional) AI Agent Details

Right now, I'm not using an actual AI agent like OpenAI or LangChain in this project — but I built it in a way that it can be extended to support one.

For example, in the n8n workflow, I've already added some logic like this:

```n8n
{{$if($json.body.Budget == "1000+", "FALSE", "TRUE")}}
```

This line checks the user's budget and marks a field as `Rejected: TRUE` or `FALSE`. It kind of acts like a mini decision engine.

Later, I could plug in OpenAI into the n8n flow and make it:

* Auto-categorize users based on message tone
* Suggest services
* Auto-reply with personalized emails

So even though I'm not using an AI agent yet, the project is open for that kind of upgrade.

---

### 4. Setup & Configuration (How to Run Everything)

#### ✅ Backend (Django)

```bash
git clone <your-repo-url>
cd <project-folder>
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

* The API endpoint is available at: `http://127.0.0.1:8000/`
* I'm using `InputSerializer` to validate the data before sending it to n8n
* Also included logic to convert keys to Title Case to match n8n's Google Sheet field expectations

#### ✅ Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

* This runs the form locally at `http://localhost:5173`
* The form includes:
  * First Name
  * Last Name
  * Email
  * Budget (dropdown)
  * Message
* On submission, it sends the data to Django

#### ✅ n8n Workflow Setup

1. Create an account at [https://n8n.cloud](https://n8n.cloud)
2. Create a new workflow:
   * Add a **Webhook node** (set to `POST` method)
   * Add a **Google Sheets node** connected to the webhook
3. Inside the Google Sheets node:
   * Map fields using expressions like `{{ $json.body["First Name"] }}` and `{{ $json.body["Budget"] }}`
   * Add logic like this in custom columns if needed:

```n8n
{{$if($json.body.Budget == "1000+", "FALSE", "TRUE")}}
```

4. Get the webhook URL and paste it into the Django backend (`views.py`)

---

### 🛠️ Other Notes

* Enabled CORS in Django using `django-cors-headers` for development
* If you're planning to deploy, replace the webhook with an environment variable and configure security accordingly
* You can extend this project to store the data in PostgreSQL or MongoDB instead of Google Sheets
* Add email notifications or AI agents in n8n as next steps!

---
