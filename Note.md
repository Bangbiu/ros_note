# Terminal Command

## Git
### 1)git clone https://github.com/24k-milk/24k-milk.git (https://github.com/Bangbiu/ros_note.git)
### 2)git add .
### 3)git commit -a -m "add .md"

## ROS
### Turtle
* [Master]  
<font color=#FF00CC>*roscore*</font>  
* [Open Up Node]  
*rosrun turtlesim turtlesim_node*  
* [Keyboard Operating]  
*rosrun turtlesim turtle_teleop_key*  
>[Key Value]  
>[[A up  
>[[B down  
>[[C right  
>[[D left  

### ROS List
* [Topic List]  
>*rostopic list*  
* [Show Publisher Subscriber and Other Information]  
>*rostopic info {topicname}*  
* [Listen Events]  
>*rostopic echo {topicname}*  
* [Publish Message]  
>*rostopic pub {topicname} {MessageType} {Message}*  
### ROS RUN
* [Execution]  
>*rosrun {pkgname} {executable}*  
### ROS CD
* [Go to pkg's Location]  
>*roscd {pkgname}*  
### Make Workspace and Compile Package
* [Create Workspace directory]  
>*mkdir -p {workspace}*  
>*cd {workspace}*  
>*catkin_make or catkin_make -j2 []*  
>*catkin_create_pkg {pkgname} rospy {lang}*  
>*cd {workspace/devel/}*   
>*source setup.bash*  
>*mkdir {pkgname}/launch*  
>*touch {topicname}.launch*  
>*gedit .*  
### ROS Launch
* [launch]  
>*<node name="hahahh" pkg="turtlesim" type="turtlesim_node" />*  
* [launch in launch]  
>*<node name="virtualController" pkg="mx_teleop" type="virtual_joystick.py" />*  
### Gazebo
>*roslaunch mx_urdf gazebo.launch*  
### Rviz
>*roscore*  
>*rviz*  
### Rqt
>*roscore*  
>*rqt* [plugins--visualizations--plot]  
### Nav
#### Build a map
>*roslaunch mx_bringup rbc_lidar_start.launch*  
>*roslaunch mx_nav mx_gmapping.launch*  
>*roslaunch mx_rviz gmapping_view.launch*  
>*roslaunch mx_nav map_save.launch*
#### navigation 
>*roslaunch mx_bringup rbc_lidar_start.launch*
>*roslaunch mx_nav amcl_demo.launch ru*
# XML
><node name="hahahh" pkg="turtlesim" type="turtlesim_node" />  


* [BAIDU](http://www.baidu.com)*
