import datetime

data = datetime.date.today()

def mes_do_ano():
    if data.strftime("%B") == "January":
        mes = "Janeiro"
    elif data.strftime("%B") == "February":
        mes = "Fevereiro"
    elif data.strftime("%B") == "March":
        mes = "Março"
    elif data.strftime("%B") == "April":
        mes = "Abril"
    elif data.strftime("%B") == "May":
        mes = "Maio"
    elif data.strftime("%B") == "June":
        mes = "Junho"
    elif data.strftime("%B") == "July":
        mes = "Julho"
    elif data.strftime("%B") == "August":
        mes = "Agosto"
    elif data.strftime("%B") == "September":
        mes = "Setembro"
    elif data.strftime("%B") == "October":
        mes = "Outubro"
    elif data.strftime("%B") == "November":
        mes = "Novembro"
    elif data.strftime("%B") == "December":
        mes = "Dezembro"

    return mes