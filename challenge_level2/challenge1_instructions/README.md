# challenge_level2
## challenge1_instructions
### Errors: Unrecognised opcode due to instruction distribution type
## Fixes :
### Fix 1:
The *compile* rule in the Makefile has *-march* defined as **rv32i** ( -march allows you to specify the ISA and extensions that the compiled code should be compatible with). 
```
compile:
	@echo '[UpTickPro] Test Compilation ------'
	riscv32-unknown-elf-gcc -march=rv32i -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -I$(PWD)/work/common -T$(PWD)/test.ld test.S $(PWD)/work/common/crt.S -o test.elf
```

Therefore instructions which are compatible with this ISA should be present under the *isa-instruction-distribution* in **rv32i.yaml** file. 
```
isa-instruction-distribution:
  ................
  rel_rv32i.compute: 10
  rel_rv32i.data: 10
  rel_rv32i.fence: 10
  ....
  ...
  rel_rv32m: 0 
  rel_rv64m: 0     # This value has to be zero as it a rv64m ISA instructions which is not compatible with rv32i ISA 
  ....
  ....
```
### Fix 2:
Incase if want a ISA compatible with **i,m** then modify the makefile by replacing **rv32i** with **rv32im** as follows:
```
all: gen compile disass spike

gen: clean
	@echo '[UpTickPro] Test Generation ------'
	aapg setup
	aapg gen --config_file $(PWD)/rv32i.yaml --asm_name test --output_dir $(PWD) --arch rv32

compile:
	@echo '[UpTickPro] Test Compilation ------'
	riscv32-unknown-elf-gcc -march=rv32im -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -I$(PWD)/work/common -T$(PWD)/test.ld test.S $(PWD)/work/common/crt.S -o test.elf

disass: compile
	@echo '[UpTickPro] Test Disassembly ------'
	riscv32-unknown-elf-objdump -D test.elf > test.disass

spike: compile
	@echo '[UpTickPro] Spike Run ------'
	spike --isa=rv32im test.elf 
	spike --log-commits --log  test_spike.dump --isa=rv32im +signature=test_spike_signature.log test.elf

clean:
	@echo '[UpTickPro] Clean ------'
	rm -rf work *.elf *.disass *.log *.dump *.ld *.S *.ini
```
We can have **rv32m** instructions as well, as it is compatible in **rv32im** ISA
```
isa-instruction-distribution:
  ................
  rel_rv32i.compute: 10
  rel_rv32i.data: 10
  rel_rv32i.fence: 10
  ....
  ...
  rel_rv32m: 10
  rel_rv64m: 0     # This value has to be zero as it a rv64m ISA instructions which is not compatible with rv32im ISA 
  ....
  ....
```
