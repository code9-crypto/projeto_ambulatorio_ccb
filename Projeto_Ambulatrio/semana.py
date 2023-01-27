import datetime

def dia_da_semana():
    x = datetime.date.today()
    if x.strftime("%A") == "Monday":
        semana = "Segunda-feira"
    elif x.strftime("%A") == "Tuesday":
        semana = "Terça-feira"
    elif x.strftime("%A") == "Wednesday":
        semana = "Quarta-feira"
    elif x.strftime("%A") == "Thursday":
        semana = "Quinta-feira"
    elif x.strftime("%A") == "Friday":
        semana = "Sexta-feira"
    elif x.strftime("%A") == "Saturday":
        semana = "Sábado"
    elif x.strftime("%A") == "Sunday":
        semana = "Domingo"

    return semana









