# Rizz Bot 😎

Paste a text you got from your crush, pick a vibe, and Rizz Bot suggests 3 replies.

## 1. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

- Mac/Linux: `source venv/bin/activate`
- Windows: `venv\Scripts\activate`

## 2. Install requirements

```bash
pip install -r requirements.txt
```

## 3. Create the .env file

Copy `.env.example` to a new file named `.env`, then put your real key in it:

```
OPENAI_API_KEY=sk-...
```

Get a key at https://platform.openai.com/api-keys. Never share or commit your `.env` file.

## 4. Run the app

```bash
streamlit run app.py
```

It opens in your browser at http://localhost:8501.
