import os.path, sys
sys.path.insert(0,'src')
from ASTBuilder import ASTBuilder
from src.SymbolTable.SymbolTable import SymbolTable
import argparse

def main(argv):
    parser = argparse.ArgumentParser(description='A C to Pcode compiler')
    parser.add_argument('file', help='The c file to be compiled')
    parser.add_argument('-o','--output', help='Directory to write compiled C file')
    parser.add_argument('-saveast','--saveast', help='Write the AST to a file',  action='store_true')
    parser.add_argument('-showast','--showast', help='Print AST',  action='store_true')
    parser.add_argument('-n','--nocompile', help='Disable the compilation phase',  action='store_true')
    args = vars(parser.parse_args())

    filepath = os.path.split(args["file"])
    filename = os.path.splitext(filepath[1])[0]
    outputpath = ""
    if(args["output"] != None):
        outputpath += args["output"] + "/"

    symboltable = SymbolTable()
    astBuilder = ASTBuilder(args["file"], symboltable)
    ast = astBuilder.build()

    print(symboltable)

    if(bool(args["nocompile"]) == False):
        compiled = ast.compile()

        # Write to file
        file = open(outputpath + filename + ".p", "w")
        file.write(compiled)
        file.close()

    # Should we serialize
    if(args["showast"] == True):
        astBuilder.serialize()

    if(args["saveast"] == True):
        file = open(outputpath + filename + ".ast", "w")
        file.write(astBuilder.serialize())
        file.close()


if __name__ == '__main__':
    main(sys.argv)
