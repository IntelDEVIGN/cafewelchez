import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

items = [
        {
          "orden": 11100,
          "nombre": "Colores de la Estación",
          "descripcion": "",
          "nivel": 1,
          "precio": 90,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11150,
          "nombre": "con Yogurt",
          "descripcion": "",
          "nivel": 2,
          "precio": 119,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11200,
          "nombre": "con Yogurt y Granola",
          "descripcion": "",
          "nivel": 2,
          "precio": 129,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11250,
          "nombre": "Capricho Mañanero",
          "descripcion": "",
          "nivel": 1,
          "precio": 90,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11300,
          "nombre": "Amor Amor",
          "descripcion": "",
          "nivel": 1,
          "precio": 120,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11350,
          "nombre": "Huevos Marinita",
          "descripcion": "",
          "nivel": 1,
          "precio": 150,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11400,
          "nombre": "Frijolero",
          "descripcion": "",
          "nivel": 1,
          "precio": 60,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11450,
          "nombre": "Baleadas",
          "descripcion": "",
          "nivel": 1,
          "precio": 75,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11500,
          "nombre": "con Huevo",
          "descripcion": "",
          "nivel": 2,
          "precio": 90,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11550,
          "nombre": "Paris Copán",
          "descripcion": "",
          "nivel": 1,
          "precio": 0,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11600,
          "nombre": "con Jamón y Queso",
          "descripcion": "",
          "nivel": 2,
          "precio": 140,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11650,
          "nombre": "con Mermelada y Mantequilla",
          "descripcion": "",
          "nivel": 2,
          "precio": 50,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11700,
          "nombre": "Madrugada Maya",
          "descripcion": "",
          "nivel": 1,
          "precio": 150,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11750,
          "nombre": "Omelet a tu Antojo",
          "descripcion": "Dos ingredientes",
          "nivel": 1,
          "precio": 135,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11800,
          "nombre": "Ingrediente Adicional:",
          "descripcion": "Jamón, Queso, Chile Dulce, Tomate o Cebolla",
          "nivel": 2,
          "precio": 20,
          "precio_2": 0,
          "activo": true
        },
        {
          "orden": 11850,
          "nombre": "Pie de Queso y Panceta",
          "descripcion": "",
          "nivel": 1,
          "precio": 125,
          "precio_2": 0,
          "activo": true
        }
      ]

cursor.executemany("INSERT INTO menu_item VALUES ()", items)