from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def home():
    return{
        "message":"Hello FastAPI"
    }


@app.get("/health")
def health_check():
    return{
        "status":"ok"
    }


@app.get("/skills")
def skills():
    return{
        "skills":[
            "Python",
            "FastAPI",
            "React",
            "Node.js",
            "MongoDB"
        ]
    }