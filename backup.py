import subprocess

db_name = 'test'
collection = 'employees'
host = "localhost"
port = 27017
backup_dir = "/Users/Sarthak.Deshpande/Excercises"
cmd = f"mongodump --port={port} --host={host} --db={db_name} --collection={collection} --out={backup_dir}"

subprocess.run(cmd, check=True, shell=True)