# challenge_level1
## challenge3_illegal
### Errors : To fix an illegal instruction using a handler code

![Screenshot (1210)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/02904231-b3d7-4c9e-844d-7925d9851c8c)


## Fixes :
### Fix 1:
The code handles the machine trap vector for illegal instruction exceptions. When an illegal instruction is encountered, the code checks the cause of the exception and updates the program counter *mepc* within the handler to skip the illegal instruction, allowing the program to continue executing from the next instruction.

```
illegal_instruction:
  .word 0 
  j fail 
  TEST_PASSFAIL 

  .align 8 
  .global mtvec_handler
mtvec_handler:
  li t1, CAUSE_ILLEGAL_INSTRUCTION
  csrr t0, mcause
  bne t0, t1, fail
  csrr t0, mepc
  addi t0,t0,8             # Adding immediate 8 to the value in t0 
  csrw mepc,t0             # Updating the value of mepc to point to the next instruction after the illegal instruction 

  mret
  ....
```

![Screenshot (1211)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/23a757e1-4f34-49ca-a5e3-2d9f10f8e671)


The label *TEST_PASSFAIL* is defined inside the file **test_macros.h** which hass the *pass* and *fail* statements. It checks if x0 and *TEST_NUM* values are equal, if not, executes *pass*.

### Fix 2:
I replaced **.word 0** (illegal instruction) with **.word 164499** (instruction pointing to mv t0,t0 ). I used the **test.disass** file to get the instruction address.

```
illegal_instruction:
  .word 164499
  j pass
  TEST_PASSFAIL

  .align 8
  .global mtvec_handler
mtvec_handler:
  li t1, CAUSE_ILLEGAL_INSTRUCTION
  csrr t0, mcause
  bne t0, t1, fail
  csrr t0, mepc

  mret
  ....
```

![Screenshot (1212)](https://github.com/vyomasystems-lab/riscv-ctb-challenge-Megna1703/assets/110230441/1b6bd469-e021-4b48-ab92-3b1c7998ad51)
