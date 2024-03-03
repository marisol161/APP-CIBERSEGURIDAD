import subprocess

def add_iptables_rule(rule):
    subprocess.run(["/sbin/iptables", rule])

def delete_iptables_rule(rule):
    subprocess.run(["/sbin/iptables", "-D", rule])

def allow_port_22():
    rule_to_add = "-A INPUT -p tcp --dport 22 -j ACCEPT"
    add_iptables_rule(rule_to_add)
    print("Acceso al puerto 22 permitido.")

def deny_port_22():
    rule_to_add = "-A INPUT -p tcp --dport 22 -j DROP"
    add_iptables_rule(rule_to_add)
    print("Acceso al puerto 22 denegado.")

def main():
    try:
        while True:
            print("\nMenú:")
            print("1. Permitir acceso al puerto 22")
            print("2. Denegar acceso al puerto 22")
            print("3. Salir")

            choice = input("Seleccione una opción: ")

            if choice == "1":
                allow_port_22()
            elif choice == "2":
                deny_port_22()
            elif choice == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.")
    except KeyboardInterrupt:
        print("\nSaliendo del programa debido a la interrupción del teclado.")

if __name__ == "__main__":
    main()
