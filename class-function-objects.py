class girafee:
    def left(self):
        print("left forward")
        print("left backward")
        print("left backward")
    def right(self):
        print("right forward")
        print("rihgt backward")
        print("right forward")
    def dance(self):
        self.left()
        self.right()


# Output:
# >>> san = girafee()
#
# >>> san.dance()
# left forward
# left backward
# left backward
# right forward
# rihgt backward
# right forward
