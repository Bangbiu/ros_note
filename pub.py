#!/usr/bin/env python

import rospy
from std_msgs.msg import string
def talker():
	pub = rospy.piblisher('a',string,queue_size = 10)
	rospy.init_node('b',anonymous = true)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		hello_str = 'abashdgyed %s' %rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
	if __name__ =='__main__'
		try:
			taker()
		except rospy.ROSinterruptException:
			pass
