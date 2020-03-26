import os
import sys
import shutil

LOG_FILE_LOCATION = sys.argv[1]
CHUNK_LENGTH = sys.argv[2]
WRITE_LOCATION = os.path.join(os.getcwd(), "test")

if os.path.exists(WRITE_LOCATION):
    shutil.rmtree(WRITE_LOCATION)

os.mkdir(WRITE_LOCATION)

f_read = open(LOG_FILE_LOCATION)
log_data = f_read.read()
chunk_length = int(sys.argv[2])
starting_positon_of_chunk = 0
count = 0

def write_chunk_data(chunk):
    global count

    f_write = open("{0}/chunk_{1}".format(WRITE_LOCATION, count), "w+")
    f_write.write(chunk)
    f_write.close()
    count = count + 1


while starting_positon_of_chunk != log_data.rfind(" ")+1 :

    chunk = log_data[starting_positon_of_chunk : starting_positon_of_chunk+chunk_length]
    last_char_of_chunk =  log_data[starting_positon_of_chunk : starting_positon_of_chunk+chunk_length+1][-1]

    index_of_last_space = chunk.rfind(" ")
    
    if last_char_of_chunk == " ":
        write_chunk_data(chunk)
        starting_positon_of_chunk = starting_positon_of_chunk + chunk_length + 1
    else:
        write_chunk_data(chunk[0:index_of_last_space])
        starting_positon_of_chunk = starting_positon_of_chunk + index_of_last_space + 1

f_read.close()
