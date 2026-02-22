from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

EMAIL = "24f2006813@ds.study.iitm.ac.in"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # The grader looks for this exact string in the body
    return f"<html><body>{EMAIL}</body></html>"

if __name__ == "__main__":
    # host="0.0.0.0" is REQUIRED for localtunnel to connect
    uvicorn.run(app, host="0.0.0.0", port=5501)
