import requests


class Gasto:
    def __init__(self, fecha, valor, metodo_pago, tipo, valor_en_pesos):
        self.__fecha = fecha
        self.__valor = valor
        self.__metodo_pago = metodo_pago
        self.__tipo = tipo
        self.__valor_en_pesos = valor_en_pesos

    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor

    def get_metodo_pago(self):
        return self.__metodo_pago
    
    def set_metodo_pago(self, metodo_pago):
        self.__metodo_pago = metodo_pago

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_valor_en_pesos(self):
        return self.__valor_en_pesos
    
    def set_valor_en_pesos(self, valor_en_pesos):
        self.__valor_en_pesos = valor_en_pesos

    def realizar_conversion(self, destino: str):
        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500").json()
        ##print(response[0])
        if destino.upper() == "USA":
            self.set_valor_en_pesos(response[0]["random"])
        elif destino.upper() == "EUROPA":
            self.set_valor_en_pesos(response[0]["random"] + 200)
