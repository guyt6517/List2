from fastapi import FastAPI

# Define the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    o=open('E', 'r')
    x=o.read()
    return x
