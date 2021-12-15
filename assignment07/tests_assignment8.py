import Assignment8Objects as AO
import pytest

def test_exit():

    exitTest = AO.Booking()
    exit_1 = exitTest.system_exit(True)
    assert exit_1 == 1

def test_shippable_1():

     shippable_test = AO.Booking()
     shippable_1 = shippable_test.determine_if_shippable(126, 12)
     assert shippable_1 == 1

def test_shippable_2():

    shippable_test = AO.Booking()
    shippable_2 = shippable_test.determine_if_shippable(23, 12)
    assert shippable_2 == 1


def test_shippable_3():
    shippable_test = AO.Booking()
    shippable_3 = shippable_test.determine_if_shippable(134, 6)
    assert shippable_3 == 1

def test_shippable_4():
    shippable_test = AO.Booking()
    shippable_4 = shippable_test.determine_if_shippable(100, 6)
    assert shippable_4 == True

def test_get_volume():

    volume_test = AO.Booking()
    volume_test_1 = volume_test.get_volume(5,5,5)
    assert volume_test_1 == 125

    volume_test = AO.Booking()
    volume_test_2 = volume_test.get_volume(3, 3, 3)
    assert volume_test_2 == 27


def test_set_weight_boundaries():

    weight_test = AO.Booking()
    weight_test_1 = weight_test.set_weight_boundaries(9)
    assert weight_test_1 == 'heavy'

    weight_test_1 = weight_test.set_weight_boundaries(1)
    assert weight_test_1 == 'light'

def test_air_fare():

    air_fare_test = AO.Booking()
    air_fare_test_1 = air_fare_test.determine_air_fare(10, 125)
    assert air_fare_test_1 == 2500


    air_fare_test_2 = air_fare_test.determine_air_fare(1, 20)
    assert air_fare_test_2 == 400

    air_fare_test_2 = air_fare_test.determine_air_fare(5, 1)
    assert air_fare_test_2 == 50

def test_urgency():

    urgency_test = AO.Booking()
    urgency_test_1 = urgency_test.determine_urgency('1')
    assert urgency_test_1 == True

    urgency_test_2 = urgency_test.determine_urgency('0')
    assert urgency_test_2 == False

def test_logistics_planning_1():

    logistics_test = AO.Booking()
    logistics_test.check_contents('0')
    logistics_test_1 = logistics_test.logistics_planning(True, True, 9, 98, True)
    assert logistics_test_1 == 1960

def test_logistics_planning_2():


    logistics_test = AO.Booking()
    logistics_test.check_contents('1')
    logistics_test.set_weight_boundaries(8)
    logistics_test.set_dimension_boundaries(52)
    logistics_test_2 = logistics_test.logistics_planning(True, True, 8, 52, True)
    assert logistics_test_2 == 45

def test_dangerous_content():

    content_test = AO.Booking()
    content_test_1 = content_test.check_contents('1')
    assert content_test_1 == True

def test_logistics_planning_3():

    logistics_test = AO.Booking()
    logistics_test.check_contents('0')
    logistics_test.set_weight_boundaries(7)
    logistics_test.set_dimension_boundaries(25)
    logistics_test_1 = logistics_test.logistics_planning(True,False, 7, 25, True)
    assert logistics_test_1 == 500

    logistics_test = AO.Booking()
    logistics_test.check_contents('1')
    logistics_test.set_weight_boundaries(7)
    logistics_test.set_dimension_boundaries(25)
    logistics_test_2 = logistics_test.logistics_planning(True, False, 7, 25, False)
    assert logistics_test_2 == 20

    logistics_test = AO.Booking()
    logistics_test.check_contents('0')
    logistics_test.set_weight_boundaries(9)
    logistics_test.set_dimension_boundaries(77)
    logistics_test_2 = logistics_test.logistics_planning(True, False, 9, 77, True)
    assert logistics_test_2 == 1540

    logistics_test = AO.Booking()
    logistics_test.check_contents('1')
    logistics_test.set_weight_boundaries(5)
    logistics_test.set_dimension_boundaries(77)
    logistics_test_2 = logistics_test.logistics_planning(True, False, 5, 77, True)
    assert logistics_test_2 == 45

    logistics_test = AO.Booking()
    logistics_test.check_contents('1')
    logistics_test.set_weight_boundaries(8)
    logistics_test.set_dimension_boundaries(77)
    logistics_test_2 = logistics_test.logistics_planning(True, False, 8, 77, True)
    assert logistics_test_2 == 45