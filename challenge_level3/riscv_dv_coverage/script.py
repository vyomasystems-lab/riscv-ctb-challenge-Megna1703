import os
import sys
testname = "riscv_arithmetic_basic_test"     
#testname = "riscv_rand_instr_test"           
#testname = "riscv_jump_stress_test"         
#testname = "riscv_loop_test"                 
out_directory = "out_2023-07-31" 

out_csv = testname + "_trace.csv"

os.system("run --target rv32i --test " + testname + " --testlist testlist.yaml --simulator pyflow")

os.system("python /tools/riscv-dv/scripts/spike_log_to_trace_csv.py --log " + out_directory + "/spike_sim/" + testname + ".0.log --csv " + out_csv + " -f")

os.system("python /tools/riscv-dv/pygen/pygen_src/test/riscv_instr_cov_test.py --num_of_tests=1 --start_idx=0 --asm_file_name=" + out_directory + "/asm_test/" + testname + "0.S --trace_csv=" + out_csv + " --log_file_name=" + out_directory + "/sim_#" + testname + "_0.log --target=rv32i --seed=2033903432 --disable_compressed_instr=1")



