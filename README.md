Descrição:
Script em Python que coleta informações de múltiplos servidores Linux e Windows (hostname, versão do kernel, uptime, versão do Windows etc.) usando paramiko e winrm.
Foi criado um arquivo separado de hosts para permitir editar os alvos sem alterar o código.

Tecnologias: Python, Paramiko, WinRM, SSH, Windows Remote Management

Funcionalidades:

Leitura dinâmica de hosts via arquivo TXT

Conexão automática com Linux e Windows

Execução remota de comandos

Geração de arquivo de inventário com timestamp

Tratamento de erros integrado
