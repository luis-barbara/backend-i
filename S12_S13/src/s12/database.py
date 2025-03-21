
from pytest import Session
from s12.models import Task

def get_session()->Session:


    
def create(task: Task):
    assert task
    with get_session() as session:
