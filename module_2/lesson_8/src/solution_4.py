supply: dict[str, str] = {}
design: dict[str, str] = {}

data = [
'Снабжение Менеджер Иванов',
'Дизайн Дизайнер Смирнов',
'Снабжение Менеджер Петров',
'Дизайн Иллюстратор Cидоров',
'Маркетинг Аналитик Сергеев',
'Дизайн Дизайнер Васильев'
]

for string in data:
    dept, job, name = string.split()
    if dept == 'Снабжение':
        supply[job] = name
    elif dept == 'Дизайн':
        design[job] = name

print('Снабжение:', supply)
print('Дизайн:', design)