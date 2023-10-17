import os
import stripe
from flask import Flask, render_template, request



stripe_keys = {
    "sk_test_51O0EYTBSiu2J8WSYEUrXqQgyznVyyJpcjjA8PqY2XaeH5ONeiiRUdt0q0VBCxSxQUYflBBil1YPh7RcaECqFy4Ln00k4RkJ4l1": os.environ.get("STRIPE_SECRET_KEY"),
    "pk_test_51O0EYTBSiu2J8WSY8BPlDOXRnwSB6X15HmG6znnnAL3wvT18QsaTt73NlvfTXUDhLpL632AKEWYHfMON54qLSWKE004AfEbyXM": os.environ.get("STRIPE_PUBLISHABLE_KEY")
}

stripe.api_key = stripe_keys["sk_test_51O0EYTBSiu2J8WSYEUrXqQgyznVyyJpcjjA8PqY2XaeH5ONeiiRUdt0q0VBCxSxQUYflBBil1YPh7RcaECqFy4Ln00k4RkJ4l1"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['pk_test_51O0EYTBSiu2J8WSY8BPlDOXRnwSB6X15HmG6znnnAL3wvT18QsaTt73NlvfTXUDhLpL632AKEWYHfMON54qLSWKE004AfEbyXM'])

@app.route('/charge', methods=['POST'])
def charge():

