#!usr/bin/env python3

from lib.Driving import Driving
from lib.Navigator import Navigator
from lib.Server import Server
from lib.Sonar import Sonar

try:
    dis = Sonar()
    motor = Driving()
    server = Server(8081)
    nav = Navigator()

    dis.run()

    nav.set_sonar(dis)
    nav.set_driving(motor)
    nav.run()
    dis.set_callback(nav.set_running)

    server.set_sonar(dis)
    server.set_navigator(nav)
    server.set_driving(motor)
    server.run()
except(KeyboardInterrupt, SystemExit):
    print('\n! Received keyboard interrupt, quitting threads.\n')
    nav.__del__()
    dis.__del__()
    motor.__del__()
