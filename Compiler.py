import os.path, sys
sys.path.insert(0,'src')
from ASTBuilder import ASTBuilder

def main(argv):
    astBuilder = ASTBuilder(argv[1])
    ast = astBuilder.build()




if __name__ == '__main__':
    main(sys.argv)
