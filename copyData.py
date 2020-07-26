SECTOR_SIZE = 512
BACKUP_DRIVE = r'\\.\PhysicalDrive2'
DATA_DRIVE = r'\\.\PhysicalDrive3'

count = 0
while count < 10:
	with open(DATA_DRIVE, 'rb+') as dataDrive:
		data = dataDrive.read(SECTOR_SIZE)
		with open(BACKUP_DRIVE, 'rb+') as backup:
			backup.write(data)
	count+=1