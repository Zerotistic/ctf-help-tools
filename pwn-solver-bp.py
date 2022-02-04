from pwn import *

ip = '127.0.0.1'
port = 8000

gdbscript = """b *main"""

io = gdb.debug('./path',gdbscript=gdbscript)
#io = process('./path')
#io = remote(ip,port)

padding = b"A"*0
exploit = p64(0x00000001)

payload = padding + exploit

io.sendline(payload)
io.interactive()