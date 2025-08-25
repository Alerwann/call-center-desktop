from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/login")
async def login():
    return{"message":"login endpoint"}

@router.post("/refresh_token")
async def refresh_token():
    return{"message":"refresh_token end point"}


@router.post("/logout")
async def logout():
    return {"message": "logout end point"}


@router.post("/logout_all")
async def logout_all():
    return {"message": "logout_all end point"}


@router.get("/get_session")
async def get_session():
    return {"message": "get_session end point"}

@router.post("/revoke_session")
async def revoke_session():
    return{"message": "revoke_session end point"}
