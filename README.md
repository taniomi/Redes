# Redes de Computadores 

### Tarefa 1 | TCP - Transmission Control Protocol
Implementation of TCP connection with python and socket module.

![TCP Socket Basic Diagram intended for this project. Client and server establish connection with handshake, data is sent to and fro the server and the client. Client sends an end message and server closes the connection.](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg)

### Tarefa 2 | TCP & HTTP
Implementação baseada na Tarefa 1, com servidor que serve arquivos HTML e imagens.

### Tarefa 3 | UDP - User Datagram Protocol 
Implementação de cliente e servidor UDP. Servidor deve enviar arquivos e separá-los em *batches*.

Deve-se definir o tamanho do *buffer* do servidor e do cliente.

Servidor deve ter *checksum*.

Cliente deve ser capaz de descartar partes do arquivo, para simular perda de dados e testar mecanismo de recuperação de dados.
Cliente deve receber, montar e conferir o *checksum* do arquivo recebido do servidor.
