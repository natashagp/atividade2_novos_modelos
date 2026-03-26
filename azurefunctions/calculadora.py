import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger1")  # Coloque no nome da rota, o nome que vc cadastrou no portal da Azure (http_trigger1, caso não tenha alterado)
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse: # Normalmente, colocamos o nome da função, igual ao nome da rota

    try:
        operacao = req.params.get('operacao')
        numero1 = req.params.get('numero1')
        numero2 = req.params.get('numero2')
        if not operacao or not numero1 or not numero2:
            raise ValueError(f"Parâmetro inválido. Esperados parametros operacao, numero1 e numero2.")

        if operacao == "soma":
            resposta = float(numero1) + float(numero2)
        else:
            raise ValueError(f"Parametro operacao incorreto: [{operacao}].")

        ret = {"mensagem": f"Segue o resultado da {operacao} entre [{numero1}] e [{numero2}]: [{resposta}].",
               "resposta": resposta,
               "autor": "Pedrinho",
               "versao": 1.0}

        return func.HttpResponse(json.dumps(ret), status_code=200)
    except Exception as err:
        return func.HttpResponse(json.dumps({"message": str(err)}),
                                 status_code=400)
