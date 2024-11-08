from flask import Flask

app = Flask(__name__)

def calcular_factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

@app.route('/factorial/<numero>')
def factorial(numero):
    try:
        numero = int(numero)
    except ValueError:
        return "Numero no válido", 400
    
    if numero < 0:
        return "Numero no válido", 400
    
    result = calcular_factorial(numero)
    return f"El factorial de {numero} es {result}"

if __name__ == '__main__':
    app.run(debug=True)