all:
	echo "Nothing at this moment"

# Download dependencys
configure:
	wget http://www.antlr.org/download/antlr-4.5.3-complete.jar -P /usr/local/lib
	export CLASSPATH=".:/usr/local/lib/antlr-4.5.3-complete.jar:$CLASSPATH"
	alias antlr4='java -jar /usr/local/lib/antlr-4.5.3-complete.jar'
	alias grun='java org.antlr.v4.gui.TestRig'
	python3 -m pip install antlr4-python3-runtime

# Set Antlr path
antlr4 = java -jar /usr/local/lib/antlr-4.5.3-complete.jar

# Generate the ANTLR grammer
generate:
	$(antlr4) -Dlanguage=Python3 C.g4 -o src/

test:
	python3 -m unittest discover

testold:
	python3 Compiler.py testfiles/ast/main.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/arithmetic.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/array.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/assignment.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/compoundstatement.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/const.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/constantexpression.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/function.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/functioncall.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/if.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/include.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/negatenot.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/typedef.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/variables.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/while.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/for.c -showast -o testoutput
	python3 Compiler.py testfiles/ast/return.c -showast -o testoutput

testsymbol:
	python3 Compiler.py testfiles/Symboltable/test1.c
	python3 Compiler.py testfiles/Symboltable/test2.c
	python3 Compiler.py testfiles/Symboltable/test3.c
	python3 Compiler.py testfiles/Symboltable/test4.c
	python3 Compiler.py testfiles/Symboltable/test5.c
	python3 Compiler.py testfiles/Symboltable/test6.c
	python3 Compiler.py testfiles/Symboltable/test7.c
	python3 Compiler.py testfiles/Symboltable/test8.c
	python3 Compiler.py testfiles/Symboltable/test9.c
	python3 Compiler.py testfiles/Symboltable/test10.c
	python3 Compiler.py testfiles/Symboltable/test11.c
	python3 Compiler.py testfiles/Symboltable/test12.c
	python3 Compiler.py testfiles/Symboltable/test13.c
