#!/bin/bash
#BATCH -J af2_job
#SBATCH -o my_prefix_output.%j.output
#SBATCH -e my_prefix_error.%j.err
#SBATCH -p compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=64
#SBATCH -t 24:00:00
#SBATCH --account=was136
#SBATCH --mem=8G
______________________________________________________________________

python ExemplarScreeningPocketDruggability/gen_exemplars.py /expanse/lustre/projects/was136/vmischley/vmischley_04_28/Exemplar_Screen_01_17/exemplars 1 12                                                                                                                                                                      
