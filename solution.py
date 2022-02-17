from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    #gmailAddress = "smtp.gmail.com"
    #mailServerAddress = "127.0.0.1"
    #port = 1025
    mailserver = (mailserver, port)
    clientSocket = socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(mailserver)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfromCmd = 'MAIL FROM:<fakeEmail@test.com>\r\n'
    clientSocket.send(mailfromCmd.encode())
    recv2=clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpttomCmd = 'RCPT TO:<hannah@thompsonmail.org>\r\n'
    clientSocket.send(rcpttomCmd.encode())
    recv3=clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCMD = 'DATA\r\n'
    clientSocket.send(dataCmd.encode())
    recv4=clientSocket.recv(1024).decode() #should be 354?
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5=clientSocket.recv(1024).decode() #should be 250
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCmd = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv6=clientSocket.recv(1024).decode()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
