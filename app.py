from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

EMAIL = "24f2006813@ds.study.iitm.ac.in"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # We add or use a span to break the pattern 
    # Cloudflare's scraper won't see it as a single email string
    part1, part2 = EMAIL.split("@")
    tricked_email = f'<span>{part1}</span>@<span>{part2}</span>'
    
    # We also add the data-cfemail="false" attribute to hint to Cloudflare to stop
    return f"""
    <html>
        <body>
            <div data-cfemail="false">
                {tricked_email}
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5501)
