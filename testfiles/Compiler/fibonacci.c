void main(){
  int vector[10];
  vector[0] = 1;
  for(int i = 1;i < 10;i = i + 1){
    vector[i] = vector[i - 1] + 2;
  }
}
