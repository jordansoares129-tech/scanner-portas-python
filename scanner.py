import socket
from datetime import datetime

def scanner_portas(host, portas):
    print("=" * 50)
    print(f"Scanner iniciado para o host: {host}")
    print(f"Data/Hora: {datetime.now()}")
    print("=" * 50)

    for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        resultado = sock.connect_ex((host, porta))

        if resultado == 0:
            print(f"[ABERTA] Porta {porta}")

        sock.close()

    print("=" * 50)
    print("Scanner finalizado.")
    print("=" * 50)


if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio autorizado: ")

    portas_comuns = [
        21, 22, 23, 25, 53, 80, 110,
        139, 143, 443, 445, 3306, 3389, 8080
    ]

    scanner_portas(alvo, portas_comuns)