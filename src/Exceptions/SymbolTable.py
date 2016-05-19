class ScopeError(RuntimeError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class SymbolError(RuntimeError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class SymbolNotRegisteredError(SymbolError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class SymbolAlreadyRegisteredError(SymbolError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class TypeError(RuntimeError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class FunctionError(RuntimeError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class FunctionNotRegisteredError(FunctionError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class FunctionAlreadyRegisteredError(FunctionError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class AliasError(RuntimeError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class AliasNotRegisteredError(AliasError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)

class AliasAlreadyRegisteredError(AliasError):
   def __init__(self, arg):
      self.args = arg
   def __str__(self):
      return ''.join(self.args)
