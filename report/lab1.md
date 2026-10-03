# Scyode

### Regular Expressions
- Numbers: [0-9]+(\\.[0-9]*)?
- Strings: "(\\\\"|[^"])*"
- Indentifiers: \\w+

### Design choices relative to Lox
#### Function
How my scanner functions is pretty much identical to Lox's, although I did modify a few minor things. The only relevent here is how I handled the peek() function and my additional skip() helper function. My peek() function lets you view further along the source string and lets you specify in you want the entire substring or just the last character and my skip() helper neatly handles a loop of advances. Both modifications were to aid in my alternative comment structure. My other changes are detailed in the Extra Credit section below.
#### Style
Unrelated to how the scanner actually works, I wanted to make some aesthetic alterations to how Scyode code will look.
- Comments are denoted by an at symbol (@) rather than a double slash (//) as I want that symbol to instead eventually denote floor division, like in Python. For example:
    ```
    @ normal comment

    @== 
    big 
    multi-line 
    comment 
    ==@
    ```
- This was all I had time for on this lab, but if I have extra time on the next one I may make additional cosmetic changes as I see fit.

### Setup/ Run Instructions
There are no required dependancies to run Scyode (other than Python). Once you have downloaded the source code, you can use ```python src\scyode.py``` to open the interactive shell. You can then type "quit" or use Ctrl+C to exit. To run a Scyode source file (*.vv), use ```python src\scyode.py test\lab1\[test_file]```. The files to repoduce test results are in the test folder.

### Test Cases

1. nonlit.vv

    This test shows that every defined non-literal token type is recognized by the implemented scanner.

    Input:
    ```
    (){} @ LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE
    ,.-+;* @ COMMA, DOT, MINUS, PLUS, SEMICOLON, STAR
    !=! === <=< @ BANG_EQUAL, BANG, EQUAL_EQUAL, EQUAL, LESS_EQUAL, LESS
    >=> /// @ GREATER_EQUAL, GREATER, DOUBLE_SLASH, SLASH
    @ EOF
    ```
    Output:
    ```
    TokenType.LEFT_PAREN ( None
    TokenType.RIGHT_PAREN ) None
    TokenType.LEFT_BRACE { None
    TokenType.RIGHT_BRACE } None
    TokenType.COMMA , None
    TokenType.DOT . None
    TokenType.MINUS - None
    TokenType.PLUS + None
    TokenType.SEMICOLON ; None
    TokenType.STAR * None
    TokenType.BANG_EQUAL != None
    TokenType.BANG ! None
    TokenType.EQUAL_EQUAL == None
    TokenType.EQUAL = None
    TokenType.LESS_EQUAL <= None
    TokenType.LESS < None
    TokenType.GREATER_EQUAL >= None
    TokenType.GREATER > None
    TokenType.DOUBLE_SLASH // None
    TokenType.SLASH / None
    TokenType.EOF  None
    ```
    Matches Expected: ✔
2. lit.vv

    This test shows that every defined literal token is recognized by the implemented scanner.

    Input:
    ```
    456 3.14 @ NUMBER, NUMBER
    "hello" "" @ STRING, STRING
    test_var f1 @ IDENTIFIER, IDENTIFIER
    " @ unterminated string
    ```
    Output:
    ```
    [line 4] Error: Unterminated string
    TokenType.NUMBER 456 456.0
    TokenType.NUMBER 3.14 3.14
    TokenType.STRING "hello" hello
    TokenType.STRING "" 
    TokenType.IDENTIFIER test_var None
    TokenType.IDENTIFIER f1 None
    TokenType.EOF  None
    ```
    Matches Expected: ✔
3. keywords.vv

    This test shows that every defined keyword token is recognized by the implemented scanner.

    Input:
    ```
    and class else false for @ AND, CLASS, ELSE, FALSE, FOR
    fun if nil or print return @ FUN, IF, NIL, OR, PRINT, RETURN
    super this true var while @ SUPER, THIS, TRUE, VAR, WHILE
    ```
    Output:
    ```
    TokenType.AND and None
    TokenType.CLASS class None
    TokenType.ELSE else None
    TokenType.FALSE false None
    TokenType.FOR for None
    TokenType.FUN fun None
    TokenType.IF if None
    TokenType.NIL nil None
    TokenType.OR or None
    TokenType.PRINT print None
    TokenType.RETURN return None
    TokenType.SUPER super None
    TokenType.THIS this None
    TokenType.TRUE true None
    TokenType.VAR var None
    TokenType.WHILE while None
    TokenType.EOF  None
    ```
    Matches Expected: ✔
4. comments.vv

    This test shows that comments are ignored by the scanner, that both inline and multi-line comments function, and will report an unclosed multi-line comment.

    Input:
    ```
    @ this will not be output
    @ even if there are literals
    @ "hello" 213 !!!

    @==
    and they
    can be long
    ==@

    @== oops!
    ```
    Output:
    ```
    [line 10] Error: Unterminated comment
    TokenType.EOF  None
    ```
    Matches Expected: ✔
5. Interactive shell

    This test shows that the interactive shell is functional in that it reads input, continues after error, and can be exited. You can copy-paste each line after the '>>>' into the terminal yourself to verify the output.

    Terminal:
    ```
    python src\scyode.py                      
    >>>>> Interactive Shell <<<<<
    >>> hello
    TokenType.IDENTIFIER hello None
    TokenType.EOF  None
    >>> "hello"
    TokenType.STRING "hello" hello
    TokenType.EOF  None
    >>> []
    [line 1] Error: Unexpected character
    [line 1] Error: Unexpected character
    TokenType.EOF  None
    >>> 1+2
    TokenType.NUMBER 1 1.0
    TokenType.PLUS + None
    TokenType.NUMBER 2 2.0
    TokenType.EOF  None
    >>> quit
    ..... Exiting Shell .....
    ```
    Matches Expected: ✔
6. bad_file.txt

    This test shows that the scanner will not scan a file of incorrect type.

    Input:
    ```
    python src\scyode.py test\lab1\bad_file.txt
    ```
    Output:
    ```
    [line 0] Error: Can only run .vv files
    ```
    Matches Expected: ✔
7. Incorrect source call

    This test shows that the source code will not be run if called incorrectly.

    Input:
    ```
    python src\scyode.py 1 2 3 
    ```
    Output:
    ```
    [line 0] Error: Usage: python scyode.py [script]
    ```
    Matches Expected: ✔

### Known Limitations
There are not any limitations in the scanner that I can think of that detract from its intended design. Some quality of life aspects and extended use cases that are handled by modern languages (e.g. additional numerical formats, leading or trailing decimal points, nested comments, etc.) were intentionally ommited/not immplemented due to scope.

# Extra Credit

### String Escape Sequences
String escape seqences are extremely useful for formating outputted text in a neat and easy way, which is why I optted to include them in my scanner. The escape sequences implented are the ones I use and feel are the most important are as follows:
- Quote (\\")
- Backslash (\\\\)
- New line (\\n)
- Tab (\\t)

Testing the file escape_seq.vv reveals these seqences working in action.

Input:
```
"This -> \" is an escaped quote" 
"This -> \\ is an escaped backslash" 
"This -> \n is an escaped newline" 
"This -> \t is an escaped tab" 
```
Output:
```
TokenType.STRING "This -> \" is an escaped quote" This -> " is an escaped quote
TokenType.STRING "This -> \\ is an escaped backslash" This -> \ is an escaped backslash
TokenType.STRING "This -> \n is an escaped newline" This -> 
 is an escaped newline
TokenType.STRING "This -> \t is an escaped tab" This ->          is an escaped tab
TokenType.EOF  None
```
Matches Expected: ✔