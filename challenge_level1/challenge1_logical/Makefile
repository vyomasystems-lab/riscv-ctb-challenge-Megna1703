all: compile disass spike

compile:
	riscv32-unknown-elf-gcc -march=rv32i -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -I$(PWD)/common -T$(PWD)/common/link.ld test.S -o test.elf

disass: compile
	riscv32-unknown-elf-objdump -D test.elf > test.disass

spike: compile
	/tools/spike_hyp_latest/bin/spike --isa=rv32i test.elf 
	/tools/spike_hyp_latest/bin/spike --log-commits --log  test_spike.dump --isa=rv32i +signature=test_spike_signature.log test.elf

clean:
	rm -rf *.elf *.disass *.log *.dump
