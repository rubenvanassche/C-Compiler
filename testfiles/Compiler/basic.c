int add(int a, int b);

int main(){
  int a = add(5,6);
  int b = 0;
  while(b < a){
    b = b + 1;
  }
}

int add(int a, int b){
  return a + b;
}
