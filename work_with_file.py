import pickle
game_data = {'позиция' : 'C23 B45',
    'карманы' : ['ключи', 'ноШ', 'камень'],
    'рюзак' : ['веревка','яблоко'],
    'деньги' : 158.60}
save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()


load_file = open('save.dat', 'rb')
#load_file = open('c:\\Users\\User1\\save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)
"""
import shutil
shutil.copy('c:\\Users\\User1\\test.txt',"c:\\Users\\User1\\file.txt")
#test_file = open('c:\\Users\\User1\\test.txt')
#file = open("c:\\Users\\User1\\file.txt", "w")
#file.write("test test")
#file.close()
file = open('c:\\Users\\User1\\file.txt')
text = file.read()
print(text)
"""