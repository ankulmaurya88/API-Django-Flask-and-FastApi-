from fastapi import APIRouter, Request, HTTPException, Depends

router = APIRouter(prefix="/users", tags=["Users"])


def require_role(role: str):
    def checker(request: Request):
        user = getattr(request.state, "user", None)

        if not user:
            raise HTTPException(status_code=401, detail="Not authenticated")

        if user.get("role") != role:
            raise HTTPException(status_code=403, detail="Forbidden")

        return user

    return checker


@router.get("/profile")
def profile(request: Request):
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(status_code=401)
    return user


@router.get("/admin")
def admin_dashboard(user=Depends(require_role("admin"))):
    return {"message": "Welcome Admin"}


@router.get("/user")
def user_dashboard(user=Depends(require_role("user"))):
    return {"message": "Welcome User"}
