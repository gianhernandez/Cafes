from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from database import db
from forms import AddForm
from models import Cafe
import os
from dotenv import load_dotenv


load_dotenv('.env')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///cafes.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Display all cafes
@app.route('/', methods=['GET'])
def get_all_cafes():
    cafes = Cafe.query.order_by(Cafe.id).all()
    return render_template('index.html', cafes=cafes)


# Add New Cafe
@app.route('/add-cafe', methods=['GET', 'POST'])
def add_cafe():
    form = AddForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('get_all_cafes'))
    return render_template('add.html', form=form)


# Delete a Cafe
@app.route('/delete-cafe/<int:cafe_id>')
def delete_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('get_all_cafes'))


if __name__ == '__main__':
    app.run()
