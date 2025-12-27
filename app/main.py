from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
import shutil
import os
from pathlib import Path

from app.pipeline import run_pipeline

app = FastAPI(title="AI Sales Campaign CRM")

# ---------- Paths ----------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_INPUT_DIR = BASE_DIR / "data" / "input"
DATA_OUTPUT_DIR = BASE_DIR / "data" / "output"
REPORTS_DIR = BASE_DIR / "reports"

DATA_INPUT_DIR.mkdir(parents=True, exist_ok=True)
DATA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


# ---------- UI ----------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Sales CRM</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            button { padding: 8px 16px; }
        </style>
    </head>
    <body>
        <h2>AI-Enhanced Sales Campaign CRM</h2>

        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv" required />
            <br><br>
            <button type="submit">Run Campaign</button>
        </form>

        <p>
            📬 MailHog UI:
            <a href="http://localhost:8025" target="_blank">
                http://localhost:8025
            </a>
        </p>
    </body>
    </html>
    """


# ---------- Upload + Run Pipeline ----------
@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    try:
        input_path = DATA_INPUT_DIR / file.filename
        output_path = DATA_OUTPUT_DIR / f"processed_{file.filename}"

        # Save uploaded CSV
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run pipeline
        run_pipeline(
            input_csv_path=str(input_path),
            output_csv_path=str(output_path)
        )

        return JSONResponse({
            "status": "success",
            "message": "Campaign completed successfully",
            "output_csv": f"data/output/{output_path.name}",
            "report": "reports/campaign_summary.md",
            "mailhog_ui": "http://localhost:8025"
        })

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "detail": str(e)}
        )


# ---------- Health Check ----------
@app.get("/health")
def health():
    return {"status": "ok"}
