from fastapi import APIRouter

router = APIRouter(prefix="/profil", tags=["authentication"])


@router.get("/getAll")
async def getAllProfils():
    return {"message": "obtention de tous les profils"}
    

@router.get("/getone/{identifiantRH}")
async def getUserProfil(identifiantRH : str):
    return {"message": "obtenir le profil d'un identifiantRH"}

@router.get("/getonebyid/{id}")
async def getUserProfilByid(id: str):
    return {"message":"avoir un progil grace à son id"}

@router.post("/create")
async def createUserProfil():
    return{"message":"création du profil"}

@router.patch("/update/{identifiantRH}")
async def updateUserProfil(identifiantRH :str):
    return{"message":"mise a jour d'un profil d'un identifiantRH"}


@router.get("/without-account")
async def getProfilsWithoutAccount():
    return {"message":"obtenir les profils sans comptes user"}

