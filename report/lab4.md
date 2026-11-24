# Lab 4

### Setup/ Run Instructions
 There are no required dependancies to run Scyode (other than Python). Once you have downloaded the source code and are in your parent directory, you can access the interactive shell using ```python src/scyode.py``` or run a .vv file using ```python src/scyode [file_path]```. The files to run the tests documented below are in the lab4 folder under the test folder and can be run using ```python src/scyode test/lab4/[test_file]```.

 ### Test Cases

 1. panic.vv
    
    This test is the first test case listed in the lab assignment and demonstrates the panic-mode error recovery of the parser, which lets it report a syntax error and then continue parsing subsequent statements.

    Input: 
    ```
    "one"
    true;
    print 2 +
    ```

    Expected Output:
    ```
    [line 2] Error at 'true': Expect ';' after expression
    [line 3] Error at end: Expect expression
    ```

    Actual Output:
    ```
    [line 2] Error at 'true': Expect ';' after expression
    [line 3] Error at end: Expect expression
    ```

    Matches Expected: ✔

2. print.vv

    This test is the second test case listed in the assignment and demonstrates the function of the print statement and how expressions are no longer printed without a print statement.

    Input:
    ```
    4 + 2;
    print "one";
    print true;
    print 1 + 2;
    print nil;
    ```

    Expected Output
    ```
    one
    True
    3
    nil
    ```

    Actual Output:
    ```
    one
    True
    3
    nil
    ```

    Matches Expected: ✔