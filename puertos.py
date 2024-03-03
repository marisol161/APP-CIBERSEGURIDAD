from tkinter import Canvas
from flask import Flask, request, render_template
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import nmap
import platform
import subprocess

app = Flask(__name__)

def scan_ports(host):
    nm = nmap.PortScanner()
    results = nm.scan(hosts=host, arguments="-sT -n -Pn -T4")
    return nm

def ping(host):
    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', parametro, '1', host]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return resultado.stdout

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        host = request.form["host"]
        nm = scan_ports(host)
        puertos_abiertos = ""
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                puertos_abiertos += f"port : {port}\tstate : {nm[host][proto][port]['state']}\n"

        ping_resultado = ping(host)
        return render_template("puertos.html", host=host, state=nm[host].state(), puertos_abiertos=puertos_abiertos, ping_resultado=ping_resultado)
    
    return render_template("puertos.html")

def generar_pdf(resultados):
    c = Canvas.Canvas("resultados_escaneo.pdf", pagesize=letter)
    c.drawString(100, 750, "Resultados del escaneo para {}".format(resultados['host']))
    c.drawString(100, 730, "Estado: {}".format(resultados['state']))
    c.drawString(100, 710, "Puertos abiertos:")
    c.drawString(120, 690, resultados['puertos_abiertos'])
    c.drawString(100, 670, "Ping enviado a {}: {}".format(resultados['host'], resultados['ping_resultado']))
    c.save()

if __name__ == "__main__":from tkinter import Canvas
from flask import Flask, request, render_template
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import nmap
import platform
import subprocess

app = Flask(__name__)

def scan_ports(host):
    nm = nmap.PortScanner()
    results = nm.scan(hosts=host, arguments="-sT -n -Pn -T4")
    return nm

def ping(host):
    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', parametro, '1', host]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return resultado.stdout

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        host = request.form["host"]
        nm = scan_ports(host)
        puertos_abiertos = ""
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                puertos_abiertos += f"port : {port}\tstate : {nm[host][proto][port]['state']}\n"

        ping_resultado = ping(host)
        return render_template("puertos.html", host=host, state=nm[host].state(), puertos_abiertos=puertos_abiertos, ping_resultado=ping_resultado)
    
    return render_template("puertos.html")

def generar_pdf(resultados):
    c = Canvas.Canvas("resultados_escaneo.pdf", pagesize=letter)
    c.drawString(100, 750, "Resultados del escaneo para {}".format(resultados['host']))
    c.drawString(100, 730, "Estado: {}".format(resultados['state']))
    c.drawString(100, 710, "Puertos abiertos:")
    c.drawString(120, 690, resultados['puertos_abiertos'])
    c.drawString(100, 670, "Ping enviado a {}: {}".format(resultados['host'], resultados['ping_resultado']))
    c.save()

if __name__ == "__main__":
    app.run(debug=True)

    app.run(debug=True)
