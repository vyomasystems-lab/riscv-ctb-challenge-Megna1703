# challenge_level2
## challenge2_exceptions
## Fixes :
I generated 10 exceptional errors of type **misaligned instruction addresses** by setting the value of *ecause00* to 10 under the **exception generation** in **rv32i.yaml** file

```
exception-generation:
  ecause00: 10
  ecause01: 0
  ecause02: 0
  .....

```

![Screenshot (1220)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/b184b5a1-0b78-4996-bdf8-40512fd38db7)

In the Makefile we use the *grep* command under the *check* rule to trap all exceptions as follows:
```
check: test_spike.dump
	@echo '[UpTickPro] Number of Exceptions'
	spike -l --isa=rv32i test.elf 2> spike.log
	grep exception spike.log > exceptions.log
	......
```

![Screenshot (1221)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/c8900ce8-1628-4c60-bd20-49ebabf8ab9a)


The trapped instructions are stored in a generated log file, **exceptions.log** in my case.

![Screenshot (1222)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/97f7c94e-a4b7-4d51-aa2b-640f92f8a5c0)

