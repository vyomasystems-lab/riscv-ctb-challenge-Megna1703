# challenge_level1
## challenge1_logical 
### Errors : Found errors in line number 15855 and 25584 in the file test.S
## Fixes :
### 1. add s7,ra,z4 ---> add s7,ra,a4
>z4 is an invalid operand as RV32M ISA defines a standard set of registers, and there is no provision for a specific register named "z4." I replaced it with a specifc register a4.
### 2. andi s5,t1,s0 --> and s5,t1,s0
>*andi* is a instruction for adding a immediate value to the source register and stores in the destination register. Here s0 is a register and not an immediate value. So the correct instruction should be *and* instead of *andi* so that it does bitwise operations of data in registers s0 and t1 stored in s5.
