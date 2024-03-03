from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

def permitir_ssh(ip_destino):
    comando = f"/sbin/iptables -D INPUT -p icmp -s {ip_destino} -j DROP"
    ejecutar_comando(comando)

def denegar_ssh(ip_destino):
    comando = f"/sbin/iptables -A INPUT -p icmp -s {ip_destino} -j DROP"
    ejecutar_comando(comando)

def ejecutar_comando(comando):
    # Verificar si el usuario actual es root
    if os.geteuid() != 0:
        comando = f"sudo {comando}"
    subprocess.run(comando, shell=True)

@app.route('/')
def index():
    return render_template('resultado.html')

@app.route('/control_ssh', methods=['POST'])
def control_ssh():
    ip_destino = request.form['ip_destino']
    accion = request.form['accion']
    
    if accion == "permitir":
        permitir_ssh(ip_destino)
        mensaje = "Se ha permitido el acceso SSH desde la dirección especificada."
    elif accion == "denegar":
        denegar_ssh(ip_destino)
        mensaje = "Se ha denegado el acceso SSH desde la dirección especificada."
    else:
        mensaje = "Entrada no válida. Por favor, ingresa 'permitir' o 'denegar'."
    
    return render_template('resultado.html', mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)