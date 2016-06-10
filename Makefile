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
	python3 Compiler.py testfiles/AST/logic.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/multivar.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/pointers.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/io.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/main.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/arithmetic.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/array.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/assignment.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/compoundstatement.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/const.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/constantexpression.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/function.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/functioncall.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/if.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/include.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/negatenot.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/typedef.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/variables.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/while.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/for.c -showast -o testoutput
	python3 Compiler.py testfiles/AST/return.c -showast -o testoutput

testcompiler:
	python3 Compiler.py testfiles/Compiler/basic.c -showast -o testoutput/Compiler
	python3 Compiler.py testfiles/Compiler/fact.c -showast -o testoutput/Compiler


testcrash:
	python3 Compiler.py testfiles/Crashes/2io3.c -showast -o testoutput
	python3 Compiler.py testfiles/Crashes/4control2.c -showast -o testoutput
	python3 Compiler.py testfiles/Crashes/4control3.c -showast -o testoutput
	python3 Compiler.py testfiles/Crashes/4control6.c -showast -o testoutput
	python3 Compiler.py testfiles/Crashes/7function2.c -showast -o testoutput
