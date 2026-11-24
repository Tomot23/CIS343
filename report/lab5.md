# Lab 5

### Variable Design Choices
All design choices in regards to variable declaration, access, and assignment made my Lox have been reflected in Scyode. If a variable is accessed before its declaration, Scyode raises a runtime error. If there is a missing initializer in the declaration, Scyode declares that variable with value nil. If an existing varaible is redeclared, that's not an issue and the variable's stored value is replaced.

### Setup/ Run Instructions
 There are no required dependancies to run Scyode (other than Python). Once you have downloaded the source code and are in your parent directory, you can access the interactive shell using ```python src/scyode.py``` or run a .vv file using ```python src/scyode [file_path]```. The files to run the tests documented below are in the lab5 folder under the test folder and can be run using ```python src/scyode test/lab5/[test_file]```.

### Test Cases

1. var_decl.vv

    This test demonstrates a functioning variable declaration and access system.

    Input:
    ```
    var a = "variable";
    print a;
    ```

    Expected Output:
    ```
    variable
    ```

    Actual Output:
    ```
    variable
    ```

    Matches Expected: ✔

2. var_assign.vv

    This test demonstrates a functioning variable assignment and access system.

    Input:
    ```
    var b = "old";
    print b;
    b = "new";
    print b;
    ```

    Expected Output:
    ```
    old
    new
    ```

    Actual Output:
    ```
    old
    new
    ```

    Matches Expected: ✔

3. textbook_ex.vv

    This test demonstrates a functioning block scope, as outlined in the textbook.

    Input:
    ```
    var a = "global a";
    var b = "global b";
    var c = "global c";
    {
        var a = "outer a";
        var b = "outer b";
        {
            var a = "inner a";
            print a;
            print b;
            print c;
        }
        print a;
        print b;
        print c;
    }
    print a;
    print b;
    print c;
    ```

    Output:
    ```
    inner a
    outer b
    global c
    outer a
    outer b
    global c
    global a
    global b
    global c
    ```

    Explanation: The new variables defined in the blocks shadow the variables from outside the blocks and will be accessed instead. In the innermost block, a is redefined but b and c are not so they take on the values of declarations from nested scopes, working from the inside out. The same principle applies to the outermost block, and once we are outside any blocks, and variable reflect their global declarations.

4. undefined_var.vv

    This test demonstrates the error handling of variable access before declaration.

    Input:
    ```
    b = 42;
    ```

    Expected Output:
    ```
    Undefined variable 'b'
    [line 1]
    ```

    Actual Output:
    ```
    Undefined variable 'b'
    [line 1]
    ```

    Matches Expected: ✔

5. unmatched_brace.vv

    This test demonstrates the error handling of unmatched braces in blocks.

    Input:
    ```
    {
        print "bad block";
    ```

    Expected Output:
    ```
    [line 3] Error at end: Expect '}' after block
    ```

    Actual Output:
    ```
    [line 3] Error at end: Expect '}' after block
    ```

    Matches Expected: ✔

6. invalid_assignment.vv

    This test demonstrates the error handling of invalid assignment targets.

    Input:
    ```
    var 4 = 5;
    ```

    Expected Output:
    ```
    [line 1] Error at '4': Expect variable name
    ```

    Actual Output:
    ```
    [line 1] Error at '4': Expect variable name
    ```

    Matches Expected: ✔