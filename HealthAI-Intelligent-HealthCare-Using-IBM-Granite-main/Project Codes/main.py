from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# -----------------------------
# Home Page
# -----------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# -----------------------------
# Disease Prediction
# -----------------------------
@app.post("/predict", response_class=JSONResponse)
async def predict(user_input: str = Form(...)):
    symptoms = user_input.lower()

    if "fever" in symptoms:
        result = "👉 Possible Flu\n👉 Stay hydrated\n👉 Take rest"
    elif "headache" in symptoms:
        result = "👉 Possible Migraine\n👉 Reduce screen time\n👉 Drink water"
    elif "cough" in symptoms:
        result = "👉 Possible Cold\n👉 Drink warm fluids\n👉 Take proper rest"
    else:
        result = "👉 Could not determine disease\n👉 Please consult a doctor"

    return {"result": result}


# -----------------------------
# Home Remedies
# -----------------------------
@app.post("/remedies", response_class=JSONResponse)
async def remedies(user_input: str = Form(...)):
    text = user_input.lower()

    if "cold" in text or "cough" in text:
        result = """
👉 Drink ginger tea
👉 Honey with warm water
👉 Steam inhalation
👉 Rest properly
"""
    elif "headache" in text:
        result = """
👉 Drink water
👉 Rest in dark room
👉 Apply cold compress
"""
    else:
        result = """
👉 Maintain healthy diet
👉 Drink plenty of water
👉 Get enough sleep
"""

    return {"result": result}


# -----------------------------
# Health Tips
# -----------------------------
@app.get("/tips", response_class=JSONResponse)
async def tips():

    tips_list = """
👉 Drink 8 glasses of water daily
👉 Exercise at least 30 minutes
👉 Eat fruits and vegetables
👉 Maintain proper sleep
👉 Reduce sugar intake
👉 Manage stress
👉 Avoid smoking
👉 Maintain hygiene
👉 Take regular health checkups
👉 Limit junk food
👉 Practice meditation
👉 Stay physically active
"""

    return {"result": tips_list}


# -----------------------------
# Chat Assistant
# -----------------------------
@app.post("/chat", response_class=JSONResponse)
async def chat(user_input: str = Form(...)):
    question = user_input.lower()

    if "fever" in question:
        response = "It may be due to infection. Stay hydrated and rest."
    elif "exercise" in question:
        response = "Daily exercise improves heart health and stamina."
    elif "diet" in question:
        response = "A balanced diet includes proteins, vitamins and minerals."
    else:
        response = "For serious health concerns please consult a doctor."

    return {"result": response}


# -----------------------------
# Treatment Plan
# -----------------------------
@app.post("/treatment", response_class=JSONResponse)
async def treatment(user_input: str = Form(...)):

    plan = """
Medications:
• Take prescribed medicines
• Use pain relief tablets if necessary
• Follow dosage instructions

Lifestyle Changes:
• Drink plenty of water
• Maintain healthy diet
• Exercise regularly

Follow-up Care:
• Monitor symptoms
• Visit doctor if condition worsens
• Take proper rest
"""

    return {"plan": plan}


# -----------------------------
# AI Health Insights (Demo)
# -----------------------------
@app.post("/ai-insights", response_class=JSONResponse)
async def ai_insights(
        heart_rate: str = Form(...),
        blood_pressure: str = Form(...),
        glucose: str = Form(...)
):

    result = f"""
Health Data Summary

Heart Rate: {heart_rate}
Blood Pressure: {blood_pressure}
Blood Glucose: {glucose}

Insights:
👉 Your health data shows normal variations.
👉 Maintain balanced diet and exercise.

Recommendations:
👉 Drink enough water
👉 Maintain regular physical activity
👉 Monitor health weekly
"""

    return {"result": result}