import uvicorn

if __name__ == "__main__":
     uvicorn.run(
         host="0.0.0.0",
         port=8000,
         reload=True,
         #debug=True,
         app="main:app"
     )

