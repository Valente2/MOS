#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  char *num[3];
  num = (char*) malloc(5 * sizeof(string));
  switch(argc)
  {
    case 4:
      num[1] = argv[2];
      num[2] = argv[4];
      break;

    case 6:
      num[1] = argv[2];
      num[2] = argv[4];
      break;

    case 2:
      num[1] = argv[2];
      break;  
  }
  int loop;
  for(loop =0; loop < sizeof(num); loop++)
    printf("%s", num[loop]);
  free(num);
  return 0;
}
