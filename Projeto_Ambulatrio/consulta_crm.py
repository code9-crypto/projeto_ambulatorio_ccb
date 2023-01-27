import requests

def consultar_crm(crm):
    consulta = requests.get(f"https://www.consultacrm.com.br/api/index.php?tipo=crm&q={crm}&chave=2ec53203e65f7e9&destino=xml")
    #consulta = requests.get(f"https://www.consultacrm.com.br/?q_tipo=crm&uf=&q={crm}")
    print(consulta.content.decode())

    resp_consulta = consulta.content.decode().splitlines()[12][15]
    if resp_consulta != "0":
        retorno = True
    else:
        retorno = False


    return retorno