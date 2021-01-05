# Doorbell
Simple doorbell client/server

Server based in web sockets written in python
Client is an android app written in flutter

# How it works:

Client has to input server ip/port on the app in order for it to work

Server is started on linux/windows boot and rests in background. Whenever the client sends a "beep" a doorbell sfx plays in speakers in the computer.
Client will use the android/ios app to ring the bell

# Goals: 

[x] Develop barebone server
[x] Develop barebone client
[x] Client can ring the server
[ ] Client can see if the server is online offline
[ ] Client can only ring the server if is close enough
[ ] Client can send a message to server and play it via text to speech


