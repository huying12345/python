import zipfile

f = zipfile.ZipFile('D:\\Candy\\', 'w', zipfile.ZIP_DEFLATED)
f.write('D:\\Candy\\其他\\greeter.js')
f.close()
