This code is for running on Expanse

- Step 1: Fix any PDB file to only have two chains. use fix_formatting_folder.py
- Step 2: Make folder on expanse: "Exemplars"
- Step 2: Upload fixed PDB files to folder on expanse "Exemplars/Input_PDBs"
- Step 3: Make folder for exemplars: "Exemplars/exemplars"
- Step 4: Modify gen_exemplars.py to the correct location of "Exemplars/Input_PDBs"
- Step 5: Geneate command list: use gen_exemplars.py and use the gen_exemplars module. This will output the command list
- Step 6: change into "Exemplars/exemplars" folder
- Step 7: copy exemplar_batch_submits.py into "Exemplars/exemplars" folder
- Step 8: run exemplar_batch_submits.py to generate submit scripts
- Step 9: for i in *.sb; do echo 'sbatch '$i''; done > submit.sh
- Step 10: split -l 2000 submit.sh (seperates submit.sh into two seperate submit scripts with 2,000 commands each)
- Step 11: mv xaa submit1.sh
- Step 12: mv xab submit2.sh
- Step 13: Bash submit1.sh
- Now all exemplars should be located in: "Exemplars/exemplars"
- Step 14: mv all of the old submit scripts into new folder; "Exemplars/exemplars/exemplar_submit_scripts". mv exemplars/*.sb exemplar_submit_scripts
- Step 14:  Make the complex PDB files:- use gen_exemplars.py and use the copy_files module and make_complexes module (just unhastage these two scripts), use submit.slurm to run this.
- Now all of the complexes are located in: "Exemplars/exemplars/complexes"

Step 3: use parallaize_get_exemplar_features.py to make a command list for all of the feature generations. 

