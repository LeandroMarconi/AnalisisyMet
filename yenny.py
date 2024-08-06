import sqlite3
from usuario import usuario
from libro import libro

conn = sqlite3.connect('libroyenny.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS usuario (
          nombre TEXT PRIMARY KEY,
          passw TEXT NOT NULL
          )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS libro (
          id INTEGER PRIMARY KEY,
          titulo TEXT NOT NULL,
          autor TEXT NOT NULL,
          precio REAL NOT NULL,
          stock INTEGER NOT NULL
          )""")
conn.commit()

usuario1 = usuario('Leandro', 'Leandro1234')
usuario2 = usuario('Joaquin', 'Joaquin1234')

c.execute("INSERT OR IGNORE INTO usuario (nombre, passw) VALUES (?, ?)", (usuario1.nombre, usuario1.passw))
c.execute("INSERT OR IGNORE INTO usuario (nombre, passw) VALUES (?, ?)", (usuario2.nombre, usuario2.passw))
conn.commit()

libro1 = libro(1, '1984', 'George Orwell', 15000, 20)
libro2 = libro(2, 'To Kill a Mockingbird', 'Harper Lee', 10000, 5)
libro3 = libro(3, 'The Great Gatsby', 'F. Scott Fitzgerald', 12000, 15)
libro4 = libro(4, 'Pride and Prejudice', 'Jane Austen', 11000, 50)
libro5 = libro(5, 'Moby Dick', 'Herman Melville', 9000, 6)

c.execute("INSERT OR IGNORE INTO libro (id, titulo, autor, precio, stock) VALUES (?, ?, ?, ?, ?)", 
          (libro1.libro_id, libro1.titulo, libro1.autor, libro1.precio, libro1.stock))
c.execute("INSERT OR IGNORE INTO libro (id, titulo, autor, precio, stock) VALUES (?, ?, ?, ?, ?)", 
          (libro2.libro_id, libro2.titulo, libro2.autor, libro2.precio, libro2.stock))
c.execute("INSERT OR IGNORE INTO libro (id, titulo, autor, precio, stock) VALUES (?, ?, ?, ?, ?)", 
          (libro3.libro_id, libro3.titulo, libro3.autor, libro3.precio, libro3.stock))
c.execute("INSERT OR IGNORE INTO libro (id, titulo, autor, precio, stock) VALUES (?, ?, ?, ?, ?)", 
          (libro4.libro_id, libro4.titulo, libro4.autor, libro4.precio, libro4.stock))
c.execute("INSERT OR IGNORE INTO libro (id, titulo, autor, precio, stock) VALUES (?, ?, ?, ?, ?)", 
          (libro5.libro_id, libro5.titulo, libro5.autor, libro5.precio, libro5.stock))
conn.commit()

c.execute("SELECT * FROM usuario")
usuarios = c.fetchall()  
print("Usuarios:")
for usuario in usuarios:
    print(usuario)

c.execute("SELECT * FROM libro")
libros = c.fetchall() 
print("\nLibros:")
for libro in libros:
    print(libro)

conn.close()
