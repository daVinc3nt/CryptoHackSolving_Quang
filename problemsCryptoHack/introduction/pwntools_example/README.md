# Write-up for pwntools_example CTF challenge

## Challenge Information
- **Name:** pwntools_example
- **Category:** pwn
- **Source:** https://cryptohack.org/challenges/
- **Description:**
> Several of the challenges are dynamic and require you to talk to our challenge servers over the network. This allows you to perform man-in-the-middle attacks on people trying to communicate, or directly attack a vulnerable service. To keep things consistent, our interactive servers always send and receive JSON objects.
>
> Such network communication can be made easy in Python with the pwntools module. This is not part of the Python standard library, so needs to be installed with pip using the command line pip install pwntools.
>
> For this challenge, connect to socket.cryptohack.org on port 11112. Send a JSON object with the key buy and value flag.
>
> The example script below contains the beginnings of a solution for you to modify, and you can reuse it for later challenges.
>
> Connect at socket.cryptohack.org 11112
>
> Challenge files:
>   - pwntools_example.py
>  You have solved this challenge! View solutions

## Solution Idea
- Analyze the challenge: Requires connecting to a server via TCP, communicating using JSON, and sending the key "buy" with value "flag" to receive the flag.
- Identify the weakness: The server does not require authentication, just send the correct JSON to get the flag.
- Exploitation plan: Use pwntools to connect, send/receive JSON automatically.

## Solution Steps
1. **Connect to the server** using pwntools (remote).
2. **Read the welcome messages** from the server to synchronize communication.
3. **Send the JSON** `{"buy": "flag"}` to the server.
4. **Receive and print the result** (the flag) from the server.

## Exploit Script
The script uses pwntools to automate the flag retrieval process:

```bash
pip install pwntools
python3 exploit.py
```

The result will be a JSON object containing the flag.

## Flag
```
[solved]
```

## Additional Notes
- This script can be reused for similar challenges by changing the HOST, PORT, or JSON data.
- See `notes.md` for experiment notes.
