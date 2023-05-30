def find_missing_addresses(wallet_file, target_file, output_file):
    # Чтение адресов кошельков из файла wallets.txt
    with open(wallet_file, 'r') as f:
        wallets = {line.strip() for line in f.readlines()}

    # Чтение целевых адресов из файла 2wall.txt
    with open(target_file, 'r') as f:
        target_wallets = {line.strip() for line in f.readlines()}

    # Поиск адресов, которых нет в файле 2wall.txt
    missing_addresses = list(wallets - target_wallets)

    # Запись найденных адресов в файл final.txt
    with open(output_file, 'w') as f:
        f.write('\n'.join(missing_addresses))


# Укажите названия файлов
wallet_file = 'wallets.txt'
target_file = '2wall.txt'
output_file = 'final.txt'

# Вызов функции для поиска и записи отсутствующих адресов
find_missing_addresses(wallet_file, target_file, output_file)