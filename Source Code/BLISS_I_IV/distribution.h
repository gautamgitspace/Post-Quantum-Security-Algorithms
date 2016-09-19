#ifndef DISTRIBUTION_H
#define DISTRIBUTION_H

#include <stdint.h>

/*initialize parameter sets 0..4*/
void gauss_init();

/*sample from the given set*/
int32_t gauss_sample(int set);

#endif
