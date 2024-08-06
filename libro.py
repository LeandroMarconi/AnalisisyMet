class libro:
    def __init__(self, libro_id, titulo, autor, precio, stock):
        self.libro_id = libro_id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock

    def get_libro_id(self):
        return self.libro_id

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_precio(self):
        return self.precio

    def get_stock(self):
        return self.stock

    
    def set_libro_id(self, libro_id):
        self.libro_id = libro_id

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_precio(self, precio):
        self.precio = precio

    def set_stock(self, stock):
        self.stock = stock

 
    def mostrar_info(self):
        return f"ID: {self.libro_id}, Título: {self.titulo}, Autor: {self.autor}, Precio: {self.precio}, Stock: {self.stock}"
