from ulta import OrientationDetection, Orientation


def test_orientation_initialization():
    orientation_detector = OrientationDetection()
    assert orientation_detector is not None

    res = orientation_detector.detect_orientation("tests/assets/image_h.png")
    assert res == Orientation.UPRIGHT

    res = orientation_detector.detect_orientation("tests/assets/image_v.jpeg")
    assert res == Orientation.ROTATE_90_CCW
