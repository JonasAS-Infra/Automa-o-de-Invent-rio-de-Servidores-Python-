#inventario

import paramiko
import winrm
from datetime import datetime

# ----------------------------
# Função: Lê uma lista de hosts de um arquivo txt
# ----------------------------

def carregar_hosts(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        linhas = f.readlines()
        return [linha.strip() for linha in linhas if linha.strip()]
    

# ----------------------------
# Função: Coletar inventário de servidores Linux
# ----------------------------

def coletar_linux(host):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username="svc_inventory", password="sVc.321",timeout=5)
        comando = """
        hostname
        uname -r
        uptime -p
        """
        stdin, stdout, stderr = ssh.exec_command(comando)
        saida = stdout.read().decode().strip()
        
        ssh.close()
        
        return f"[LINUX] {host}:\n{saida}\n"
    
    except Exception as e:
        return f"[LINUX] {host}: ERRO -> {e}\n"
    

# ----------------------------
# Função: Coletar inventário de servidores Windows
# ----------------------------

def coletar_windows(host):
    try:
        sess = winrm.Session(host,auth=('svc_inventory','sVc.321'))
        comando = "hostname && ver"
        resposta = sess.run_cmd(comando)
        saida = resposta.std_out.decode().strip()
        return f"[WINDOWS] {host}:\n{saida}\n"
    
    except Exception as e:
        return f"[WINDOWS] {host}: ERRO -> {e}\n"
    
# ----------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------

def main():
    print("=== Iniciando coleta... ===\n")
    hosts_linux = carregar_hosts("hosts_linux.txt")
    hosts_win = carregar_hosts("hosts_win.txt")
    
    resultados = []
    
    for host in hosts_linux:
        print(f"Coletando Linux -> {host}")
        resultados.append(coletar_linux(host))
        
    for host in hosts_win:
        print(f"Coletando Windows -> {host}")
        resultados.append(coletar_windows(host))
        
    nome_log = f"inventario_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt"
    
    with open(nome_log, "w") as arquivo:
        arquivo.write("\n".join(resultados))
        
        print(f"\nColeta finalizada! Arquivo gerado: {nome_log}") 
        
# ----------------------------
# Executa o script
# ----------------------------

if __name__ == "__main__":
    main()
    

                
        

    