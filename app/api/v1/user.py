from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["authentication"])


@router.post("/createuser")
async def create_user():
    return {"message": "create_user endpoint"}


@router.get("/userlist")
async def user_list():
    return {"message": "user_list endpoint"}


@router.get("/getone/{identifiant}")
async def getone(identifiant: str):
    return {"message": "get_one endpoint"}


@router.post("/reset-password/{identifiant}")
async def reset_one_password(identifiant: str):
    return {"message": "reset_one_password"}


@router.patch("/change-role/{identifiant}")
async def change_role(identifiant: str):
    return {"message": "change role endpoint"}


@router.patch("/toggle-active/{identifiant}")
async def toggle_active(identifiant: str):
    return {"message": "toggle_active endpoint"}


@router.patch("/change-password")
async def change_password():
    return {"message": "change password end point"}


@router.delete("/users/{identifiant}")
async def delete_user(identifiant: str):
    return {"message": "supression de l'utilisateur"}
