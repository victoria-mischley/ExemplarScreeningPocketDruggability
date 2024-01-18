This code is for running on Expanse

- Step 1: Fix any PDB file to only have two chains. use fix_formatting_folder.py
- Step 2: Make folder on expanse: "Exemplar_screen"
- Step 2: Upload fixed PDB files to folder on expanse "Exemplar_screen/Input_PDBs"
- Step 3: Make folder for exemplars: "Exemplar_screen/exemplars"
- Step 4: Modify gen_exemplars.py to the correct location of "Exemplar_screen/Input_PDBs"
- Step 5: Geneate command list: use gen_exemplars.py and use the gen_exemplars module. This will output the command list
- Step 6: change into "Exemplar_screen/exemplars" folder
- Step 7: copy exemplar_batch_submits.py into "Exemplar_screen/exemplars" folder
- Step 8: run exemplar_batch_submits.py to generate submit scripts
- Step 9: for i in *.sb; do echo 'sbatch '$i''; done > submit.sh
- Step 10: split -l 2000 submit.sh (seperates submit.sh into two seperate submit scripts with 2,000 commands each)
- Step 11: mv xaa submit1.sh
- Step 12: mv xab submit2.sh
- Step 13: Bash submit1.sh
- Now all exemplars should be located in: "Exemplar_screen/exemplars"
- Step 14: mv all of the old submit scripts into new folder; "Exemplar_screen/exemplars/exemplar_submit_scripts". mv exemplars/*.sb exemplar_submit_scripts
- Step 14: remove all files ending in .out or .err within the exemplar folder (speeds up downstream calculations a bit)
- Step 15: mv all of the Input_PDBs into exemplar folder: mv Input_PDBs/*.pdb exemplars
- Step 16:  Make the complex PDB files:- use gen_exemplars.py and use the copy_files module and make_complexes module (just unhastage these two scripts), use submit.slurm to run this.
- Now all of the complexes are located in: "Exemplar_screen/exemplars/complexes"
- Step 17: use parallaize_get_exemplar_features.py to make a command list for all of the feature generations. Command list will be located in complex folder. Direct the python script to the folder containing the complexes: python parallize_get_exemplar_features.py /expanse/lustre/projects/was136/vmischley/vmischley_04_28/Exemplar_Screen_01_17/exemplars/complexes/
- 

