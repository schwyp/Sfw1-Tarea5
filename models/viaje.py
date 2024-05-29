class Viaje:

    def __init__(self, destino, fecha_inicio, fecha_fin, presupuesto_diario):
        self.__destino = destino
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__presupuesto_diario = presupuesto_diario
        self.__gastos = []

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_fecha_fin(self):
        self.__fecha_fin

    def set_fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin

    def get_presupuesto_diario(self):
        return self.__presupuesto_diario
    
    def set_presupuesto_diario(self, presupuesto_diario):
        self.__presupuesto_diario = presupuesto_diario

    def agregar_gasto(self, gasto):
        print(self.__destino)
        gasto.realizar_conversion(self.__destino)
        self.__gastos.append(gasto)
        total_gastado = 0
        for gasto in self.__gastos:
            total_gastado += gasto.get_valor_en_pesos()
        diferencia = self.__presupuesto_diario - total_gastado
        print(f"Presupuesto diario: {self.__presupuesto_diario}")
        print(f"Total gastado: {total_gastado}")
        print(f"Diferencia: {diferencia}")

    def reporte_diario(self):
        reporte = {}
        for gasto in self.__gastos:
            if gasto.get_fecha() not in reporte:
                reporte[gasto.get_fecha()] = {'efectivo': 0, 'tarjeta': 0, 'total': 0}
            if gasto.get_metodo_pago() == 'efectivo':
                reporte[gasto.get_fecha()]['efectivo'] += gasto.get_valor_en_pesos()
            else:
                reporte[gasto.get_fecha()]['tarjeta'] += gasto.get_valor_en_pesos()
            reporte[gasto.get_fecha()]['total'] += gasto.get_valor_en_pesos()
        return reporte
    
    def reporte_por_tipo(self):
        reporte = {}
        for gasto in self.__gastos:
            if gasto.get_tipo() not in reporte:
                reporte[gasto.get_tipo()] = {'efectivo': 0, 'tarjeta': 0, 'total': 0}
            if gasto.get_metodo_pago() == 'efectivo':
                reporte[gasto.get_tipo()]['efectivo'] += gasto.get_valor_en_pesos()
            else:
                reporte[gasto.get_tipo()]['tarjeta'] += gasto.get_valor_en_pesos()
            reporte[gasto.get_tipo()]['total'] += gasto.get_valor_en_pesos()
        return reporte

    