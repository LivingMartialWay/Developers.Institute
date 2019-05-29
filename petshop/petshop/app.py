from flask import Flask
from flask import render_template

from cart import get_cart, save_cart, get_cart_total
from pets import get_pets, find_pet


app = Flask(__name__)


# Required URLs:
# /                 -> index page.
# /pets/            -> listing of all pets in the store
# /pets/3/          -> display the pet with the given ID (numerical)
# /cart/            -> display your cart
# /cart/add_pet/3/  -> add to your cart one pet with the given ID. redirect to /cart/
# /cart/empty/      -> empty your cart. redirect to /

@app.route("/")
def index():
    return render_template('index.html')
