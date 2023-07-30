# challenge_level3
## random_test
## Fixes :
### Fix 1:
When I gave the *make* command to run the **Makefile**, I faced an error *spike: unrecognized option -c*.
```
spike: compile
	@echo '[UpTickPro] Spike ------'
	spike --isa=rv32i test.elf 
	spike -c --isa=rv32i +signature=spike_signature.log test.elf --log-commits --log spike.dump
.....
```
![Screenshot (1200)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/6c89541f-4d84-4029-bfa4-338e0f1d0039)

I used the command *which spike* to identify the spike version to use. I make the following changes:
```
spike: compile
	@echo '[UpTickPro] Spike ------'
	/tools/mod_spike/bin/spike --isa=rv32i test.elf 
	/tools/mod_spike/bin/spike -c --isa=rv32i +signature=spike_signature.log test.elf --log-commits --log spike.dump
....
```
### Execution of the code:
The when the *Makefile* of the *random_test* is executed, it produces **rtl.dump** and **spike.dump**. The spike rule in the *Makefile* uses a command *diff* 
to show if the two generated files are same or different. 
I tried executing the *make* several times and the files are either same or different in various cases. 
The following is displayed when the generated **rtl.dump** and **spike.dump** are same:

![Screenshot (1201)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/a702b26e-1619-4221-af6e-7f8af0e6ba26)

The following is displayed when the generated **rtl.dump** and **spike.dump** are different:
I used *diff -q rtl.dump spike.dump* in the terminal to show if the files differ or not.

![Screenshot (1202)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/bc157c1d-4b21-4472-b007-a196f9368b4f)

I compared the **test.S** files for *directed_test* and *random_test* and I found that the test cases generated in *directed_test* were fixed whereas in
*random_test* the test cases were generated randomly.

![Screenshot (1204)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/591fad89-8040-44d5-890f-89dfb4757968)




