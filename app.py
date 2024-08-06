from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('libroyenny.db')
        c = conn.cursor()
        c.execute("SELECT * FROM usuario WHERE nombre=? AND passw=?", (username, password))
        user = c.fetchone()
        conn.close()
        
        if user:
            return redirect(url_for('libros'))
        else:
            return redirect(url_for('error'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('libroyenny.db')
        c = conn.cursor()
        c.execute("INSERT INTO usuario (nombre, passw) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/libros')
def libros():
    conn = sqlite3.connect('libroyenny.db')
    c = conn.cursor()
    c.execute("SELECT * FROM libro")
    libros = c.fetchall()
    conn.close()

    return render_template('libros.html', libros=libros)

@app.route('/update_stock', methods=['POST'])
def update_stock():
    libro_id = request.form['libro_id']
    cantidad = int(request.form['cantidad'])

    conn = sqlite3.connect('libroyenny.db')
    c = conn.cursor()
    c.execute("SELECT stock, titulo, precio FROM libro WHERE id=?", (libro_id,))
    libro = c.fetchone()
    stock_actual = libro[0]
    titulo = libro[1]
    precio = libro[2]
    
    if stock_actual >= cantidad:
        nuevo_stock = stock_actual - cantidad
        c.execute("UPDATE libro SET stock=? WHERE id=?", (nuevo_stock, libro_id))
        conn.commit()
        conn.close()

        total_venta = cantidad * precio

        return redirect(url_for('ticket', titulo=titulo, cantidad=cantidad, total_venta=total_venta))
    else:
        conn.close()
        return "No hay suficiente stock para completar la venta."

@app.route('/ticket')
def ticket():
    titulo = request.args.get('titulo')
    cantidad = request.args.get('cantidad')
    total_venta = request.args.get('total_venta')
    
    return render_template('ticket.html', titulo=titulo, cantidad=cantidad, total_venta=total_venta)

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
