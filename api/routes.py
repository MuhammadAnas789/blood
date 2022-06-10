from api.models import User, blood_request
from flask import request, jsonify
from api import app, db


current_user_id = ''


@app.route("/signup", methods=['GET', 'POST'])
def signup():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        city = request.form.get('city')
        blood_group = request.form.get('blood_group')
        gender = request.form.get("gender")
        password = request.form.get('password')
        print(name, email, city, blood_group, gender)
        user = User.query.filter_by(email=email).first()
        if user:
            return {"email": "Email Already Exists!", "status": "200"}

        user_add = User(
            name=name,
            email=email,
            password=password,
            city=city,
            blood_group=blood_group,
            gender=gender
        )

        db.session.add(user_add)
        db.session.commit()
        return {"msg": "Account created successfully"}


@app.route("/login", methods=['GET', "POST"])
def login():
    if request.method == "POST":
        global current_user_id
        print("login Success")
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user:
            if user.password == password:

                current_user_id = user.id
                return {"msg": "logged in"}
            else:
                return {"email": "wrong Password"}
        else:
            return {"email": "wrong email"}


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form.get("name")

        if current_user_id:
            pass
        else:
            print("done")
            return {"msg": "Please login to access this page"}

        users = []
        data = User.query.filter_by(blood_group=search).all()

        for user in data:
            if current_user_id == user.id:
                pass
            else:
                l = {'name': user.name, 'id': user.id}
                users.append(l)
        return jsonify(users)


@app.route("/req/<id>")
def req(id):
    if current_user_id:
        pass
    else:
        print("done")
        return {"msg": "Please login to access this page"}
    user = User.query.get(current_user_id)

    data = blood_request(
        request_from=id,
        request_to=user.id,
        name=user.name
    )
    db.session.add(data)
    db.session.commit()
    return "requset send successfully"


@app.route("/blood_requests", methods=["POST"])
def blood_requests():
    reque = blood_request.query.filter_by(request_to=current_user_id).all()

    for value in reque:
        print(value.id)

    req = []

    for data in reque:
        l = {'name': data.name,
             'status': data.status,
             'id': data.id}
        req.append(l)
    return jsonify(req)


@app.route("/Approve/<id>")
def Approve(id):
    data = blood_request.query.filter_by(id=id).first()
    data.status = "Approved"
    db.session.commit()
    return "Approved"


@app.route("/reject/<id>")
def Reject(id):
    data = blood_request.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return "Rejected"
