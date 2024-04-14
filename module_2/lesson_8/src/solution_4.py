supply: dict[str, str] = {}
design: dict[str, str] = {}

for i in range(6):
    dept, job, name = input().split(', ')
    if dept == 'Снабжение':
        supply[job] = name
    elif dept == 'Дизайн':
        design[job] = name

print('Снабжение:', supply)
print('Дизайн:', design)