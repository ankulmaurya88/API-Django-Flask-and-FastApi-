from flask import Flask,request,jsonify
import json
from data.data_base import unquine_data,normal_data,key_value_data,save_to_disk
import os
app=Flask(__name__)


def get_user_by_name(username):
    return next((u for u in normal_data if u.get("username") == username), None)


@app.get("/")
def health():
    return {"status": "working"}

@app.post("/registration")
def resi():
    
    try:
        user_data=request.get_json()
        if not user_data :
            return jsonify({"status": "Invalid data", "error": "No JSON payload provided"}), 400
        
        normal_data.append(user_data)
        save_to_disk()
        print(f"Data saved! Total users: {len(normal_data)}")
        return jsonify ({"status": "Success",'message':"User added"}),200
    except Exception as e:

        return jsonify({"status":"Error","Messsage":str(e)}),500
    

@app.put("/change/<username>")
def fullbodychange(username):
    try:
        user = get_user_by_name(username)
        if not user:
            return jsonify({"status": "error", "message": "User not found"}), 404
        
        new_data = request.get_json()
        if not new_data:
            return jsonify({"status": "error", "message": "No data provided"}), 400

        # Replace content: clear old keys and add new ones
        user.clear()
        user.update(new_data)
        
        save_to_disk(normal_data)
        return jsonify({"status": "success", "message": "Full update complete"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.patch('/partial/<username>')
def partialbodychange(username):
    try:
        user = get_user_by_name(username)
        if not user:
            return jsonify({"status": "error", "message": "User not found"}), 404
        
        updates = request.get_json()
        # Update only specific fields provided in JSON
        user.update(updates)
        
        save_to_disk(normal_data)
        return jsonify({"status": "success", "message": "Partial update complete"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500




@app.delete('/delete/<username>')
def deletedata(username):
    try:
        user = get_user_by_name(username)
        if not user:
            return jsonify({"status": "error", "message": "User not found"}), 404
        
        normal_data.remove(user)
        save_to_disk(normal_data)
        return jsonify({"status": "success", "message": f"User {username} deleted"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.get("/users")
def get_users():
    # If using the file-based method, load the file first:
    # with open("data/data_storage.json", "r") as f:
    #     normal_data = json.load(f)
    
    return jsonify({
        "total_users": len(normal_data),
        "users": normal_data
    }), 200

print(normal_data)      
if __name__ == "__main__":
    app.run(debug=True)