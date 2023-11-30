import os
from flask import Flask, render_template, request
from flask_cors import CORS #gestion des accès au w.s.
import json
import pandas as pd
from time import time
import numpy as np

from controller import ProductsC, BrandsC, BodyPartsC, CustomersC, GendersC, InvoicesC, OrdersC, OrderDetailsC, InvoicesC

from model import ProductsM, BrandsM, BodyPartsM, CustomersM, GendersM, InvoicesM, OrdersM, OrderDetailsM, InvoicesM

app = Flask(__name__)


#CORS(app, resources={fr"api/lvmh/sephora/postgresql/*": {"origins": "http://localhost:63342"}})

CORS(app, resources={fr"api/lvmh/sephora/postgresql/*": {"origins": "*"}})

Privacy_Policy='''
Confidentiality and Security: We prioritize the protection of your information and have implemented appropriate security measures to prevent unauthorized access, disclosure, or alteration. Only authorized personnel have access to this information, and they are bound by confidentiality obligations.

Access Restrictions and Exploration: Unauthorized access to our application, including attempting to explore its functioning by accessing the root of the API, is strictly prohibited. Any violation of this privacy policy or our terms of use may result in disciplinary action, including account termination and, if necessary, legal action.

Information Retention: We retain your information for as long as necessary to fulfill the purposes stated in this privacy policy, unless a longer retention period is required or permitted by law.

Changes to the Privacy Policy: We reserve the right to modify this privacy policy at any time. Any changes will be effective upon publication on our website or within the application. It is your responsibility to regularly review this privacy policy for any updates.

Consent: By using our application, you consent to the collection, use, and disclosure of your information in accordance with this privacy policy.

Last Updated: 2023/11/30
'''

@app.route('/', methods=['GET'])
def start():
    return {'Notice': "The api is protected, you could not do anything.",
            'A message for you ':"Hello dear dev./user WELCOME TO the Privacy Policy lvmh_sephora",
            'Pay attention':"We collect certain information, including your IP address and MAC address, for troubleshooting purposes. This information is collected automatically and anonymously and is not used to personally identify you unless there is a technical issue.",
            'Privacy Policy':Privacy_Policy}


@app.route(f'/api/lvmh/sephora/postgresql/getbrands/',methods=['GET'])
def get_brands():

    #ip = request.client

    brandc = BrandsC.Brands().visualiserBrands()

    brand = {}

    liste_brand = []

    for bc in brandc:

        brand = {
            "brand_id" : bc.getBrandId(),
            "brand_name" : bc.getBrandName()
        }

        liste_brand.append(brand)

    return {'response':liste_brand}


if __name__=='__main__':

    # Run flask with the following defaults
    app.run(debug=True, port=5000, host='0.0.0.0', )