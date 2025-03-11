from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()

process = rwm.get_process_by_name("Tutorial-i386.exe")

process.open()


baseaddress = 0x400000+0x019AFD98

healthpointer = process.get_pointer(baseaddress, offsets=[0x264,0x714,0x76C,0x2DC,0x18,0x14,0x4B0])

while 1:
    value = process.read(healthpointer)
    print(value)
