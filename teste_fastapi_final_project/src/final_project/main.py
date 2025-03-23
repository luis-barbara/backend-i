from final_project.models import Task
from fastapi import FastAPI


app = FastAPI(
    title="TODO: AI IMAGE CREATOR"
)


app.get("/task",response_model=Task)
def get_task():
    pass

app.post("/task")
def create_task():
    pass

app.put("/task")
def edit_task():
    pass

app.patch("/task")
def close_task():
    pass

app.delete("/task")
def delete_task():
    pass
