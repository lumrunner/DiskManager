SECTOR_SIZE = 512
BACKUP_DRIVE = r'\\.\PhysicalDrive2'
DATA_DRIVE = r'\\.\PhysicalDrive3'

count = 0
with open(DATA_DRIVE, 'rb+') as dataDrive:
	with open(BACKUP_DRIVE, 'rb+') as backup:
		for count in range(0, 100000):
			backup.seek(SECTOR_SIZE * count)
			data = dataDrive.read(SECTOR_SIZE)
			backup.write(data)