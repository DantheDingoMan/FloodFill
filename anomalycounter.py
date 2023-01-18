#!/usr/bin/env python3
# Solution by Aidan Schooling
from pathlib import Path

def fill(filelists, positionx, positiony):
    filelists[positionx][positiony] = 'o'

    
    
        
    try:
        if positionx != 0:
            if filelists[positionx-1][positiony] == '*':
            
                fill(filelists, positionx-1, positiony)

        if positiony != 0:
            if filelists[positionx][positiony-1] == '*':
                fill(filelists, positionx, positiony-1)
        
    
        if filelists[positionx][positiony+1] == '*':
            fill(filelists, positionx, positiony+1)
        if filelists[positionx+1][positiony] == '*':
            fill(filelists, positionx+1, positiony)
    except IndexError as ie:
        pass
    return filelists

def count(filename: str) -> int:
    """Count number of anomalies/blobs in an image

    :param filename: name of the file to process
    :return: number of anomalies/blobs in the file
    """
    
    file = open(filename, "r")
    filelist = file.read().splitlines()
    filelists=[]

    for i in range(len(filelist)):
        filelists.append(list(filelist[i]))
    
    file.close()

    counter = 0
    for i in range(len(filelists)):
        
        for z in range(len(filelists[i])):
            
            
            if filelists[i][z] == '*':
                counter += 1

                filelists = fill(filelists, i, z)
                print(filelists)
                print(counter)


    
    
    return counter


 


def main():
    """Entry point"""
    data_dir = "data/projects/anomalycounter/"
    for f in Path(data_dir).glob("*.in"):
        print(f"{f.name}: {count(f)}")


if __name__ == "__main__":
    main()
