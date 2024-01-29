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

def get_csv(folder_path):
    file_names = []
    merged_data = pd.DataFrame()
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            data = pd.read_csv(file_path)
            file_name = file
            file_names.append(file_name)
            merged_data = merged_data.append(data, ignore_index = True)
    merged_data['file_name'] =file_names
    output_csv_path = os.path.join(folder_path, f"combined_features_updated.csv")
    merged_data.to_csv(output_csv_path, index = False)

if __name__ == '__main__':
    args = args()
    # get_features(args.folder_path)
    get_csv(args.folder_path)
