#ifndef ETHERCAT_MOTOR_H
#define ETHERCAT_MOTOR_H
#include "soem/ethercat.h"
int init_motor();
void send_torque(uint16 slave, int16 torque);
int32_t get_position(uint16 slave);
#endif