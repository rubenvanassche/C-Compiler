import os.path, sys
sys.path.insert(0,'src')
from ASTBuilder import ASTBuilder

def main(argv):
    # Case no file was defined
    if(len(argv) == 1):
        print("C2P Compiler")
        print("------------")
        print("usage: Compiler.py [file.c] [-saveast]")
        return

    # Let's work
    if(len(argv) >= 2):
        print("C2P Compiler")
        print("------------")

    astBuilder = ASTBuilder(argv[1])
    ast = astBuilder.build()
    #compiled = ast.compile()

    # Write to file
    #file = open("compiled.p", "w")
    #file.write(compiled)
    #file.close()

    print("Compilation complete!")

    # Should we serialize
    if(len(argv) > 2 and argv[2] == "-saveast"):
        astBuilder.serialize()




if __name__ == '__main__':
    main(sys.argv)
