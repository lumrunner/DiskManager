DRIVE = r'\\\\.\\PhysicalDrive2'

#get drive geometry here, just put in some values for now
driveSize = 16 * 1000000000
sectorSize = 512
blockSize = 8
writeSize = sectorSize * blockSize
disk = driveSize / writeSize

zeros = []
ones = []
num = (4) * 2 - 1

#create a erasing sector, one of zeros and one of ones 
for i in range(0, writeSize):
     zeros.append(0x00)
     ones.append(0xFF)

#magic happens below :)
count = 0
with open(DRIVE, 'rb+') as file:
     while count < num:
          if count % 2 == 0:
               for sector in disk:
                    file.seek(sector)
                    file.write(zeros)
          else: 
               for sector in disk:
                    file.seek(sector)
                    file.write(ones)
          count += 1
