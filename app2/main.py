from fastapi import FastAPI,HTTPException
import uvicorn
import data_base
from pydantic import BaseModel

app=FastAPI()

class Schema(BaseModel):
    name : str
    email: str
    age: int 

login_data=[]

@app.get("/")
def home():
    return {"ram":"ram is good"}



@app.post("/apply")
def sing(user: Schema):
    try:
        
        # for value in user:
        #     login_data.append(value)
        login_data.append(user)
        return {"status": "success", "received": user}
    except Exception as e :
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/all-users")
def get_all_users():
    # FastAPI automatically converts this list to a JSON array
    return {"total": len(login_data), "users": login_data}





if __name__=="__main__":
    # print(f'i am checking myself to know __name__{__name__} and __main__ {"__main__"}')
    print(login_data)
    uvicorn.run( "main:app", host="0.0.0.0", port=8000, reload=True)