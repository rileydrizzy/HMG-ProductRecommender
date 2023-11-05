import subprocess
COMMAND = [
    "kaggle",
    "competitions",
    "files",
    "-c",
    "h-and-m-personalized-fashion-recommendations",
]
r = subprocess.run(COMMAND, check= False, capture_output= True, text =True)

with open('new.txt', 'w', encoding= 'utf-8') as file:
    file.write(r.stdout)
