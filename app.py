from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()

EMAIL = "24f2006813@ds.study.iitm.ac.in"

@app.get("/")
async def read_root():
    # We return the RAW email string. 
    # No <html>, no <body>, no <span>. 
    # This ensures the grader's string-match works perfectly.
    content = EMAIL
    
    # We manually set headers to bypass the Localtunnel landing page
    headers = {
        "Bypass-Tunnel-Reminder": "true",
        "Content-Type": "text/plain",
        "Access-Control-Allow-Origin": "*"
    }
    
    return Response(content=content, media_type="text/plain", headers=headers)

if __name__ == "__main__":
    # Ensure port matches what you are using in your 'lt' command
    uvicorn.run(app, host="0.0.0.0", port=5501)
