#include <stdio.h>
#include <math.h> 

int main(int argc, char *argv[])
{
  int num;
  switch(argc)
  {
    case 4:
      int num[] = (int) {argv[2], argv[4]};
      break;

    case 6:
      int num[] = (int) {argv[2], argv[4], argv[6]};
      break;

    case 2:
      int num[] = (int) argv[2];
      break;  
  }
  printf(num[]);
  return 0;
}
