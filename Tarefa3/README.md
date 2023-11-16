# Trabalho com UDP

## O Protocolo UDP
Neste trabalho iremos explorar a implementação de uma aplicação rodando sobre UDP através da programação com sockets. Este trabalho tem a finalidade de trazer o conhecimento de programação e funcionamento básico do protocolo UDP, principalmente comparando o UDP com os serviços que o TCP fornece para a camada de aplicação. Baseado no primeiro trabalho, mas agora transformando o anterior em um Servidor UDP simplificado.

### Fluxo do trabalho:
- Procurar um código “Hello word” usando servidor UDP e seu cliente.
    - Este trabalho pode ser realizado em qualquer linguagem de programação, a escolha do aluno, mas lembre-se: não pode ser usado bibliotecas que manipulem o UDP, e sim usar o UDP diretamente através da criação e manipulação dos sockets.
- Servidor UDP (deve executar antes do cliente)
    - Escolher um porta para comunicação (maior que 1024)
    - Na recepção de dados :
        - Tratar esses dados (requisição necessária - propor o seu próprio protocolo para substituir o HTTP )
        - Ex.: GET /arquivo
        - Transmitir o arquivo requisitado pelo cliente (deve ser grande)
            - Dividir o arquivo em pedaços (tamanho do buffer)
            - Qual o tamanho do buffer?
            - Buffer cliente e servidor devem ser iguais?
            - O valor do MTU influencia?
            - Para que colocar checksum?
            - Preciso numerar os pedaços?
            - Se o arquivo não existir, como aviso o cliente?
- Cliente UDP (deve executar depois do servidor)
    - Colocar o endereço da máquina e porta escolhida para o servidor
        - @ip do servidor:(Porta servidor)/arquivo
    - Requisitar um arquivo
    - Dar a opção ao usuário (Professor) para descartar uma parte do arquivo
        - Para simular a perda de dados e testar o mecanismo de recuperação de dados proposto pelo aluno.
    - Receber, montar e conferir (checksums) o arquivo recebido do servidor
    - Se arquivo OK:
        - Apresentar o arquivo requisitado
    - Se arquivo não OK
        - Verificar quais pedaços faltam e pedir para re-enviar.
        - Interpretar ERROS.
            - Ex.: Arquivo não encontrado etc.
            
> [! IMPORTANT]
> Para agilizar a verificação de integridade são utilizadas somas de verificação (checksums) ou resumos criptográficos como o MD5 e SHA.