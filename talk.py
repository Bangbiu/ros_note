#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
def GetTwist(forward,turn):
	twi = Twist()
	twi.linear.x = forward; twi.angular.z = turn
	return twi
def Draw(vtwist,times,rates):
	delta = 0
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)
	rospy.init_node('b',anonymous = True)
	rate = rospy.Rate(rates)
	
	while not delta>=times:
		##hello_str = 'abashdgyed %s' %rospy.get_time()
		rospy.loginfo(delta)
		pub.publish(vtwist)
		delta=delta+1
		rate.sleep()
	delta=0
def talker():
	ret = Draw(GetTwist(1,1),50,10)


if __name__ =='__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
