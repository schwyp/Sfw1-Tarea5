from models.viaje import Viaje
from models.gasto import Gasto


viaje = Viaje("EUROPA", "2021-06-01", "2021-06-05", 5000)


gasto1 = Gasto("2021-06-01", 100, "efectivo", "transporte", 100)
gasto2 = Gasto("2021-06-02", 200, "tarjeta", "alojamiento", 200)
gasto3 = Gasto("2021-06-03", 300, "efectivo", "alimentación", 300)
gasto4 = Gasto("2021-06-04", 400, "tarjeta", "entretenimiento", 400)
gasto5 = Gasto("2021-06-05", 500, "efectivo", "compras", 500)

viaje.agregar_gasto(gasto1)
viaje.agregar_gasto(gasto2)
viaje.agregar_gasto(gasto3)
viaje.agregar_gasto(gasto4)
viaje.agregar_gasto(gasto5)

print("--- Reporte diario ---")
for reporte in viaje.reporte_diario():
    print(reporte + " Efectivo: " + str(viaje.reporte_diario()[reporte]["efectivo"]) + " Tarjeta: " + str(viaje.reporte_diario()[reporte]["tarjeta"]) + " Total: " + str(viaje.reporte_diario()[reporte]["total"]) + "\n")

print("--- Reporte por tipo ---")
for reporte in viaje.reporte_por_tipo():
    print(reporte + " Efectivo: "  + str(viaje.reporte_por_tipo()[reporte]["efectivo"]) + " Tarjeta: " + str(viaje.reporte_por_tipo()[reporte]["tarjeta"]) + " Total: " + str(viaje.reporte_por_tipo()[reporte]["total"]) + "\n")