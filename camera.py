#!/usr/bin/python

import sys

import qrtools
print ("start", sys.argv[1])

fil=sys.argv[1]

cid=sys.argv[2]
posx=sys.argv[3]
posy=sys.argv[4]

camera = {
	"cameraId" : cid,
	"pos" : {"x" : posx, "y": posy},
	"carrageId" : "0"
}

qr = qrtools.QR()
qr.decode(fil)
if qr.data != "NULL":
	camera["carrageId"] = qr.data


print(camera)




