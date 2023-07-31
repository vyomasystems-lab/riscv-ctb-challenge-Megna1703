# RISCV-DV

Test generation using riscv-dv
```
run --target rv32i --test riscv_arithmetic_basic_test --testlist testlist.yaml --simulator pyflow
```

Coverage related information is obtained in the below link:
https://github.com/chipsalliance/riscv-dv/tree/master/pygen/pygen_src

# Challenge
The challenge is to fix the tool problem in generating coverage and make rv32i ISA coverage 100%

The *test.yaml* file had several tests which we have to execute and generate a coverage reports.
I made python script consisting of the following commands:
```
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


```

I executed the following code in terminal:

```
python script.py
```
![Screenshot (1225)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/308e0c71-0006-4ae0-8869-3884a195f539)

Coverage report for riscv_arithmetic_basic_test 

![Screenshot (1226)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/090a8906-0b1e-4f1c-9f53-7f5ffa2d9b2e)
