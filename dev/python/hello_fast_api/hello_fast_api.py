# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

app = FastAPI(
    title="Mon API FastAPI",
    description="Exemple complet",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "hello sur FastAPI!"}

# 404 handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    # On ignore simplement le favicon (ou on peut le renvoyer 204)
    if request.url.path == "/favicon.ico":
        return Response(status_code=204)   # No Content
    return JSONResponse(status_code=404, content={"detail": "Not Found"})