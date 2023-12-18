This code is for running on Expanse
Step 1: Generate exemplars- use gen_exemplars.py and use the gen_exemplars module. This will output the command list
- use python script to generate submit scrips
- for i in *.sb; do echo 'sbatch '$i''; done > submit.sh
- split -l 2000 submit.sh (seperates submit.sh into two seperate submit scripts with 2,000 commands each)
- Bash submit1.sh


After exemplars are done running: 
Step 2: Make the complex PDB files:- use gen_exemplars.py and use the copy_files module and make_complexes module

