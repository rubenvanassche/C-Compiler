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
	python3 Compiler.py testfiles/ast/arithmetic.c -saveast
	python3 Compiler.py testfiles/ast/assignment.c -saveast
	python3 Compiler.py testfiles/ast/compoundstatement.c -saveast
	python3 Compiler.py testfiles/ast/const.c -saveast
	python3 Compiler.py testfiles/ast/constantexpression.c -saveast
	python3 Compiler.py testfiles/ast/for.c -saveast
	python3 Compiler.py testfiles/ast/function.c -saveast
	python3 Compiler.py testfiles/ast/functioncall.c -saveast
	python3 Compiler.py testfiles/ast/if.c -saveast
	python3 Compiler.py testfiles/ast/include.c -saveast
	python3 Compiler.py testfiles/ast/negatenot.c -saveast
	python3 Compiler.py testfiles/ast/typedef.c -saveast
	python3 Compiler.py testfiles/ast/variables.c -saveast
	python3 Compiler.py testfiles/ast/while.c -saveast
