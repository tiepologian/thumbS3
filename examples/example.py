#!/usr/bin/python

from thumbs3 import ThumbS3

images = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]

thumbs = ThumbS3("AWS_ACCESS_KEY", "AWS_ACCESS_SECRET", "http://s3-eu-west-1.amazonaws.com/mybucket", 150, 150)
thumbs.setDestinationFolder("/thumbs")
thumbs.setSuffix("_thumb")
thumbs.setVerbose()

for name in images:
    thumbs.create(name)

print "Finished!"
