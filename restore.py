import subprocess
host = 'localhost:27017'
port = 27017
db_name = 'test'
collection = 'employees'
file = '/Users/Sarthak.Deshpande/Excercises/test/employees.metadata.json'
restore_cmd = f"mongoimport --db={db_name} --collection={collection} --host={host} --file={file}"
subprocess.run(restore_cmd, check=True, shell=True)