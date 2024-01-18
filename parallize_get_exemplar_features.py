import pandas as pd
import os
import argparse

def args():
    parser = argparse.ArgumentParser()
    # Add command line arguments
    parser.add_argument('folder_path', type=str, help='path to location of AF folder output')
    # Parse the command line arguments
    args = parser.parse_args()
    return args

def get_features(folder_path):
    output_file_path = f"{folder_path}/command_list.txt"
    command_list = []
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith(".pdb"):
            file_path = os.path.join(folder_path, file)
            command = f"featurize_pocket -pdb {file_path} -lig_name TMP -csv {file_path}.csv"
            command_list.append(command)
    with open(output_file_path, 'a') as output_file:
        output_file.write('\n'.join(command_list))



if __name__ == '__main__':
    args = args()
    get_features(args.folder_path)

