from fastapi import APIRouter

router = APIRouter(prefix="/task",tags=["task"])

@router.get("/task")
async def all_tasks():
    pass

@router.get("/task_id")
async def get_task():
    pass

@router.post ("/create")
async def create_task():
    pass

@router.put("/update")
async def update_tas():
    pass

@router.delete("/delete")
async def delete_task():
    pass
