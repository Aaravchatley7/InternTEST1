import os

# ── OpenRouter (REQUIRED for LLM fallback, FREE tier available) ───────────────
# Sign up free at https://openrouter.ai → Dashboard → API Keys
# Free models: mistral-7b-instruct:free, llama-3.2-3b-instruct:free
# NOTE: Regex extraction works without this key — it's only used when OCR is unclear.
OPENROUTER_API_KEY = os.getenv(
    'OPENROUTER_API_KEY',
    ''
)

# ── Gmail SMTP ────────────────────────────────────────────────────────────────
# Use a Gmail App Password (not your main password):
# Gmail → Security → 2-Step Verification → App Passwords
SMTP_EMAIL    = os.getenv('SMTP_EMAIL',    '')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')

# ── Flask ─────────────────────────────────────────────────────────────────────
SECRET_KEY = os.getenv('SECRET_KEY', '')
