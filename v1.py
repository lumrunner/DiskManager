import json

SECTOR_SIZE = 512
DRIVE = r'\\.\PhysicalDrive3'


def addStr(i):
    '''for list of strings to be made into hex'''
    if i == '0':
        i == '00'

    return i

class partition():
    '''a partition of a hard drive'''

    def __init__(self, mbr):
        '''initializing the partitions'''
        self.active = str(mbr[0])
        self.startHead = str(mbr[1])
        self.startSector = str(mbr[2])
        self.startCylinder = str(mbr[3])
        self.ID = str(mbr[4])
        self.endHead = str(mbr[5])
        self.endSector = str(mbr[6])
        self.endCylinder = str(mbr[7])
        self.sectorsBefore = [str(mbr[8]), str(mbr[9]), str(mbr[10]), str(mbr[11])]
        self.numSectors = [str(mbr[12]), str(mbr[13]), str(mbr[14]), str(mbr[15])]

    def get_partition_type(self):
        '''returns the volume format of the partition'''
        return self.ID

class mbr():
    '''a container for a mbr sector'''
    def __init__(self, boot, part0, part1, part2, part3):
        '''initializing the mbr'''
        self.end = 0x55aa
        self.partitions = [part0, part1, part2, part3]
        self.boot = boot[0:0x1BE].hex()
        print(self.boot)

    def getHex(self):
        '''returns the hex representation of the mbr'''
        h = []
        for entry in range(0, 0x1BE*2, 2):
            entryHex = str(self.boot[entry]) + str(self.boot[entry + 1])
            h.append(entryHex)
       
        for part in self.partitions:
            h.append(part.active)
            h.append(part.startHead)
            h.append(part.startSector)
            h.append(part.startCylinder)
            h.append(part.ID)
            h.append(part.endHead)
            h.append(part.endSector)
            h.append(part.endCylinder)
            for entry in part.sectorsBefore:
                h.append(entry)
            for entry in part.numSectors:
                h.append(entry)

        h.append(str(0x55))
        h.append(str(0xaa))
        print(h)
        return h
    
possible_drives = [
    r'\\.\PhysicalDrive0',
    r'\\.\PhysicalDrive1',
    DRIVE]

with open('mbr.dat', 'rb') as goodMBR:
    goodMBR.seek(0) #ensuring to start at beginning of file
    goodBoot = goodMBR.read(SECTOR_SIZE)

with open(DRIVE, 'rb+') as disk:
    disk.seek(0)
    diskMBR = disk.read(SECTOR_SIZE)

partID = [ diskMBR[0x1C3], diskMBR[0x1D3], diskMBR[0x1E3], diskMBR[0x1F3]]
part0 = partition(diskMBR[0x1BE:0x1CE])
part1 = partition(diskMBR[0x1CE:0x1DE])
part2 = partition(diskMBR[0x1DE:0x1EE])
part3 = partition(diskMBR[0x1EE:0x1FE])

#maybe do some edits to the partitions?

newMBR = mbr(goodBoot, part0, part1, part2, part3)
how = newMBR.getHex()
with open('temp.txt', 'wb') as tempFile:
    for entry in how:
        tempFile.write(bytes().fromhex(entry))

with open('temp.txt', 'rb') as tempFile:
    tempFile.seek(0)
    finalMBR = tempFile.read(SECTOR_SIZE)
#print(finalMBR.hex())

repairedDrive = open(DRIVE, 'rb+')
repairedDrive.seek(0)
#repairedDrive.write()
repairedDrive.close()