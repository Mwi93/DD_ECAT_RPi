#include "ethercat_motor.h"
#include "soem/ethercat.h"
#include <stdint.h>

volatile int32_t actual_position = 0;

int setup_drive(uint16 slave) {
    int8 op_mode = 0x0A;
    uint16 ctrl_word;
    ec_SDOwrite(slave, 0x6060, 0x00, FALSE, 1, &op_mode, EC_TIMEOUTSAFE);
    ctrl_word = 0x0006;
    ec_SDOwrite(slave, 0x6040, 0x00, FALSE, 2, &ctrl_word, EC_TIMEOUTSAFE);
    ctrl_word = 0x000F;
    ec_SDOwrite(slave, 0x6040, 0x00, FALSE, 2, &ctrl_word, EC_TIMEOUTSAFE);
    return 1;
}

void send_torque(uint16 slave, int16 torque) {
    ec_SDOwrite(slave, 0x6071, 0x00, FALSE, 2, &torque, EC_TIMEOUTSAFE);
}

int32_t get_position(uint16 slave) {
    int32_t pos;
    ec_SDOread(slave, 0x6064, 0x00, FALSE, NULL, &pos, EC_TIMEOUTSAFE);
    actual_position = pos;
    return pos;
}

int init_motor() {
    if (ec_init("eth0")) {
        if (ec_config_init(FALSE) > 0) {
            ec_config_map(&IOmap);
            ec_configdc();
            setup_drive(1);
            return 0;
        }
    }
    return -1;
}
