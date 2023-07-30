# challenge_level3
## directed_test
## Fixes :
I executed the *Makefile* using the *make* and it showed an error like *spike:unrecognised option -c* :
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
After fixing this error, the *Makefile* generated two files **rtl.dump** and **spike.dump**. The *diff* command in the *Makefile* is used to check if both of the files are same. 

![Screenshot (1199)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/5fcaf3bd-8823-4940-a56f-a394964d8dc7)

I used the following command in the terminal to check if both the files are same:
```
diff -q rtl.dump spike.dump
```
