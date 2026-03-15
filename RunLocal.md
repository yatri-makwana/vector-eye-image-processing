# EYE - Quick Local Setup

## Prerequisites
- Python 3.12+
- Node.js 18+
- Ollama (optional, for AI features)

## Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set environment variables
echo "EYE_ENVIRONMENT=development" > .env
echo "EYE_DATABASE_URL=sqlite:///./eye.db" >> .env

# Run backend
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload

## Frontend Setup
```bash
cd frontend
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:8001" > .env.local
npm run dev -- -p 3003
```

## AI Setup (Optional)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama
ollama serve

# Pull a model (use small one for testing)
ollama pull gemma2:2b
```

## Access Points
- **Frontend**: http://localhost:3003
- **Backend API**: http://localhost:8001
- **API Docs**: http://localhost:8001/docs
- **AI Chat**: Available in frontend at /eye-ai

## Test AI
```bash
# Test AI is working
curl -X POST http://localhost:8001/api/v1/ollama/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "model": "gemma2:2b"
  }'
```

## Notes
- Backend uses SQLite by default (no PostgreSQL needed)
- AI features work if Ollama is running
- Storage directories created automatically
- Perfect for development and testing

---
**Created by**: Dhawan Solanki  
**Purpose**: Simple local development setup for EYE
