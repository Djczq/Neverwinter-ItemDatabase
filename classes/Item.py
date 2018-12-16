# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, lang, svalue, bvalue, itemlvl, reqlvl, rpvalue, quantity, plvl, profession, commission, morale, time, focusMin, focusMax, proficiency):
        self.name = name
        self.lang = lang
        self.materials = []
        self.svalue = svalue
        self.bvalue = bvalue
        self.itemlvl = itemlvl
        self.reqlvl = reqlvl
        self.rpvalue = rpvalue
        self.quantity = quantity
        self.plvl = plvl
        self.profession = profession
        self.commission = commission
        self.morale = morale
        self.time = time
        self.focusMin = focusMin
        self.focusMax = focusMax
        self.proficiency = proficiency

    def addMaterial(self, quantity, materialName):
        self.materials.append((quantity, materialName))

    def __str__(self):
        s = self.name + ","
        s += str(self.svalue) + ","
        s += str(self.bvalue) + ","
        s += str(self.itemlvl) + ","
        s += str(self.reqlvl) + ","
        s += str(self.rpvalue) + ","
        s += str(self.quantity) + ","
        s += str(self.plvl) + ","
        s += str(self.profession) + ","
        s += str(self.commission) + ","
        s += str(self.morale) + ","
        s += str(self.time) + ","
        s += str(self.focusMin) + ","
        s += str(self.focusMax) + ","
        s += str(self.proficiency) + ","
        s += str(self.materials)
        return s


if __name__ == "__main__":
    print "test"
    i = Item("MyItem")
    i.addMaterial(1, "mat1")
    i.addMaterial(2, "mat2")
    print i