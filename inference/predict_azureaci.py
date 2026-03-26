import sys, json, os, joblib
import pandas as pd
import numpy as np
from flask import Flask


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


app = Flask(__name__)
app.json_encoder = NpEncoder
global meumodelo


def init():
    print(f"Python version: {sys.version}")
    try:
        print(f"Abs path: {os.path.abspath('.')}")
        print(f"Arquivos e diretorios: {os.listdir()}")
        global meumodelo

        print("Carregando modelo (warming model).")
        meumodelo = joblib.load('./modelo/modelo_bin.pkl')
    except Exception as err:
        print(f"Exception: \n{err}")


def run(data):
    print(data)

    try:
        json_ = json.loads(data)
        print(f"received data {json_}")

        campos = pd.DataFrame(json_)

        if campos.shape[0] == 0:
            return "Dados de chamada da API estão incorretos.", 400

        for col in meumodelo.feature_names_in_:
            if col not in campos.columns:
                campos[col] = 0
        x = campos[meumodelo.feature_names_in_]

        prediction = meumodelo.predict(x)
        try:
            predict_proba = meumodelo.predict_proba(x)
        except Exception as ex:
            predict_proba = None

        ret = json.dumps({'prediction': list(prediction),
                          'proba': list(predict_proba),
                          'author': "Elthon Manhas de Freitas"}, cls=NpEncoder)
        print(ret)

        return app.response_class(response=ret, mimetype='application/json')
    except Exception as err:
        print(f"Exception: \n{err}")
        return f"Error processing input data: {json_}"
