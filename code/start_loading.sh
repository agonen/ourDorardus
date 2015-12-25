#!/bin/bash
nohup python ./gp_test_all_fields.py > /tmp/load.log &
echo loading started take a look at /tmp/load.log for progress
