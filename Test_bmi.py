import ET0735_Lab2.bmi as bmi


def Test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73 , 68)
    assert (result == 0)
def Test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73, 85)
    assert (result == 1)
def Test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73,50)
    assert (result == -1)