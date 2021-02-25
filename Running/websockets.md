# How websockets differ from HTTP
## Why websockets exist
- Websockets were created to solve an issue with services that required bi-directional communications between a client and a server. Meaning, send update, get update. For example, a chat service.
- Before websockets, HTTP was used to create a "bi-directional" communication between client and server by establishing multiple ports and then performing constant polls on these established communications. This added excessive stress on the systems because much of the polls were practically useless considering that not every packet is going to have an update. 
- For ease of adoption, websockets works over the HTTP standard ports of 80 and 443
- Although the protocol works over these standard HTTP ports it is important to note that the pattern of communications does not entirely match those of HTTP, naturally. So when sniffing on these comms it may look odd

### A Typical websocket handshake
```
# Client
        GET /chat HTTP/1.1
        Host: server.example.com
        Upgrade: websocket
        Connection: Upgrade
        Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
        Origin: http://example.com
        Sec-WebSocket-Protocol: chat, superchat
        Sec-WebSocket-Version: 13
# Server
        HTTP/1.1 101 Switching Protocols
        Upgrade: websocket
        Connection: Upgrade
        Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
        Sec-WebSocket-Protocol: chat
```
- Once a successful handshaked is made, the client and server are free to send "messages" at will instead of the client initiating every communication
- A websocket "message" could be made up of one or more frames

## Resources
[RFC6455 - Websockets](https://tools.ietf.org/html/rfc6455)
[Websockets VS HTTP](https://medium.com/platform-engineer/web-api-design-35df8167460)
