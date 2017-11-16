from django.db import models

from machinery import schemas


class ElementCapability(models.Model):
    description = schemas.SupportResource.text()

    class Meta:
        abstract = True


class Tailstock(ElementCapability):
    spindle_name = schemas.SupportResource.label()
    taper = schemas.SupportResource.label()
    maximum_workpiece_weight_of_quill = schemas.Measure.mass()


class Coolant(ElementCapability):
    coolant_type = schemas.Enumerations.coolant_type()
    means_of_delivery = schemas.Enumerations.means_of_coolant_delivery()
    capacity_of_coolant_tank = schemas.Measure.volume(null=True, blank=True)
    coolant_weight = schemas.Measure.mass(null=True, blank=True)


class BarFeeder(ElementCapability):
    minimum_stock_diameter = schemas.Measure.length()
    maximum_stock_diameter = schemas.Measure.length()
    maximum_stock_length = schemas.Measure.length()


class Collet(ElementCapability):
    collet_type = schemas.SupportResource.label()
    minimum_part_diameter = schemas.Measure.length()
    maximum_part_diameter = schemas.Measure.length()


class Chuck(ElementCapability):
    minimum_part_diameter = schemas.Measure.length()
    maximum_part_diameter = schemas.Measure.length()
    number_of_jaws = schemas.Measure.count()