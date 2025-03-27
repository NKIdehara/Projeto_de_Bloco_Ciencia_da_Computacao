import subprocess

host = "192.168.1.181"
saida = subprocess.run(["nmap", "-sV", host], capture_output=True, text=True, check=True)
for linha in saida.stdout.split("\n"):
    print(linha)
