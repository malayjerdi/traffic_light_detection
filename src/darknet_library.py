import rospy
from ctypes import *
import darknet_class

darknet_library = rospy.get_param("/darknet_library")
lib = CDLL(darknet_library, RTLD_GLOBAL)
lib.network_width.argtypes = [c_void_p]
lib.network_width.restype = c_int
lib.network_height.argtypes = [c_void_p]
lib.network_height.restype = c_int

predict = lib.network_predict
predict.argtypes = [c_void_p, POINTER(c_float)]
predict.restype = POINTER(c_float)

set_gpu = lib.cuda_set_device
set_gpu.argtypes = [c_int]

make_image = lib.make_image
make_image.argtypes = [c_int, c_int, c_int]
make_image.restype = darknet_class.IMAGE

get_network_boxes = lib.get_network_boxes
get_network_boxes.argtypes = [c_void_p, c_int, c_int, c_float, c_float, POINTER(c_int), c_int, POINTER(c_int)]
get_network_boxes.restype = POINTER(darknet_class.DETECTION)

make_network_boxes = lib.make_network_boxes
make_network_boxes.argtypes = [c_void_p]
make_network_boxes.restype = POINTER(darknet_class.DETECTION)

free_detections = lib.free_detections
free_detections.argtypes = [POINTER(darknet_class.DETECTION), c_int]

free_ptrs = lib.free_ptrs
free_ptrs.argtypes = [POINTER(c_void_p), c_int]

network_predict = lib.network_predict
network_predict.argtypes = [c_void_p, POINTER(c_float)]

reset_rnn = lib.reset_rnn
reset_rnn.argtypes = [c_void_p]

load_net = lib.load_network
load_net.argtypes = [c_char_p, c_char_p, c_int]
load_net.restype = c_void_p

do_nms_obj = lib.do_nms_obj
do_nms_obj.argtypes = [POINTER(darknet_class.DETECTION), c_int, c_int, c_float]

do_nms_sort = lib.do_nms_sort
do_nms_sort.argtypes = [POINTER(darknet_class.DETECTION), c_int, c_int, c_float]

free_image = lib.free_image
free_image.argtypes = [darknet_class.IMAGE]

letterbox_image = lib.letterbox_image
letterbox_image.argtypes = [darknet_class.IMAGE, c_int, c_int]
letterbox_image.restype = darknet_class.IMAGE

load_meta = lib.get_metadata
lib.get_metadata.argtypes = [c_char_p]
lib.get_metadata.restype = darknet_class.METADATA

load_image = lib.load_image_color
load_image.argtypes = [c_char_p, c_int, c_int]
load_image.restype = darknet_class.IMAGE

rgbgr_image = lib.rgbgr_image
rgbgr_image.argtypes = [darknet_class.IMAGE]

predict_image = lib.network_predict_image
predict_image.argtypes = [c_void_p, darknet_class.IMAGE]
predict_image.restype = POINTER(c_float)