# general
## What is a network?
A network is a set of devices connected to each other using a physical transmission medium
example : a computer network is a group of computers connected with each other to communicate 
and share information and resources like hardward, data, and software across each otehr.
In a network, nodes are used to connect two or more networks.

## What is network topology
network topology is a physical layout of the computer network.
it defines how the computers, devices, cables and other assets are connected to each other

## What is a Router
A router is a network device which connects two or more network segments
The router is used to transfer information from source to destination
Routers send the information in terms of data packets and when these data packets are forwarded from
one router to another router then the router reads the network address in the packets and identifies
the destination network.

## What are the layer in OSI reference Models?
1. Physical Layer : Physical Layer converts data bits into electrical impulse or radio signals. E.g. Ethernet
2. Data Link Layer : At Data Lnik layer, data packets are encoded and decoded into bits and it provides a node
to node data transfer. Data Link LAyer also detects the errors occurred at Layer 1.
3. Network Layer : Network Layer transfers variable length data seqnece from one node to another node in the same network
This variable length data sequence is also known as "data grams"
4. Transport LAyer : It transfers data between nodes and also provides acknowledgement of successful data transmission.
It keeps track of transmission and sends the segments again if the transmission fails
5. Session Layer : Session Layer manages and controls the connections between computers. It establishes, coordinates,
exchange and terminates the connections between local and the remote applications.
6. Presentation Layer : It is also called as "syntax Layer" Layer 6 transfroms the data into the form in which the
application layer accepts.
7. Applications LAyer : The is the last layer of OSI Reference Mode land is the one which is close to the end user.
Both end-user and application layer interacts with the software application. This layer provides services for email, 
file transfer etc.

## How can a network be certified as an effective network? What are the factors affecting them?
A network can be certified as an effective network based on below-menthioned points:
- Performance : Anetwork's performance is based on its transmitted time and response time. The factors affecting the 
performance of a network are hardware, software, transmission medium types and the number of users using the network.
- Reliability : Reliability is nothing but measuring the probability of failures occurred in a network and the time taken by it torecover from it. The factors affecting the same are the frequency of failure and revoery time from failure.
- Security: Protecting the data from malware and unauthorized users. The factors affecting the security are malware and users who do not have permission to access the network.

# Protocols
## Exaplin the TCP/IP Model
It stands for Transmaission Control Protocol and Internet Protocol and is the most widely used and available protocol.
TCP/IP specifies how data should be packaged, transmitted and routed in their end to end data communicatinos.
It consists of 4 layers:
1. Application layer : This is the top layer in tcp/ip model. It includes processes which use Transport layer protocol to transmit the data to thier destinations. There are differenct application layer protocol such as http, ftp, smtp, snmp protocols etc.
2. Transport layer : it receives the data from the application layer which is above transport layer. it acts as a backbone between the host's system connected with each other and it mainly concerns the transmission of data. tcp and udp are mainly used as a transport layer protocols
3. network or internet layer: this layer sends the packets a cross the network. packets mainly contain source, destination ip addresses and actual data to be transmitted
4. network interface layer: it is the lowest layer of tcp, ip model. it trnasfers the packts between differnect hosts. it includes encapsulation of ip packets into frames, mapping ip addresses to physical hardware devices etc.

## What is http and what port does it use?
http is htpertext transfer protocol and it is responsible for web content. many web pages are using http to transmit the web content and allow the display and navigation of hypertext. it is primary protocol and the default port used is tcp port 80.

## what is https and what port does it use?
https is a secure http. https is sued for encrypted and secure communitaion over a computer network to prevent man in the middle attack and sniffing

in a bi-directional communactions, https protocol encrypts the commmunication so that tapmpering of the data get avoided with the help of a ssl certificate, it verifies if the requested server connection is a valid connection or not. https uses tcp with port 443.

## what is an ip address?
ip address stands for internet protocol address. it is a unique string of numbers used to specify the location of a computer or other device in a network using tcp/it. it is represented by a serice of four decimal numbers, seperated by dots. 


