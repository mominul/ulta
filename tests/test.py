from ulta import OrientationDetection, Orientation
from PIL import Image


def test_orientation_initialization():
    orientation_detector = OrientationDetection()
    assert orientation_detector is not None

    res = orientation_detector.detect_orientation("tests/assets/image_h.png")
    assert res == Orientation.UPRIGHT

    res = orientation_detector.detect_orientation("tests/assets/image_v.jpeg")
    assert res == Orientation.ROTATE_90_CCW

    image = Image.open("tests/assets/image_h.png")
    res = orientation_detector.detect_orientation(image)
    assert res == Orientation.UPRIGHT

    image = Image.open("tests/assets/image_v.jpeg")
    res = orientation_detector.detect_orientation(image)
    assert res == Orientation.ROTATE_90_CCW
