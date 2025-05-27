from prettytable import PrettyTable

territorio_chile = [
    ["Arica y Parinacota", [
        ["Arica", ["Arica", "Camarones"]],
        ["Parinacota", ["Putre", "General Lagos"]]
    ]],
    ["Tarapacá", [
        ["Iquique", ["Iquique", "Alto Hospicio"]],
        ["Tamarugal", ["Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]]
    ]],
    ["Antofagasta", [
        ["Antofagasta", ["Antofagasta", "Mejillones", "Sierra Gorda"]],
        ["El Loa", ["Calama", "Ollagüe", "San Pedro de Atacama"]],
        ["Tocopilla", ["Tocopilla"]]
    ]],
    ["Atacama", [
        ["Copiapó", ["Copiapó", "Caldera", "Tierra Amarilla"]],
        ["Chañaral", ["Chañaral", "Diego de Almagro"]],
        ["Huasco", ["Vallenar", "Freirina", "Huasco", "Alto del Carmen"]]
    ]],
    ["Coquimbo", [
        ["Elqui", ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paihuano", "Vicuña"]],
        ["Limarí", ["Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]],
        ["Choapa", ["Illapel", "Canela", "Los Vilos", "Salamanca"]]
    ]],
    ["Valparaíso", [
        ["Valparaíso", ["Valparaíso", "Viña del Mar", "Concón", "Quintero", "Puchuncaví", "Juan Fernández"]],
        ["Marga Marga", ["Quilpué", "Villa Alemana", "Limache", "Olmué"]],
        ["Quillota", ["Quillota", "La Calera", "La Cruz", "Nogales", "Hijuelas"]],
        ["San Antonio", ["San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo"]],
        ["San Felipe de Aconcagua", ["San Felipe", "Llaillay", "Panquehue", "Putaendo", "Santa María"]],
        ["Los Andes", ["Los Andes", "Calle Larga", "Rinconada", "San Esteban"]]
    ]],
    ["O'Higgins", [
        ["Cachapoal", ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente"]],
        ["Colchagua", ["San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]],
        ["Cardenal Caro", ["Pichilemu", "La Estrella", "Litueche", "Marchigüe", "Navidad", "Paredones"]]
    ]],
    ["Maule", [
        ["Talca", ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pencahue", "Río Claro", "San Clemente", "San Rafael"]],
        ["Linares", ["Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"]],
        ["Cauquenes", ["Cauquenes", "Chanco", "Pelluhue"]]
    ]],
    ["Ñuble", [
        ["Diguillín", ["Bulnes", "Chillán", "Chillán Viejo", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay"]],
        ["Itata", ["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco"]],
        ["Punilla", ["San Carlos", "San Fabián", "San Nicolás"]]
    ]],
    ["Biobío", [
        ["Concepción", ["Concepción", "Chiguayante", "Coronel", "Florida", "Hualpén", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé"]],
        ["Arauco", ["Arauco", "Cañete", "Contulmo", "Curanilahue", "Lebu", "Los Álamos", "Tirúa"]],
        ["Biobío", ["Alto Biobío", "Antuco", "Cabrero", "Laja", "Los Ángeles", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel"]]
    ]]
]

# tabla = PrettyTable(["Región","Provincia","Comuna"])

# for fila in territorio_chile:
#     tabla.add_row([fila[0]])

# print(tabla)

print(len(territorio_chile))
print(len(territorio_chile[0]))