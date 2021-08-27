"""Top-level package for luma combine."""

__author__ = """Edward Harman"""
__email__ = 'jaq@ethelred.org'
__version__ = '0.0.1'


from luma.core import mixin

class combine(mixin.capabilities):
    """
    Combine two devices into a single display. For simplicity in the initial version I'm only supporting exactly two devices in a left-right orientation.

    :param device_left: Device on the left.
    :param device_right: Device on the right.
    """
    def __init__(self, device_left, device_right):
        self.capabilities(device_left.width + device_right.width, max(device_left.height, device_right.height), rotate=0, mode="1")
        self._left = device_left
        self._right = device_right

    def display(self, image):
        leftImage = image.crop((0, 0, self._left.width, self._left.height))
        rightImage = image.crop((self._left.width, 0, self.width, self._right.height))
        self._left.display(leftImage)
        self._right.display(rightImage)
