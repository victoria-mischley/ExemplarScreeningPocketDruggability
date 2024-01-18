This code is for running on Expanse
Step 1: Fix any PDB file to only have two chains. use fix_formatting_folder.py
Step 2: Geneate command list: use gen_exemplars.py and use the gen_exemplars module. This will output the command list
- use python script to generate submit scrips
- for i in *.sb; do echo 'sbatch '$i''; done > submit.sh
- split -l 2000 submit.sh (seperates submit.sh into two seperate submit scripts with 2,000 commands each)
- mv xaa submit1.sh
- mv xab submit2.sh
- Bash submit1.sh


After exemplars are done running: 
Step 2: Make the complex PDB files:- use gen_exemplars.py and use the copy_files module and make_complexes module

Step 3: use parallaize_get_exemplar_features.py to make a command list for all of the feature generations. 

