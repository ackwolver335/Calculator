# here is a Module related to the Outcomes of your BMI ensuring your health status
# This contains only a single class in which you have to enter the data once and get the data in that contain default functions


class BMI:
    weight = 0
    height_in_cm = 0
    height_in_m = 0
    height_in_foot = 0
    height_in_inch = 0

    def __init__(self, m = 0, cm = 0, foot = 0, inches = 0,wgt = 0):
        self.weight = wgt
        self.height_in_cm = cm
        self.height_in_m = m
        self.height_in_foot = foot
        self.height_in_inch = inches

    def heightinch(self):
        height = self.height_in_inch * 0.0254
        weight = self.weight
        convertion = weight / (height ** 2)
        return convertion

    def heightmtr(self):
        height = self.height_in_m
        weight = self.weight
        convertion = weight / (height ** 2)
        return convertion

    def heightcm(self):
        height = self.height_in_cm / 100
        weight = self.weight
        convertion = weight / (height ** 2)
        return convertion

    def heightfoot(self):
        height = self.height_in_foot * 0.304
        weight = self.weight
        convertion = weight / (height ** 2)
        return convertion