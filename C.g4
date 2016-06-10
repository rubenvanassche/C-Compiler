grammar C;



/**
 * A C program consist of a sequence of statements in which they are ended with
 * the special symbol EOF, indicating the end of the file.
 */
program: statement*;


/**
 * A statement is a program construction that do something. For this compiler,
 * the following statements are supported:
 *
 * - empty statement
 * - BREAK statement (jumps to the end of the loop)
 * - CONTINUE statement (jumps to the begin of the loop)
 * - INCLUDE statement (includes the program on the given path)
 * - expression statement
 * - compound statement
 * - WHILE statement (repeats the given statement until the given condition
 *   evaluates to FALSE)
 * - FOR statement (evaluates the first expression, then repeats the given
 *   statement untill the second expression evaluates to FALSE, also execute
 *   the third expression at the end of the loop)
 * - type definition
 * - function declaration/definition
 */
statement
: SEMICOLON
| BREAK SEMICOLON
| CONTINUE SEMICOLON
| INCLUDE (CPATH|STRING)
| RETURN (expression|VOID)?
| expression SEMICOLON
| IF LPAREN expression RPAREN statement (ELSE statement)?
| LBRACE statement* RBRACE
| WHILE LPAREN expression RPAREN statement
| FOR LPAREN expression? SEMICOLON expression? SEMICOLON expression? RPAREN statement
| TYPEDEF basetype IDENTIFIER (LSQUAREBRACKET NUM RSQUAREBRACKET)* SEMICOLON
| basetype IDENTIFIER LPAREN (VOID|basetype IDENTIFIER? (COMMA basetype IDENTIFIER?)*)? RPAREN (SEMICOLON|LBRACE statement* RBRACE)
;


/**
 * An expression always yields a value. The following expressions are supported
 * for this compiler:
 *
 * - constants (boolean constant, character, number, real, string)
 * - negation/NOT/reference/pointer expressions
 * - nested expressions
 * - multiplication/division expresssions
 * - addition/subtraction expresssions
 * - comparisation expressions (==, !=, <=, >=, <, >)
 * - AND/OR expressions
 * - array indexing
 * - function call expression
 * - variable (assignment)
 */
expression
: TRUE|FALSE|CHAR|NUM|REAL|STRING
| variable ASSIGN expression
| variable
| (MINUS|NOT|AMPERSAND|STAR) expression|variable
| LPAREN expression RPAREN
| expression (EQUAL|NOTEQUAL|GREATERTHAN|LESSTHAN|LESSTHANOREQUAL|GREATERTHANOREQUAL) expression
| expression (AND|OR) expression
| expression LSQUAREBRACKET expression RSQUAREBRACKET
| variable (PLUS PLUS|MINUS MINUS)
| expression (STAR|SLASH) expression
| expression (PLUS|MINUS) expression
| IDENTIFIER LPAREN (expression (COMMA expression)*)? RPAREN
;

variable
: IDENTIFIER
| basetype (STAR)? IDENTIFIER
| variable LSQUAREBRACKET expression RSQUAREBRACKET
;


/**
 * The type qualifier determines which type the operand has or should be casted
 * to. The type qualifier could also be an identifier, since we have to support
 * the typedef.
 *
 * In addition, the type qualifier can have a const qualifier to indicate that
 * the value of the object cannot be changed at runtime.
 *
 * Note the difference between the following type qualifiers (hint: read it
 * backwards):
 *
 *      int* - pointer to int
 *      int const* - pointer to const int
 *      int* const - const pointer to int
 *      int const* const - const pointer to const int
 *
 * Also note that the first `const` could be on either side of the type, so:
 *
 *      const int* == int const*
 *      const int* const == int const* const
 */
basetype
: CONST basetype
| basetype (STAR|CONST)
| (VOID|IDENTIFIER)
;


// the reserved keywords/tokens for this compiler
AMPERSAND: '&';
AND: '&&';
ASSIGN: '=';
BEGINCOMMENT: '/*';
BEGININLINECOMMENT: '//';
BREAK: 'break';
COMMA: ',';
CONST: 'const';
CONTINUE: 'continue';
DQUOTE: '"';
DOT: '.';
ELSE: 'else';
ENDCOMMENT: '*/';
EQUAL: '==';
FOR: 'for';
GREATERTHAN: '>';
GREATERTHANOREQUAL: '>=';
IF: 'if';
INCLUDE: '#include';
LBRACE: '{';
LESSTHAN: '<';
LESSTHANOREQUAL: '<=';
LPAREN: '(';
LSQUAREBRACKET: '[';
MINUS: '-';
NOT: '!';
NOTEQUAL: '!=';
OR: '||';
PLUS: '+';
RBRACE: '}';
RETURN: 'return';
RPAREN: ')';
RSQUAREBRACKET: ']';
SEMICOLON: ';';
SLASH: '/';
SQUOTE: '\'';
STAR: '*';
TYPEDEF: 'typedef';
VOID: 'void';
WHILE: 'while';

// all the values
TRUE: 'true';
FALSE: 'false';
CHAR: SQUOTE . SQUOTE;
NUM: '0'|'1'..'9' ('0'..'9')*;
REAL: (NUM? DOT NUM* 'f'?)|NUM DOT 'f';
STRING: DQUOTE .*? DQUOTE;
CPATH: LESSTHAN .*? GREATERTHAN;


// A legal C identifier begins with a letter from the alphabet or an underscore
// and may be followed by alphanumeric characters, including the underscore.
IDENTIFIER: ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;

// Skip comments (as they are not a part of the AST). Also ignore whitespaces
// and newlines.
COMMENT: (BEGININLINECOMMENT .*? NEWLINE
       | BEGINCOMMENT .*? ENDCOMMENT)  -> skip
       ;

WHITESPACE: (' '|'\t')+ -> skip;
NEWLINE: '\r'? '\n'  -> skip;
