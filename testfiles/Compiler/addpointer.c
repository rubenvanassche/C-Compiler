int add(int* a, int *b){
  return *a + *b;
}

int multiply(int a, int b){
  return a*b;
}

int main(){
  int a = 20;
  int b = 23;
  int* c = &a;
  int* d = &b;
  int e = add(d, c);
  int f = multiply(a,b);
}
