from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

def permitir_ssh(mac_address):
    comando = f"iptables -D INPUT -m mac --mac-source {mac_address} -j DROP"
    ejecutar_comando(comando)

def denegar_ssh(mac_address):
    comando = f"iptables -A INPUT -m mac --mac-source {mac_address} -j DROP"
    ejecutar_comando(comando)

def ejecutar_comando(comando):
    # Verificar si el usuario actual es root
    if os.geteuid() != 0:
        comando = f"sudo {comando}"
    subprocess.run(comando, shell=True)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/control_mac', methods=['POST'])
def control_mac():
    mac_address = request.form['mac_address']
    action = request.form['action']
    
    if action == "permitir":
        permitir_ssh(mac_address)
        mensaje = "Se ha permitido el acceso por MAC desde la dirección especificada."
    elif action == "denegar":
        denegar_ssh(mac_address)
        mensaje = "Se ha denegado el acceso por MAC desde la dirección especificada."
    else:
        mensaje = "Entrada no válida. Por favor, selecciona 'permitir' o 'denegar'."
    
    return render_template('formulario.html', mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
