#Yareli Vergara
#November 20th
#Pokemon Evolution Game

#Initialize
pokemon_level = 0
pokemon_name = "Egg"
import random


#Functions
def draw_Charizard1(): #Image used for evolutions - stage 1
    print ("""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣛⣫⣭⣭⣭⡵⣶⢶⣦⣭⣭⣭⣛⣻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢯⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣭⣶⢾⣻⢯⣟⡷⣯⢿⡽⣯⣟⣾⣳⢯⣷⣻⣽⣻⢷⡾⣭⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣥⢛⣼⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣡⣾⣟⡷⣯⢿⣽⣻⢾⡽⣯⢿⣽⣳⣟⡾⣽⣻⢾⡷⣯⣟⣯⣟⣷⣻⣟⣮⣝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⢏⢞⡹⣙⢯⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣵⣟⣯⢷⣯⢿⣽⣻⢾⡽⣯⢿⣽⣻⣞⡷⣯⣟⡷⣯⢿⣽⣳⣟⡾⣽⣞⣷⣻⢾⣽⣳⣌⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠯⣜⠪⣵⣩⡖⣭⠲⢭⢿⣿⣿⣿⣿⣿⣿⡹⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣵⣻⢾⡽⣞⡿⣞⡿⣾⡽⣯⢿⣽⣻⣞⡷⣯⣟⡷⣯⢿⣽⣻⣞⡷⣯⣟⣷⣻⢾⣽⣻⣞⡷⣯⢷⣎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⠴⣫⢷⣯⣟⢦⡛⡜⣎⢻⣙⢻⡻⣿⣿⣧⠳⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣾⢯⣟⣯⠿⣽⡽⣯⡽⣾⡽⣯⣟⣾⣳⢯⣟⡷⣯⢿⣽⣻⣞⡷⣯⣟⣷⣻⢾⣽⣻⣞⡷⣯⢿⡽⣻⣞⡷⡜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣬⢳⣡⢛⡶⣹⣾⣷⣯⡜⡥⢎⣧⣱⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⡿⣞⣟⡾⣽⣻⢷⣻⣳⣟⣷⣻⣳⣟⡾⣽⣻⢾⡽⣯⣟⣾⣳⢯⣟⣷⣻⢾⣽⣻⣞⢷⣫⣽⣞⣯⠟⣃⣙⡻⢽⣮⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⢦⡓⣾⣿⣿⣷⣿⣾⣟⣷⣽⣻⣞⣷⣻⣞⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣯⢟⡽⣾⢽⣳⢯⣟⣳⡽⣞⣳⢯⡷⣾⣽⣳⢯⡿⣽⣳⣟⡾⣽⣛⡾⣧⣟⣯⣞⣷⣫⣟⣷⣻⡌⣿⢠⣤⡄⠙⢦⡹⣧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣣⡝⣹⠿⡿⢿⣟⣿⣿⣿⣿⣳⣟⣾⣷⣯⢿⡽⣎⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⣟⡾⢯⣟⣳⢯⣯⢟⣾⣳⠿⣽⣫⢿⡽⣞⣳⢯⡿⣽⣳⣟⢾⣽⣳⢯⣟⡷⣛⣮⣟⣶⣻⠾⣵⢯⣟⡷⠸⣿⠇⢀⠀⠹⣜⣧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⣋⢟⣿⣿⣷⡿⣱⢛⡾⣽⢾⣻⣷⣿⣿⣿⣿⣞⣯⡿⣝⣮⠹⣜⡹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣛⣾⢻⡾⣽⣛⣾⢻⣮⢟⣽⣳⢯⢛⣩⠴⠒⠀⠀⣁⠛⠾⣙⢾⣭⣟⡾⣽⢯⢷⣻⣼⣳⢿⡽⣫⢾⡽⡇⠀⠀⠀⠈⠠⠹⡜⡎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣍⣎⣶⣿⣟⠳⣥⢫⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣻⡔⣣⠟⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣷⡻⣞⣯⠷⣯⡽⣞⣟⣞⢿⣺⡝⣱⡟⠁⠀⠀⠀⣾⣿⣿⣦⠈⢿⣞⣵⣻⡽⣞⣯⢷⣳⢯⡟⣾⢽⣫⣽⢻⡀⠄⡠⠠⡀⣇⢻⢸⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⢬⣻⣶⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣽⣾⣳⠿⣜⡱⢎⡵⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢗⣯⣽⡳⣏⣿⢳⣻⡽⣞⣭⣟⡳⣸⡿⠀⠀⠀⢀⠀⠹⢿⣿⠿⠀⠀⠹⣞⡷⢯⣛⡾⣝⣯⠾⣝⣮⢳⡝⣮⢟⣳⡘⣤⢣⣜⣿⠙⣮⣝⢮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡎⡵⣋⠞⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣻⣦⡙⣎⢶⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣳⣳⢿⣹⣞⢯⣷⢫⣟⣮⡽⢣⣿⡃⠀⢀⠠⠀⠐⠀⠀⠀⠀⠀⠂⠄⠹⣽⢯⣻⣝⣯⣞⢯⡷⣞⡯⢿⣭⣟⢳⡷⣌⣛⣋⡭⣞⣳⢮⣳⢻⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡖⡭⣚⡿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡗⣬⢫⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣗⣯⣞⢷⣭⡟⣞⡿⣼⣳⣻⢸⣿⡇⠀⠄⡀⠀⠀⠠⠀⡀⠄⣀⠱⡈⢆⢻⡽⣳⣞⣳⣞⡯⢷⢯⡽⣝⡶⢯⣻⣼⢳⣏⡷⣻⣝⣮⢷⣫⡟⣾⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠰⣇⣻⡽⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣯⣿⣿⣿⣿⡿⡱⢎⡵⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣞⣞⢾⣫⢾⣝⣻⣼⢳⣳⢯⢸⣿⡇⡈⠔⣀⠠⠈⠄⡐⢀⠢⢄⣷⡜⣢⠸⣟⡵⣯⣳⠾⣽⣫⢯⡽⣞⡽⣏⡷⣞⢯⡾⣹⡗⣮⢷⣫⠷⣽⢳⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣙⢎⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⡶⣳⠹⣜⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣟⣮⡟⣵⡻⣞⢧⡯⣟⢧⡿⡘⣿⣷⢈⠖⣤⣧⡘⡰⣀⠣⡜⣼⡿⡧⢁⣾⡽⡽⢶⣏⡿⣣⠿⣭⢷⣫⡽⣞⡽⣞⢯⣞⢷⣹⢏⣾⢳⣻⡭⣷⡃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢎⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢯⠷⣭⣷⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣟⣶⢻⣳⣻⢭⡟⣾⢭⣻⢼⣣⡘⠿⣧⡉⢿⣿⣿⣷⢾⣷⠿⢛⣩⢶⡻⢧⣻⡽⣻⡼⡳⠏⢛⡉⢌⠡⡁⢆⠰⡀⢆⢨⡍⣡⣟⢾⣹⢧⣻⢶⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠵⣫⢿⣿⣿⠟⣿⣿⣿⣿⣿⡿⢟⠿⢿⣛⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡞⣽⣣⢯⣟⡞⣧⡻⣜⢧⡳⣝⢯⡖⣮⢥⣤⣤⡬⣶⢲⣏⡿⣹⢾⣹⢯⡳⢙⢡⠰⢤⡉⢖⡌⡒⢆⡑⠌⢆⡱⢌⠒⣰⠿⣼⣫⢞⣳⡽⡎⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣓⢮⡱⣌⠻⣔⣻⣟⣫⣿⣱⢯⣟⡾⣽⣞⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢟⣧⣟⣳⢾⣹⢧⡻⣜⢧⡻⣜⢧⡻⣜⢯⣞⡵⢯⣳⡟⣼⣝⢯⡾⢉⠅⣆⠣⢎⡱⢦⡙⢮⢜⡹⡜⣬⢓⡐⠆⢎⣰⢯⡟⣵⣫⢯⢷⡹⣼⣿⣿⡿⠿⣻⢭⢹⠿⢿⣿⣱⣭⠳⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣟⡾⣽⣳⢾⡽⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣷⢺⡽⣞⢧⡟⣵⢯⡞⣵⣫⣞⣳⢯⣻⠼⣏⡿⣱⣻⠳⠞⣋⣶⢈⠞⣤⠛⣬⢣⠧⣙⢎⡞⣱⢚⡴⡩⢞⡈⡴⣯⢳⢯⣳⣭⢟⡮⣵⣿⣿⢏⡞⡇⢧⢻⡰⢻⢸⢰⣍⢿⣷⡝⣿⠎⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣽⡳⣯⢯⣟⣅⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡘⡿⣜⣯⣛⡾⣝⡾⣹⢧⡷⣹⢮⣗⢯⣻⡝⣾⢳⡽⣛⣆⠭⣉⠎⡞⣤⠛⣤⢣⡛⡜⢮⡜⣥⢋⠶⣙⢎⡼⡽⣞⢯⣛⡶⣽⢚⣼⡿⣋⡵⣏⠞⣭⢋⠶⣩⢏⡶⢸⣿⣦⡻⢣⡖⣯⡝⣯⢖⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣶⣻⣳⡟⣾⡽⣸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡘⢽⡖⣯⣳⢻⡼⣏⡷⣽⢫⡷⣞⢯⡶⣻⠵⣯⣳⢟⣞⣳⡈⢞⡱⢢⡛⣤⢣⡝⠼⣡⠞⣔⢫⢞⡱⣾⣹⢳⣏⢯⡳⠝⠠⣚⡭⣼⡙⢶⣉⠞⡴⢋⡳⡱⢮⢡⣧⢻⣿⢡⠷⣙⠦⣽⣮⣝⢲⡝⣮⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⡷⣏⣷⣛⣧⢿⡅⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⠧⣟⣭⢷⡻⣼⢳⣏⢷⣛⣮⢷⣫⢟⣵⣫⢾⣹⢞⡽⣦⣑⠣⡕⡎⢶⡘⢧⢣⠝⣨⡵⣞⡽⣖⢯⠷⣚⠥⣃⠼⣍⡳⣙⢦⡙⢦⡙⢮⡱⢋⠶⣙⢦⣿⣿⡰⣥⢫⠞⣭⣃⣿⣯⢿⣳⣝⢲⡝⣎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣹⢶⣛⡾⡽⣶⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡚⠧⢿⣱⡟⣮⢟⣮⢳⣏⡾⣽⢲⣏⢷⣫⠾⣝⡶⣏⡷⢶⣩⣤⣭⡬⣖⢯⢷⡹⢎⡳⢭⡚⢜⡤⢳⣍⠳⣎⠵⣩⠖⡹⢦⡙⢦⡹⢍⡞⣡⣿⣿⣿⣧⢣⢯⡹⢲⡱⡜⣯⣟⡿⣞⡎⣞⡱⢦⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⡽⣞⡽⣳⢿⣱⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣔⡹⢌⠯⣜⢫⢞⡱⢏⠷⡞⢯⠞⣯⡝⣾⢱⣏⢯⣓⡳⢎⡵⢫⢞⡲⢭⠋⣓⡁⡄⠯⣜⢣⢎⡳⡌⡳⢥⢚⡵⢣⡝⣲⡙⢎⣼⣿⣿⡿⢟⡫⢥⢣⣏⢳⡹⠼⣌⡛⡽⢏⡳⡬⣝⢣⠏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣳⢯⣽⣛⡾⣭⠏⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣭⣐⡋⠸⠍⠞⣜⢣⡛⡴⣙⠦⣏⢼⠲⣍⠞⣭⢚⡝⡪⢝⢦⢯⡵⣻⢼⢦⣈⠳⡊⣵⣾⠑⣵⡇⢚⠱⣎⠵⣉⣾⡿⢟⢭⡚⣥⢛⡬⢧⡘⢧⣙⢧⡹⣜⣱⢫⡕⡳⢼⡩⢞⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⢧⡟⣶⢏⡷⣏⡇⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣟⣛⣭⡥⣖⡼⣒⢖⡲⣔⢲⡱⣚⠴⣊⠗⣮⡙⢦⢫⡜⣱⣯⣟⡾⣝⡧⣟⢾⡭⢃⣾⣿⡇⣾⣿⡇⣿⠸⣌⢣⡾⣫⠞⣭⢲⡙⢦⢫⡜⣣⢝⡪⣜⢖⡳⡜⢦⡓⡞⣭⢣⡝⣺⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣿⣿⣿⣏⡾⡽⢾⣹⠾⡅⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣛⠿⣿⣿⣿⣿⠿⣟⣛⣭⢷⣺⢯⣽⢫⡾⣵⢯⣳⢏⣾⡱⣎⢧⠳⣍⡞⣥⡛⣴⣙⡎⢧⣾⣟⣾⣵⣿⣳⡿⣯⢟⡴⠻⠿⢏⡸⢿⣳⢻⣿⠘⣰⢫⡞⣥⢛⡴⢣⡝⣎⠳⣜⡱⢎⡵⣚⢬⢳⡙⢶⡹⡜⢦⣓⠮⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⢞⣵⡻⣏⡷⣻⠇⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣝⠻⣶⢭⡹⣲⢯⢯⣟⣮⢷⢯⣟⡞⣯⢷⣫⢷⣫⢟⡶⣻⠵⣪⠟⣜⢮⡵⣹⣒⢧⢻⣹⣷⣿⣻⣾⣷⢿⣻⢏⡞⡼⣋⠗⣮⢱⢣⠖⣎⠥⡔⢡⡟⣜⢦⢫⡜⣣⠞⣬⢛⡴⣙⢎⠶⣩⢎⢧⡹⢲⡱⡹⢬⠤⢦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⢫⡾⡵⣏⡷⣏⡇⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣫⢥⠶⣩⠳⣌⠻⣵⡻⣜⣻⡼⡽⣞⢯⡾⣽⣹⢾⡹⣞⡵⣻⠼⣣⠏⡵⢛⡼⢣⡞⡵⡭⣞⣣⣿⣿⢾⣟⣷⡿⣿⡏⣼⢺⡱⣍⠞⡴⢋⣮⡙⣬⢛⡤⣶⣝⡘⢎⡳⡜⣥⢛⡴⣋⠶⣩⢎⡳⡱⢎⠶⣩⢇⡳⣙⢮⡹⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⡯⣗⢯⣗⣻⡼⣝⡆⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠫⣕⢫⠖⣭⢚⡥⣛⢬⢓⢦⡛⣷⡹⣞⡽⣭⢷⡻⣜⢧⡟⡽⢪⡝⢆⡻⢤⡛⢬⢳⣘⢣⡝⣣⢗⣣⢽⣿⣾⢿⣻⣯⢿⣷⢘⡧⢇⡳⣌⠻⣴⣿⡿⣿⡌⣳⠲⣽⡾⣿⣶⣅⡻⢔⡫⢖⡭⣚⠵⣪⠵⣙⢎⡳⡱⢎⡵⣩⢖⡹⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⡳⣽⢳⡞⣧⢟⡾⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣮⣁⠋⢶⡩⢖⠭⡲⡍⢶⡙⠶⣍⣳⡹⣜⡲⡝⡼⢦⡹⣜⢣⠞⣥⢓⡣⢞⣡⠳⣌⢣⠞⣥⢻⡬⣻⣷⡿⣿⡻⢝⣫⡄⣾⡙⢮⡱⢎⢱⣿⢷⣻⣯⡇⢧⠇⣿⣽⡷⣯⣟⣿⣦⡙⢎⠶⣩⠞⣥⢛⡜⢮⡱⣙⢎⠶⡱⢎⡕⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⡯⣗⢯⣳⣛⣮⢟⣼⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⢦⡙⢎⡳⣱⡙⢦⡝⣫⡜⢶⣱⢣⣳⣙⠮⣇⡳⢭⣚⡝⠦⢋⠘⡥⣒⠲⣌⢳⡚⣜⢧⢳⢽⣷⡟⣣⢶⡻⣜⡇⢾⡙⢦⡙⢮⢹⣯⢿⣻⣞⢣⡝⢆⣿⡷⣟⣯⣿⢾⣽⢿⣧⡙⢦⡛⡴⢫⡜⣣⠳⣍⢎⡳⣙⢎⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣿⣿⣿⣿⡳⣏⣯⢳⡽⣎⣟⡆⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣝⠣⢝⢪⡕⣣⠝⠃⣜⣑⣙⣚⣴⣯⣴⣭⣬⣥⣭⣴⣶⣶⣾⣷⠠⡳⣍⠳⣬⢣⡝⣎⡞⡭⡎⣫⡼⣝⡾⣹⢧⣇⠿⡸⣅⠻⣜⣊⠻⠯⢗⡥⣓⢞⠸⣿⣽⢿⣽⡾⣟⣯⡿⣽⡿⣆⢹⡜⣣⠞⣥⢛⡜⢮⡱⣍⠞⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣿⣿⣿⣿⡷⣫⢷⣚⣯⢳⣽⢺⢰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣧⡺⢅⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡳⣌⠷⣬⢓⠮⣕⣺⡑⣵⡳⣽⢺⡵⣛⠾⡼⡘⡵⢊⠷⡸⣌⠻⣜⡣⢞⡱⢎⡶⡝⢯⣿⣞⣿⣻⣽⣟⣯⡿⣟⣧⠸⣥⢛⡴⢫⡜⣣⠕⣮⣙⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣿⣿⣿⣿⢺⣭⢷⣫⢞⡯⣞⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢳⢬⠳⣬⢫⡝⢦⢃⣾⡱⣟⡼⢏⡞⡍⣞⣡⠳⡸⡍⣞⠱⣎⡝⡲⣍⢯⡑⣬⠳⣟⡎⢿⣾⢯⣷⢿⣞⣯⣿⣟⡿⣇⠲⣍⢖⡣⢞⡥⣛⢤⡓⣼⣿⣿⣿⣿⣿⣿⣿⣿⢫⣿⣿⣿⣿⣿⢧⡟⣮⠷⣭⡟⣾⣱⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢘⣎⢳⢥⡳⣚⡍⣞⠶⣏⠷⣩⠞⡴⡹⡰⢎⠵⣃⠳⣌⠳⡜⡼⡱⢎⠖⡜⢦⡛⡼⣽⡸⣟⣯⣿⢯⣿⣽⡾⣯⣿⣻⡘⡜⣎⠵⣋⢴⡩⢖⢡⣿⣿⣿⣿⣿⣿⣿⡿⣣⣿⣿⣿⣿⣿⡳⣏⣾⢳⡻⣵⢻⣜⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣌⡳⢎⡵⢳⡸⣭⠟⣬⠳⣑⢮⡑⢧⡓⡭⢎⠵⣋⡜⡣⠝⠴⡙⢤⡛⣜⢣⡝⡲⢧⡇⣿⡿⣽⣿⣳⣯⣿⣟⡷⣯⡇⡝⣬⢳⡩⢖⡹⢊⣾⣿⣿⣿⣿⣿⣿⡟⣵⣿⣿⣿⣿⣿⡳⣏⡷⣞⢯⣳⢏⡿⡜⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣥⢛⡼⡜⡃⡽⣎⡝⣆⢻⡘⢦⡙⣦⡙⢶⢩⠞⡴⣙⢲⡙⠶⣙⢦⡹⣌⠳⡼⣱⢫⢶⣹⡿⣟⣾⣟⣷⡿⣽⣻⢷⡇⡜⢦⢣⡝⠮⢅⣾⣿⣿⣿⣿⣿⡿⣫⣾⣿⣿⣿⣿⣿⢳⣏⡷⣽⢺⣝⡮⣟⡞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢘⢦⣋⠶⣱⢣⡝⡲⡜⣬⢣⡝⢦⣙⢦⡙⣎⢧⡚⣥⢋⠶⣩⠳⣍⠶⡱⢎⡽⢲⢥⢫⢷⢸⣿⢿⣽⣾⢿⡽⣷⢯⣟⡆⡝⣎⠳⡜⢃⣾⣿⣿⣿⡿⢟⣫⣾⣿⣿⣿⣿⣿⡿⣭⢷⡺⣵⢏⣷⢫⡾⡵⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⢦⣙⢮⡱⢣⢞⡱⣍⢖⡣⢞⡱⢎⠶⣙⠲⡎⡵⢪⡝⢮⡱⢫⡜⣣⡝⣭⢚⢧⣚⡭⡎⣿⣯⣿⣻⢾⣯⢿⣽⣻⢾⢡⢛⡬⠓⣡⣿⡿⢟⣛⣭⣶⣿⣿⣿⣿⣿⣿⣿⢯⣳⢏⡾⣝⡮⣟⡼⣻⠼⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⣧⢚⢦⡙⢧⢎⡵⣊⢮⡱⢫⡜⣭⢚⡥⣛⠼⣱⢣⠞⣥⢋⠷⣸⢱⣚⢬⢏⡞⢦⡝⢇⣿⣳⢯⣟⡿⣞⡿⣾⡽⢇⣤⣦⣤⣼⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡧⣟⢮⣻⢵⣫⢷⣹⢞⡕⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢪⢝⡢⡝⣎⠞⡴⣩⠖⡭⣓⡜⢦⣋⠶⣩⢞⡡⢏⡞⡴⣋⠷⣡⠗⣎⡳⢎⣝⡣⡟⣼⣳⢯⣟⣾⡽⣯⣟⣷⢫⣾⣟⣿⣻⣯⢿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⣜⣳⡽⣫⡞⣧⣛⣮⢗⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢋⠶⣙⡜⢮⡱⢣⢞⡱⡱⢎⡳⣌⢳⡱⢎⡵⣋⠼⡱⣍⠞⣥⢛⡬⢳⢭⡲⡝⣼⣳⣟⣯⣟⡾⣽⣳⣟⣴⣿⣳⣯⣷⢿⣽⣿⣻⣯⣿⣿⣿⣿⣿⢟⣯⢳⣳⢽⡲⣏⡷⣽⢣⣟⡼⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢢⡝⢦⡙⠧⣎⠵⣙⢎⡵⢊⢧⡙⣎⠶⣩⢞⡱⢎⡝⢦⢫⡜⣣⢧⣛⣾⣽⣳⣟⡾⣽⣻⢷⣻⣞⡿⣾⣽⣳⡿⣯⣿⢾⣟⣿⣽⣿⢿⡻⣵⢫⡾⣭⡳⣏⡷⣝⢾⣱⠿⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⡣⢝⡳⣌⠳⣍⠮⡜⣭⠲⣹⢰⣋⢖⡣⡝⢮⡜⣣⢳⡚⡥⠷⠻⠗⣋⣳⣭⣟⡷⣯⢿⣽⢾⣻⢷⣯⢿⣽⡿⣽⡿⣟⢯⣝⢮⣳⡝⣮⢟⣼⢳⡝⣧⢟⣮⠻⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣅⡊⠷⣌⠳⣍⢲⡙⢦⢳⡘⣎⠵⣙⢦⡙⠦⣃⢥⣒⠾⡟⢿⡻⣽⢾⣽⣻⣽⡻⢾⡻⢯⡟⣞⢯⡽⣹⢶⡹⣎⠷⣎⡟⣶⡹⢧⣛⣮⢻⡼⣫⢞⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣮⣬⣁⡙⢘⣢⡙⣤⢩⣌⠲⣜⡱⢎⠶⣩⢞⡹⢲⣙⢦⣋⠶⣱⠲⣭⢳⣙⠮⡵⣋⠾⡜⣧⢫⠷⣭⢻⡼⣹⢶⡹⣏⢷⡺⢝⣪⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣭⣆⡳⢌⡳⣌⠧⣋⠞⣥⢚⡵⢫⡜⡲⣍⠞⣥⡛⡴⣓⠮⣝⡲⢭⣋⢷⡩⣗⢻⡜⣧⢻⡥⡏⠷⣙⣬⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣭⣬⣙⣂⠏⠲⠣⢞⡱⢎⡝⢦⡙⢶⡩⢞⡲⣍⢧⡹⢲⠝⠼⢃⣛⣨⣥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿😇😇😇ദ്ദി ˉ͈̀꒳ˉ͈́ )✧ദ്ദി ˉ͈̀꒳ˉ͈́ )✧""")
def draw_Charizard2(): #Image used for evolutions - stage 2
    print ("""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣩⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⡛⢿⣿⣿⣿⣿⡇⣿⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⢿⣷⣝⢿⣿⣿⡿⣿⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⢫⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣵⢆⣿⣿⣧⡻⣿⣷⣍⡩⣷⣿⣿⣎⢿⣿⣿⣿⣿⣿⣿⣿⣦⠻⣷⣝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣩⣾⡟⣡⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⣿⣿⣿⣿⣷⢹⣿⣿⣶⣮⣝⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢟⣥⣾⣿⣿⣿⢸⣿⣿⣿⣿⣿⡿⣸⣿⢛⢿⣿⣿⣿⡿⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡟⠁⠀⠈⠉⠛⠻⠶⣮⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⣡⡾⠋⠁⠀⠀⢹⡸⣿⣿⣿⣿⣿⣇⢿⣿⣽⣀⡙⢏⣿⣿⣴⢻⣿⣿⣿⣿⣿⣿⣿⡏⣾⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢋⡾⠋⠀⠀⠀⠀⠀⠀⢧⢻⣿⣿⣿⣿⣿⣎⠫⣛⢿⣿⣿⣿⣿⣿⣷⢹⣿⣿⣿⣿⣿⣿⢣⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡜⣿⣿⣿⣿⣿
⣿⣿⣿⢃⡟⠁⠀⠀⠀⠀⠀⠀⠀⠘⢧⡹⣿⣿⣿⣿⣿⡼⣮⡳⠙⣿⣖⣶⣿⢣⣿⣿⣿⣿⣿⣿⡟⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠜⢿⣿⣿⣿
⣿⣿⡏⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣎⢿⣿⣿⣿⡇⣿⣿⣬⣒⢒⣦⣴⣿⣿⣿⣿⣿⣿⣿⢣⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢎⢻⣿⣿
⣿⣿⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡼⣿⣿⣿⡇⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⡿⣣⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠹⣿
⣿⡇⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠹⣿⣿⢹⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⢟⣩⠞⠁⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⣿
⣿⢰⠁⠀⠀⠀⠀⢀⢤⡠⡀⠀⠀⠀⠀⠀⠀⠘⢷⡙⠟⣼⣿⣿⣿⣿⣿⡎⠿⣛⣭⡶⠁⢶⣄⣴⣷⡧⡀⠀⠀⠀⠀⣀⠀⠀⣰⣶⣄⡀⠀⠀⠀⠀⢧⢹
⡏⢸⠀⠀⣠⣾⡇⠟⣽⢻⠼⣣⠀⠀⣀⣀⠀⠀⢀⣙⢱⣿⣿⣿⣿⣿⣭⣶⣶⣮⠋⠀⠀⠱⣾⣟⣽⣑⡫⠀⢀⣶⣾⣿⣆⢤⡿⠿⢟⣿⣦⡀⠀⠀⢸⢸
⣧⢸⣰⣿⣿⣿⢁⣛⢿⣮⣭⣷⣜⠿⠿⢿⣛⣴⡿⢣⠿⠟⠛⠿⣿⣿⣿⣿⣿⣿⣦⡀⢠⣶⢼⣷⡿⣋⠀⠀⠿⢿⣿⣿⣿⣷⢷⣵⣿⣿⣿⣿⣦⡀⢸⢸
⣿⣀⣿⣿⣿⣿⣷⣿⣶⣦⣬⡛⠿⣿⣾⠿⢟⡫⢀⣵⣿⣿⣿⣿⣦⡙⢿⣿⣯⣝⡻⢿⣾⢍⣼⣿⢣⣿⣆⣠⣄⠀⠏⢯⠻⣱⣿⣿⣿⣿⣿⣿⣿⣿⡜⢸
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⣿⣿⣿⣦⡙⠿⡿⢋⣾⣿⣿⣿⣿⣶⣾⡎⣷⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⣷⡰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣷⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣎⢻⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢣⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⠏⣼⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣾⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⡿⢋⣾⣿⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣿⣿⣿⣧⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠘⠟⣛⣩⣴⣿⣿⣿⣿⢇⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⣿⣿⣌⡻⣿⣿⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⡿⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢟⣵⣷⣾⣿⣿⣿⢫⣤⣍⠛⠿⠿⠿⣿⣷⡜⢿⣿⣿⣿⣿⣿⡇⣾⣿⣿⣿⡿⢟⡫⣢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡷⣛⣭⠿⣿⣿⣿⣿⠿⣠⣿⣿⣿⣮⣝⡻⢿⣿⣿⣷⢨⣽⣿⣿⣿⣦⡙⣛⣭⡵⢞⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣭⠭⢾⣓⣙⣭⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣭⡅⡟⣛⢿⡿⣛⢿⣟⣈⢵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣜⢿⢎⣘⢿⡏⣬⣛⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
def draw_Charizard3(): #Image used for evolutions - stage 3
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣶⣤⣶⣿⣿⣷⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⢀⣴⡿⢿⣿⣿⠿⠻⠿⢿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠟⠋⣴⣦⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠟⠛⠛⢿⡟⠛⠿⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣧⠀⠀⠀⠀⠀⣠⡖⠀⠀⢀⣸⡿⠁⠀⠘⠿⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢔⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡀⠀⠀⠀⢸⡇⠀⢀⣴⣿⣿⠃⠀⠀⠀⠀⢀⣼⣿⣿⣿⣉⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠪⣛⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡇⠀⠀⠀⠊⠀⣶⣿⣿⣿⣿⠀⠀⠀⠀⣴⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡝⢷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⠟⠉⠉⢿⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⡙⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠙⣷⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠟⠁⠀⠀⠀⠈⣧⢀⣾⣿⣿⣿⣿⣿⣿⣿⡀⢀⣾⣿⣿⣿⣿⠖⠀⠀⠉⠉⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡈⢿⣦⠀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠈⢿⣧⠀⠀
⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣮⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠘⣿⣇⠀
⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢯⣛⣛⣥⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⢹⣿⡄
⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣹⣿⣿⣿⣿⣿⡟⠁⠀⠀⠉⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠸⣿⡇
⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣾⣿⠿⠿⠿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⣿⣿
⢸⡇⠀⠀⠀⢠⠞⠓⢄⠀⠀⢀⣴⣿⡟⢱⢆⠀⠀⢀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⣿⣿
⣸⡇⠀⢀⡴⠁⠀⠀⢀⣷⣿⣿⣿⣿⡀⠃⠈⠀⢀⢚⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⣿⣿
⣿⡇⢠⠎⠀⠀⠀⠀⠸⠏⠘⡿⠋⠟⠃⠀⠀⠐⠃⢸⣿⣿⣿⣿⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⢸⣿⡏
⣿⡇⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢠⠁⠀⠀⠀⠀⠈⡿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⢀⣿⣿⠃
⢹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⢇⢻⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠁⠀⢀⣾⣿⠏⠀
⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠘⡌⢿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢠⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⣠⣿⣿⡟⠀⠀
⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⡙⢿⣿⣿⣿⣿⣿⣿⣷⣤⣄⡀⠉⠙⠻⠿⣷⣤⣀⣀⣀⣤⣤⠶⠞⠋⠁⠀⠀⢀⣴⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣶⣍⡛⠿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣮⣝⠻⢿⣿⣿⡿⢿⡿⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣷⣦⣽⣿⣷⣤⣤⣦⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
def draw_egg(): #Image used for evolutions, before stage 1
    print ("""⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟥🟥🟥🟥🟥⬛⬜⬜⬜
⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜
⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜
⬛🟥🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥⬛
⬛🟥🟥🟥🟥⬛⬜⬜⬛🟥🟥🟥🟥⬛
⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛
⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬛
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜""")


def Train(): #Raises level of pokemon by 1
    global pokemon_level
    pokemon_level = pokemon_level + 1
    training_message()
    print ("Level up!!!")
    print ("Level: "+str(pokemon_level))
    print ("""
            """)
def Train2(): #Raises level of pokemon by 2
    global pokemon_level
    pokemon_level = pokemon_level + 2
    print ("Level: "+str(pokemon_level))
    print ("""
            """)

def GymBattle(): #2nd option for a player, player can level up 0 or 2 levels
    outcome = random.randint(1,2)
    if outcome == 1:
        print ("Your pokemon won the fight! You level up by 2!!!")
        Train2()
    if outcome == 2:
        print ("Your pokemon lost the fight!!!")
        print ("Level: "+str(pokemon_level))
    print ("""
            """)

def evolve(): #evolutions come at levels 10, 20, and 30
    #when evolutions happen, an image that goes with the level appears
    #name changes as well
    global pokemon_name
    if pokemon_level == 10:
        pokemon_name = "Charmander"
        draw_Charizard1()
        print ("""
        
Congrats! Your pokemon has evolved to stage 1!""")
    if pokemon_level == 20:
        pokemon_name = "Charmeleon"
        draw_Charizard2()
        print ("""

Congrats! Your pokemon has evolved to stage 2!""")
    if pokemon_level == 30:
        pokemon_name = "Charizard"
        draw_Charizard3()
        print ("""

Congrats, your pokemon has evolved to the final stage!""")
    print ("""
            """)

def training_message(): #randomizes training message for players, 1st option
    message = random.randint(1,3)
    if message == 1:
        print ("Your pokemon " + str(pokemon_name) + " practices for a few hours and gains new skills!")
    if message == 2:
        print ("Your pokemon " + str(pokemon_name) + " tried out a new exercise!")
    if message == 3:
        print ("Your pokemon " + str(pokemon_name) + " ran a few miles, now it has more stamina!!")
    
def Rest(): #4th option for players when they want to quit playing
    print ("Your pokemon is tired after a long day of training and fighting.")
    print ("Level: "+str(pokemon_level))
    if pokemon_level < 10:
        draw_egg()
    if pokemon_level >= 10 and pokemon_level <20:
        draw_Charizard1()
    if pokemon_level >= 20 and pokemon_level < 30:
        draw_Charizard2()
    if pokemon_level >= 30:
        draw_Charizard3()
    print ("""
            """)

def Intro_Image(): #image used for the introduction, aesthetic purposes
    print ("""⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢟⣩⡶⠳⡹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⣥⣶⣿⣷⣶⣍⠀⠀⢣⢿⣿⣿⣿⣿
⢫⡶⠦⠬⠭⢍⣑⢸⣿⣿⣿⣿⣿⣿⣧⢀⢸⢸⣿⣿⣿⣿
⢸⣧⠀⠀⠀⣰⣿⣿⣟⠿⢿⣿⣿⣿⣿⢸⣷⣌⢻⣿⣿⣿
⡆⣿⡄⠀⣸⣿⣿⠿⠿⣿⢲⣼⣿⣿⠟⠈⢠⡌⢣⢻⣿⣿
⣷⠹⣿⣴⡿⡫⠊⠀⣴⣆⠀⣭⣭⣥⣾⠀⠀⠁⠈⡇⣛⢻
⣿⢸⣿⣿⡇⡇⠀⠀⠉⠁⢰⢸⣿⣿⡿⢧⠢⣀⢄⡇⢏⣾
⣿⡌⣿⣿⣷⡹⣄⡀⢀⣠⢎⣾⣏⣤⡀⢸⣿⣶⣿⢇⣾⣿
⣿⣷⡹⣿⣿⣿⣶⣭⣭⠶⢿⣿⣿⡸⣿⢸⣿⣿⡟⣼⣿⣿
⣿⣿⣷⣜⢿⣿⣿⣿⣿⣿⡶⢎⣿⣿⣶⣿⡿⢋⣾⣿⣿⣿
⣿⣿⣿⣿⣷⣬⣙⠿⠶⢶⣾⡿⠿⠟⣛⣭⣚⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣏⠶⠿⠿⢟⣒⣤⣿⣿⣮⣭⣛⣛⣈⣿⣿⣿""")

def PokemonEvolutionGame(): #all functions put together for a final function
    print ("""Welcome to Pokemon Evolution Simulator
""")
    Intro_Image()
    print ("""
Choose an activity.""")
    print ("""
        1. Train
        2. Gym Battle
        3. Rest/Display Pokemon Info
        4. Exit
 """)
    while True:
        choice = int(input ("""Enter choice 1-4 _______            
        1.) Train_________
        2.) Gym Battle_________
        3.) Rest/Display Pokemon Info_________
        4.) Exit_________"""))
        if choice == 1:
            Train()
            evolve()
        if choice == 2:
            GymBattle()
            evolve()
        if choice == 3:
            Rest()
            evolve()
        if choice == 4:
            print ("You decide to end the training for today")
            evolve()
            print ("Level: "+str(pokemon_level))
            break #ends the loop if player chooses option 4


#Main
PokemonEvolutionGame()
