
````markdown
# 🔌 Python Socket Programming

Learn the fundamentals of socket programming in Python using the built-in `socket` module. This project demonstrates how to create a basic client-server communication model.

---

## 🔹 What Is a Socket?

A **socket** is one endpoint of a two-way communication link between two programs running on a network. In Python, the `socket` module provides access to the BSD socket interface, allowing you to create both TCP and UDP connections.

---

## 🔹 Basic Socket Programming Concepts

### 🖥️ Server:

- Binds to an IP and port
- Listens for incoming connections
- Accepts a connection
- Receives data from clients
- Sends data back (optional)

### 📲 Client:

- Connects to a server using IP and port
- Sends data to the server
- Receives data from the server (optional)

---

## 🔹 How It Works

1. The **server** script listens on a specified port.
2. A **client** script connects to that port.
3. Once connected, the client sends a message.
4. The server receives the message and responds.

---

## 🔹 Requirements

- Python 3.x

No external libraries required.

---

## 🔹 Getting Started

### Run the Server

```bash
python server.py
````

### Run the Client (in a new terminal)

```bash
python client.py
```

---

## 🔹 Output Example

**Server:**

```
[*] server host 127.0.0.1       [*] server port 7444
tcp_socket_server Version:v0.1  ctrl + c to stop the server
```

**Client:**

```
Server Response: 
client side successfully connected to the Sever
tcp_server version:v0.1
>>
```

---

## 📁 Files

* `server.py` – Server-side code
* `client.py` – Client-side code

---

## 🔹 What's Next?

* Multi-client handling
* Asynchronous sockets using `asyncio`
* Chat room implementation

---

## 🛠️ Author

Created by \[SRIDHARANITHARAN]

```


