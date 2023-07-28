# challenge_level1
## challenge2_loop
### Errors : The test gets hanged and needs an interrupt to exit the spike simulation. 
## Fixes : 
 The test gets hanged as there is no check condition for the *loop* to terminate unless there is a *fail* condition. The loop checks for *fail* condition but when all the test cases pass successfully, the *loop* doesn't and gets hanged (as it is not terminated once all the test cases are verified). <br> I made the following changes to fix this error. 
### 1. The value of register t5 has to be decremented by 1 for each time *loop* is called as shown in the following code:
> addi t5, t5, -1
### 2. Initially register t5 is loaded with the value 3. As there are only 3 sets of test cases, I used the following code to *pass* once all the 3 test cases are verified:
> beqz t5, pass

### These two lines of code are exceuted under the label *loop* in the file test.S as follows:
```
loop: 
    beqz t5, pass
    addi t5, t5, -1
    .......
```

