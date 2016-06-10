int main(){
  int vector[10];
  vector[0] = 1;
  vector[1] = 1;
  for(int i = 2;i < 10;i = i + 1){
    vector[i] = vector[i-1] + vector[i-2];
  }
}
