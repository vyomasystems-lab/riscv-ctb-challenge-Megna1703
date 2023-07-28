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
In the Makefile we use the *grep* command under the *check* rule to trap all exceptions as follows:
```
check: test_spike.dump
	@echo '[UpTickPro] Number of Exceptions'
	spike -l --isa=rv32i test.elf 2> spike.log
	grep exception spike.log > exceptions.log
	......
```
The trapped instructions are stored in a generated log file, **exceptions.log** in my case.
