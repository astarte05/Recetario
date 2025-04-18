import telebot

# Token del bot
TOKEN = '7665289053:AAG0aUs8L-8PJfJs3kmw3Uf-o8u8CB9bgMg'
bot = telebot.TeleBot(TOKEN)

# Diccionario de categorías de ingredientes
ingredientes_categoria = {
    "verdura": [
        "Seta", "Pepino", "Zanahoria", "Aji", "Pimiento", "Berenjena", "Puerro",
        "Tomate", "Esparrago", "Espárrago", "Calabacin", "Calabacín", "Cebolla",
        "Patata", "Calabaza", "Espinaca", "Lechuga", "Quimbombó", "Quimbombo"
    ],
    "especia": [
        "Jengibre", "Ajo", "Albahaca", "Vainilla", "Orégano", "Oregano", "Menta"
    ],
    "fruta": [
        "Manzana", "Plátano", "Platano", "Grosella", "Cereza", "Frambuesa", "Coco",
        "Arándano", "Arandano", "Limón", "Limon"
    ],
    "grano": [
        "Trigo", "Maíz", "Maiz", "Arroz", "Canola", "Caña de azúcar", "Soja"
    ],
    "marisco": [
        "Almeja", "Ostra", "Vieira"
    ]
}

# Invertimos el diccionario: ingrediente específico -> categoría
ingrediente_a_categoria = {
    ingrediente.lower(): categoria
    for categoria, lista in ingredientes_categoria.items()
    for ingrediente in lista
}

# Diccionario de recetas: nombre -> ingredientes (pueden ser genéricos o específicos)
recetas = {
'Aperitivos': {
    "Aperitivos de marisco": ["marisco"],
    "Arenque dulce": ["arenque", "cebolla"],
    "Arenque en escabeche de Arendelle": ["arenque", "limón", "cebolla", "ajo", "especia"],
    "Arenque en escabeche": ["arenque", "limón", "cebolla", "especia"],
    "Bandeja de marisco": ["marisco", "marisco"],
    "Bandeja de ostras": ["ostra", "limón"],
    "Bandeja de queso": ["queso"],
    "Bandeja de verduras a la parrilla": ["verdura", "verdura", "verdura"],
    "Bolas de sésamo": ["trigo", "jengibre", "arroz", "soja", "algas"],
    "Burbujas de ensueño": ["fruto de Dreamlight", "trigo", "caña de azúcar", "slush"],
    "Buñuelos": ["trigo", "queso", "leche", "huevo"],
    "Café con leche": ["grano de café", "leche"],
    "Café": ["grano de café"],
    "Crema de puerros y patata": ["puerro", "patata", "leche", "cebolla", "ajo"],
    "Crema de verduras": ["verdura", "verdura"],
    "Ensalada verde": ["verdura", "lechuga"],
    "Ensalada": ["lechuga"],
    "Espárragos asados": ["espárrago", "canola"],
    "Galletas saladas": ["cereal"],
    "Gazpacho": ["pepino", "tomate", "cebolla", "especia"],
    "Gran bandeja de marisco": ["marisco", "marisco", "marisco", "marisco", "limón"],
    "Hojaldres de berenjena": ["berenjena", "huevo", "queso"],
    "Hojaldres de calabacín": ["calabacín", "huevo", "queso"],
    "Hojaldres de cebolla": ["cebolla", "huevo", "queso"],
    "Hojaldres de calabaza": ["calabaza", "huevo", "queso"],
    "Hojaldres de chiles": ["chile", "huevo", "queso"],
    "Hojaldres de patata": ["patata", "huevo", "queso"],
    "Hojaldres de pimiento": ["pimiento", "huevo", "queso"],
    "Huevos duros": ["huevo"],
    "Moka": ["grano de café", "leche", "grano de cacao"],
    "Patatas fritas": ["canola", "patata"],
    "Potaje": ["patata", "especia", "verdura"],
    "Puré": ["patata"],
    "Salteado de champiñones": ["champiñones", "mantequilla"],
    "Sopa cremosa": ["especia", "leche", "patata", "verdura"],
    "Sopa de calabaza": ["verdura", "leche", "jengibre", "calabaza"],
    "Sopa de okra": ["okra"],
    "Sopa de tomate": ["tomate"],
    "Soufflé": ["queso", "huevo", "leche", "mantequilla"],
    "Té a la menta": ["limón", "menta"],
    "Té de jazmín": ["hojas de té de jazmín", "caña de azúcar"],
    "Té de crisantemo": ["hojas de té de crisantemo", "arándano"],
    "Té oolong": ["hojas de té oolong", "frambuesa"],
    "Verduras a la parrilla": ["espárrago", "bambú", "brócoli", "coliflor", "apio", "chili", "maíz", "berenjena", "cebolla", "calabaza", "algas", "espinacas", "rábano"],
    "Verduritas": ["pimiento", "zanahoria", "pepino", "champiñones", "calabacín"]
},

'Entrantes': {
    "Bacalao al horno crujiente": ["bacalao", "trigo"],
    "Bacalao al horno crujiente con queso": ["bacalao", "trigo", "queso"],
    "Banquete de leona": ["champiñones", "tomate", "orégano", "pez del Aquí y Allí"],
    "Besugo picante al horno": ["besugo", "chili", "mantequilla"],
    "Bocadillo de bogavante": ["bogavante", "trigo", "limón", "mantequilla", "ajo"],
    "Bullabesa": ["marisco x2", "gamba", "tomate", "verdura"],
    "Brocheta de verduras": ["champiñones", "pepino", "cebolla", "pimiento"],
    "Brondada de bacalao": ["bacalao", "patata", "leche", "limón", "ajo"],
    "Cacahuetes ahumados y rape": ["rape", "cacahuete"],
    "Carpa al horno": ["carpa", "mantequilla"],
    "Congee de Mushu": ["trigo", "huevo", "champiñones", "ajo", "jengibre"],
    "Crema de marisco": ["marisco", "verdura x2"],
    "Crema de puerros": ["puerro"],
    "Ensalada de carpa": ["carpa", "limón", "lechuga"],
    "Ensalada de marisco": ["marisco", "lechuga"],
    "Ensalada de pescado": ["pescado", "limón", "lechuga"],
    "Ensalada mediterránea": ["pepino", "tomate", "cebolla", "lechuga", "especia"],
    "Ensalada ranchera": ["lechuga", "pimiento", "maíz", "tomate", "cebolla"],
    "Ensalada sabrosa": ["lechuga", "pepino", "verdura", "especia"],
    "Ensalada sustanciosa": ["verdura x2", "lechuga"],
    "Esturión hervido con mantequilla de albahaca": ["esturión blanco", "albahaca", "limón", "mantequilla"],
    "Fideos udon dulces": ["fruto de Dreamlight", "arroz", "marisco", "caña de azúcar"],
    "Filete de caballa real agridulce": ["caballa real", "caña de azúcar", "limón"],
    "Fish'n'chips": ["pescado", "trigo", "canola", "patata"],
    "Gachas de trigo con frutas": ["leche", "trigo", "fruta"],
    "Gachas de trigo": ["leche", "trigo"],
    "Guiso de verduras": ["patata", "zanahoria", "cebolla"],
    "Gumbo": ["okra", "gamba", "chili", "tomate", "cebolla"],
    "Hamburguesa de atún": ["atún", "cebolla", "limón", "trigo", "verdura"],
    "Hamburguesa de pescado": ["pescado", "trigo"],
    "Hojaldre de espinacas de Kronk": ["espinacas", "queso", "canola"],
    "Hojaldre": ["especia"],
    "Huevos revueltos": ["huevo", "queso"],
    "Kappa Maki": ["algas", "pepino", "arroz"],
    "Latkes": ["cebolla", "patata", "canola", "huevo"],
    "Lenguado Meunière": ["lenguado", "trigo", "mantequilla", "limón"],
    "Linguine al pesto": ["trigo", "mantequilla", "ajo", "orégano"],
    "Lomo de pescado fantasmal": ["pez del Aquí y Allí", "limón", "espárrago", "pimiento", "orégano"],
    "Lomo de pescado": ["pescado", "tomate", "albahaca"],
    "Lubina salteada con verduras": ["lubina", "verdura x2"],
    "Lucioperca americana en papillote": ["lucioperca americana", "albahaca", "verdura", "orégano"],
    "Maguro Sushi": ["atún", "algas", "arroz", "jengibre"],
    "Maki": ["pescado", "algas", "arroz"],
    "Mariscada": ["marisco", "especia", "patata", "maíz"],
    "Mermelada maravillosa": ["fruto de Dreamlight", "trigo"],
    "Nachos": ["chili", "maíz", "queso"],
    "Paella de lanzón": ["lanzón", "gamba", "marisco", "tomate", "arroz"],
    "Pasta con marisco": ["marisco", "trigo", "leche"],
    "Pasta con pescado": ["pescado", "ajo", "trigo", "leche"],
    "Pasta con verduras": ["tomate", "trigo", "verdura"],
    "Pasta": ["trigo", "tomate"],
    "Pastel de marisco": ["marisco", "trigo", "mantequilla"],
    "Pastel de pescado": ["pescado", "trigo", "mantequilla"],
    "Pastel de verduras": ["verdura", "mantequilla", "trigo"],
    "Perca frita sencilla": ["perca", "trigo", "mantequilla"],
    "Pescado a la parrilla": ["pescado"],
    "Pescado criollo": ["pescado", "verdura", "ajo", "arroz", "tomate"],
    "Pez espada con ajo y limón": ["pez espada", "ajo", "limón"],
    "Pez globo al vapor": ["pez globo", "jengibre", "ajo"],
    "Pez sabroso": ["pescado", "verdura"],
    "Pizza de champiñones": ["champiñones", "trigo", "tomate", "queso"],
    "Pizza griega": ["especia", "tomate", "cebolla", "queso", "trigo"],
    "Pizza margarita": ["especia", "tomate", "queso", "trigo"],
    "Pizza vegetariana": ["verdura x2", "tomate", "queso", "trigo"],
    "Pizza": ["tomate", "queso", "trigo"],
    "Plato principal de pescado a la parrilla": ["pescado", "verdura"],
    "Poutine": ["patata", "canola", "queso"],
    "Rape frito": ["rape", "tomate", "pepino", "patata"],
    "Ratatouille": ["tomate", "berenjena", "pepino", "cebolla", "especia"],
    "Risotto de pescado": ["pescado", "arroz", "mantequilla"],
    "Sake Maki": ["arroz", "algas", "salmón"],
    "Sake Sushi": ["salmón", "arroz"],
    "Salmón a la sidra": ["salmón", "caña de azúcar", "manzana"],
    "Salmón teriyaki": ["soja", "salmón", "caña de azúcar", "arroz", "jengibre"],
    "Sandwich de mantequilla de cacahuete": ["cacahuete", "trigo"],
    "Sopa de marisco": ["marisco", "verdura x2"],
    "Sopa de pescado": ["pescado", "verdura", "leche"],
    "Sopa wanton": ["huevo", "gamba", "trigo", "cebolla"],
    "Spaghetti Arrabbiata": ["tomate", "trigo", "chili"],
    "Sushi de pez globo": ["pez globo", "arroz", "algas"],
    "Sushi": ["pescado", "arroz"],
    "Taco vegetariano": ["maíz", "chili", "queso", "verdura"],
    "Tacos de pescado": ["maíz", "chili", "queso", "pescado"],
    "Tekka Maki": ["atún", "soja", "algas", "arroz"],
    "Tilapia salteada con verduras": ["tilapia", "verdura x2"],
    "Tortilla de albahaca": ["albahaca", "huevo", "queso", "leche"],
    "Tortilla francesa": ["huevo", "queso", "leche"],
    "Tortilla japonesa": ["huevo", "caña de azúcar"],
    "Trucha arcoiris salteada": ["trucha arcoiris", "tomate", "cebolla"],
    "Verduras horneadas": ["verdura x2", "queso", "especia"],
    "Verduras sabrosas": ["verdura", "especia"],
    "Vieiras cremosas al ajo": ["vieira", "limón", "mantequilla", "ajo"]
],

'Postres': [
    "Banana Split": ["slush", "plátano", "leche", "caña de azúcar", "caña de azúcar"],
    "Batido": ["leche"],
    "Buñuelos": ["canola", "trigo", "huevo", "caña de azúcar"],
    "Cannoli": ["trigo", "queso", "huevo", "vainilla"],
    "Caramelos de menta": ["caña de azúcar", "menta"],
    "Caramelos": ["caña de azúcar"],
    "Casa de jengibre": ["trigo", "jengibre", "caña de azúcar", "vainilla", "huevo"],
    "Chocolate a la menta": ["menta", "caña de azúcar", "mantequilla", "grano de cacao"],
    "Chocolate caliente": ["grano de cacao", "leche", "caña de azúcar"],
    "Chocolate primaveral": ["fruta ovoide", "caña de azúcar", "grano de cacao"],
    "Cosa gris": ["grano de cacao", "leche", "mantequilla"],
    "Crema pastelera y frutas": ["cualquier fruta", "cualquier fruta", "cualquier fruta", "leche", "caña de azúcar"],
    "Crepe": ["trigo", "huevo", "leche", "vainilla"],
    "Cucuruchos ácidos": ["slush", "limón", "caña de azúcar"],
    "Cucuruchos": ["slush"],
    "Cuencos de huevos de primavera": ["fruta ovoide", "verdura ovoide de primavera", "huevo salvaje de primavera", "grano de cacao", "caña de azúcar"],
    "Cupcake de Minnie": ["mantequilla", "leche", "trigo", "caña de azúcar", "manzana"],
    "Cupcake de Spaceship Earth": ["mantequilla", "leche", "trigo", "caña de azúcar", "coco"],
    "Cupcake de Stitch": ["mantequilla", "leche", "trigo", "caña de azúcar", "arándano"],
    "Cupcake de frambuesa de la Princesa Aurora": ["mantequilla", "leche", "trigo", "caña de azúcar", "frambuesa"],
    "Cupcake de sirena": ["mantequilla", "leche", "trigo", "caña de azúcar", "vieira"],
    "Ensalada de bayas": ["frambuesa", "arándano", "grosella"],
    "Galleta de 'Mi héroe'": ["trigo", "mantequilla", "cualquier especia"],
    "Galletas con pepitas de chocolate": ["grano de cacao", "trigo", "caña de azúcar", "mantequilla"],
    "Galletas de jengibre de Halloween": ["trigo", "jengibre", "calabaza"],
    "Galletas de jengibre de Minnie": ["trigo", "jengibre"],
    "Galletas del País de las Maravillas": ["mantequilla", "caña de azúcar", "vainilla", "trigo"],
    "Galletas": ["trigo", "caña de azúcar", "mantequilla"],
    "Gofre con cocholate": ["trigo", "leche", "huevo", "grano de cacao"],
    "Gofre con mantequilla de cacahuete": ["cacahuete", "trigo", "huevo", "leche"],
    "Gofre con mermelada": ["cualquier fruta", "trigo", "huevo", "leche"],
    "Gofre": ["trigo", "leche", "huevo", "cualquier especia"],
    "Helado de coco": ["coco", "caña de azúcar", "leche", "slush"],
    "Helado de chocolate": ["grano de cacao", "caña de azúcar", "leche", "slush"],
    "Helado de ensueño": ["fruto de Dreamlight", "leche", "slush"],
    "Helado de plátano": ["plátano", "caña de azúcar", "leche", "slush"],
    "Helado de vainilla": ["slush", "leche", "caña de azúcar", "vainilla"],
    "Helado": ["slush", "leche", "caña de azúcar"],
    "Huevos rellenos primaverales": ["fruta ovoide", "verdura ovoide de primavera", "huevo salvaje de primavera", "albahaca"],
    "Macedonia": ["cualquier fruta"],
    "Malvavisco asado": ["malvavisco rosa", "malvavisco rosa", "malvavisco azul", "malvavisco azul"],
    "Manzanas al caramelo": ["caña de azúcar", "manzana"],
    "Pastel de fruta": ["trigo", "cualquier fruta", "cualquier fruta", "cualquier fruta"],
    "Pastéis de nata": ["maíz", "huevo", "leche", "vainilla"],
    "Patapolo": ["slush", "caña de azúcar", "cualquier fruta"],
    "Polo tropical": ["slush", "cualquier fruta", "caña de azúcar", "coco"],
    "Red velvet": ["trigo", "queso", "huevo", "grano de cacao", "vainilla"],
    "S'mares": ["malvavisco rosa", "malvavisco azul", "trigo", "trigo"],
    "Slush dulce": ["slush", "caña de azúcar"],
    "Sorbete de frutas": ["slush", "cualquier fruta"],
    "Sorbete de frutos rojos": ["slush", "frambuesa", "grosella", "caña de azúcar"],
    "Sorbete de limón": ["slush", "limón"],
    "Sorbete de manzana": ["slush", "manzana", "caña de azúcar"],
    "Sorbete de menta": ["slush", "menta"],
    "Tarta de Aurora": ["trigo", "caña de azúcar", "huevo", "cualquier fruta", "leche"],
    "Tarta de arándanos": ["arándano", "trigo", "mantequilla"],
    "Tarta de boda": ["mantequilla", "caña de azúcar", "vainilla", "trigo", "huevo"],
    "Tarta de cerezas": ["cereza", "trigo", "mantequilla"],
    "Tarta de coco": ["coco", "trigo", "huevo", "caña de azúcar"],
    "Tarta de cumpleaños": ["grano de cacao", "trigo", "caña de azúcar", "huevo", "mantequilla"],
    "Tarta de frutas": ["cualquier fruta", "trigo", "mantequilla"],
    "Tarta de grosellas de Blancanieves": ["grosellas", "trigo", "mantequilla"],
    "Tarta de manzana": ["manzana", "trigo", "mantequilla"],
    "Tarta de merengue": ["limón", "trigo", "huevo", "mantequilla"],
    "Tarta de plátano": ["plátano", "trigo", "mantequilla"],
    "Tarta de queso": ["queso", "trigo", "caña de azúcar", "cualquier fruta"],
    "Tarta de zanahoria": ["zanahoria", "trigo", "huevo", "caña de azúcar"],
    "Tarta extravagante": ["fruto de Dreamlight", "trigo", "mantequilla"],
    "Tronco de navidad": ["trigo", "grano de cacao", "vainilla", "cereza"],
    "Té de burbujas de coco": ["caña de azúcar", "leche", "coco"],
    "Té de burbujas de frambuesa": ["caña de azúcar", "leche", "frambuesa"],
    "Té de burbujas de grosellas": ["caña de azúcar", "leche", "grosella"],
    "Té de burbujas de menta": ["caña de azúcar", "leche", "menta"],
    "Té de burbujas": ["caña de azúcar", "leche"],
    "Zarzaparrilla": ["jengibre", "caña de azúcar", "vainilla"]
    }
}

# 📩 Mensaje de bienvenida con instrucciones claras
@bot.message_handler(commands=['start'])
def bienvenida(message):
    texto = (
        "👋 ¡Hola! Bienvenido/a al recetario interactivo.\n\n"
        "📌 Por favor, **escribe los ingredientes con tilde si llevan tilde**, así puedo reconocerlos correctamente.\n\n"
        "🥄 Puedes escribirme los ingredientes que tienes separados por comas (ej: *zanahoria, almeja*), "
        "y yo te diré qué recetas puedes hacer.\n\n"
        "📚 También puedes ver el recetario con estos comandos:\n"
        "  - `/recetario` → ver todo el recetario completo\n"
        "  - `/aperitivos` → ver solo los aperitivos\n"
        "  - `/entrantes` → ver los entrantes\n"
        "  - `/postres` → ver los postres\n\n"
        "¡Escribe lo que tengas y manos a la cocina! 🍳"
    )
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

# 📚 Comandos para mostrar secciones del recetario (YA FUNCIONALES)
@bot.message_handler(commands=['recetario'])
def mostrar_recetario_completo(message):
    texto = (
        "*📖 Recetario completo*\n\n"
        "🍢 *Aperitivos*\n"
        "• Aperitivos de marisco\n\n"
        "🍽️ *Entrantes*\n"
        "• Bacalao al horno crujiente\n\n"
        "🍰 *Postres*\n"
        "• Banana Split"
    )
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

@bot.message_handler(commands=['aperitivos'])
def mostrar_aperitivos(message):
    texto = (
        "*🍢 Aperitivos:*\n"
        "• Aperitivos de marisco"
    )
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

@bot.message_handler(commands=['entrantes'])  # ← Asegúrate de que tu comando sea /entrantes
def mostrar_entrantes(message):
    texto = (
        "*🍽️ Entrantes:*\n"
        "• Bacalao al horno crujiente"
    )
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

@bot.message_handler(commands=['postres'])
def mostrar_postres(message):
    texto = (
        "*🍰 Postres:*\n"
        "• Banana Split"
    )
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

# 🍲 Búsqueda de recetas según ingredientes del usuario
@bot.message_handler(func=lambda message: True)
def responder_ingredientes(message):
    entrada = [i.strip().lower() for i in message.text.split(",")]
    ingredientes_usuario = set(entrada)

    categorias_usuario = set()
    for ing in ingredientes_usuario:
        cat = ingrediente_a_categoria.get(ing)
        if cat:
            categorias_usuario.add(cat)

    recetas_posibles = []

    # Recorrer todas las recetas de cada categoría
    for categoria in recetas:
        for nombre_receta, ingredientes_receta in recetas[categoria].items():
            posibles = True
            detalle_ingredientes = []

            for ing in ingredientes_receta:
                ing_lower = ing.lower()
                if ing_lower in ingredientes_usuario:
                    detalle_ingredientes.append(f"- {ing} (lo tienes)")
                elif ing_lower in ingredientes_categoria and ing_lower in categorias_usuario:
                    opciones = ", ".join(ingredientes_categoria[ing_lower])
                    detalle_ingredientes.append(f"- {ing} (puede ser: {opciones})")
                else:
                    posibles = False
                    break

            if posibles:
                recetas_posibles.append(f"🍽️ *{nombre_receta}*:\n" + "\n".join(detalle_ingredientes))

    if recetas_posibles:
        respuesta = "Con lo que tienes, podrías preparar:\n\n" + "\n\n".join(recetas_posibles)
    else:
        respuesta = "😕 No encontré recetas que puedas hacer con eso. Prueba con más ingredientes."

    bot.send_message(message.chat.id, respuesta, parse_mode="Markdown")

# 🚀 ¡Arrancamos el bot!
bot.polling()