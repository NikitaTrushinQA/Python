
units = {'B': 1, 'KB': 1024, 'MB': 1048576,'GB': 1073741824 }

def bytesize_to_str(filesize):
   if filesize < units['KB']:
      return f' {filesize} B'
   if filesize < units['MB']:
      return f' {round(filesize / units["KB"])} KB'
   if filesize < units['GB']:
      return f' {round(filesize / units["MB"])} MB'
   else:
      return f' {round(filesize / units["GB"])} GB'

#print(bytesize_to_str(1048576))
