# Microsoft-Windows-cmd.exe-Stack-Buffer-Overflow
Microsoft Windows cmd.exe / Stack Buffer Overflow


Specially crafted payload will trigger a Stack Buffer Overflow in the NT Windows "cmd.exe" commandline interpreter. Requires running an already dangerous file type like .cmd or .bat. However, when cmd.exe accepts arguments using /c /k flags which execute commands specified by string, that will also trigger the buffer overflow condition.

E.g. cmd.exe /c  [PAYLOAD]


[!Demo](https://www.youtube.com/watch?v=wYYgjV-PzD8)
