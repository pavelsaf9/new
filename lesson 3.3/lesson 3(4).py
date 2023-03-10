creds = ('__init__', '127.0.0.1', 'admin', 'SupermAn', 'ClOwN',
         'http://site.com', 'humorist', 'https://example.com',
         '192.168.12.101', 12345, 'https://yandex.ru')

print('Login:')
print(creds[2], creds[6], sep='\n', end='\n\n')
print('Password:')
print(creds[3], creds[4], sep='\n', end='\n\n')
print('IP:')
print(creds[1], creds[-3], sep='\n', end='\n\n')
print('Host:')
print(creds[5], creds[-4], creds[-1], sep='\n')
