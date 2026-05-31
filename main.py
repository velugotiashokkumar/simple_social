import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="app.app:app", host="127.0.0.7", port=8080, reload=True)