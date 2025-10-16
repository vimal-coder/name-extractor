import io
import pytesseract
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Add the following line if Tesseract is not in your PATH.
# You may need to change the path depending on where you install it.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(image_bytes):
    """
    This function will handle the core OCR processing of images.
    """
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    # Exclude lines containing "follow" (case-insensitive)
    names = []
    for line in text.split('\n'):
        clean_line = line.strip()
        if clean_line and len(clean_line.split()) <= 3 and "follow" not in clean_line.lower() and len(clean_line) >= 4:
            names.append(clean_line)
    return names

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/", response_class=HTMLResponse)
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    names = ocr_core(contents)
    return templates.TemplateResponse("index.html", {"request": request, "names": names})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
