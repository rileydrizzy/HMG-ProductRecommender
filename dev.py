import subprocess
COMMAND = [
    "kaggle",
    "competitions",
    "files",
    "-c",
    "h-and-m-personalized-fashion-recommendations",
]
#COMMAND[6] =  'images/'  #'images/010/0108775015.jpg' #"sample_submission.csv"
#COMMAND[-1] = 'dev_data'
r = subprocess.run(COMMAND, check= False, capture_output= True, text =True)

with open('new.txt', 'w', encoding= 'utf-8') as file:
    file.write(r.stdout)
