from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):        
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()




@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(random_cafe.to_dict())

@app.route('/all')
def all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify({'cafe':[cafe.to_dict() for cafe in all_cafes]})

@app.route('/search')
def search_cafes():
    query = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location.like(f"%{query}%")))
    found_cafes = result.scalars().all()
    if found_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in found_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    
# HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafes():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new cafe.'})

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_cafes(cafe_id):
    new_price = request.args.get("new_price")
    try:
        update_cafe = db.get_or_404(Cafe, cafe_id)
        update_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={'success': 'Successfully updated price.'})
    except:
        return jsonify(response={'error':{'Not Found':'Sorry, a cafe with this id was not found in the database.'}})

# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['GET','DELETE'])
def delete_cafes(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == 'TopSecretAPIKey':
        try:
            deleted_cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(deleted_cafe)
            db.session.commit()
            
            return jsonify(response={'success': 'Successfully deleted cafe.'}), 200
        except:
            return jsonify(error={'Not Found':'Sorry, a cafe with this id was not found in the database.'}), 404
    else:
        return jsonify(error={'Forbidden':'Sorry, that is not allowed. Make sure you have the correct api_key.'}), 403
    
if __name__ == '__main__':
    app.run(debug=True)
