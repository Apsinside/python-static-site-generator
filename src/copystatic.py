import os
import shutil

def copy_files_recursive(source, target):   
    if not os.path.exists(target):
        print("creating directory " + target) 
        os.mkdir(target)
    
    if os.path.exists(source):
        for dir in os.listdir(source):
            source_path = os.path.join(source, dir)
            target_path = os.path.join(target, dir)
            if os.path.isfile(source_path):
                print("copying file " + dir + " -> " + target)
                shutil.copy(source_path, target_path)
            else:
                targetPath = os.path.join(target, dir)              
                copy_files_recursive(source_path,target_path)   
