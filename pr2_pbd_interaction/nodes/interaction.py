#!/usr/bin/env python
import sys
import signal
import rospy

from pr2_pbd_interaction.Interaction import Interaction

def signal_handler(signal, frame):
    # The following makes sure the state of a user study is saved, so that it can be recovered
    global interaction
    #interaction.saveExperimentState()
    print 'Program Terminated!!'
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGQUIT, signal_handler)

if __name__ == "__main__":
    global interaction
    rospy.init_node('pr2_pbd_interaction')
    interaction = Interaction()
    #rospy.spin()
    while(not rospy.is_shutdown()):
        interaction.update()