# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machinery', '0002_auto_20171118_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='axiscapability',
            name='machine_tool_requirement',
        ),
        migrations.RemoveField(
            model_name='electrical',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='hydraulics',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='locator',
            name='machine_tool_specification',
        ),
        migrations.RemoveField(
            model_name='machinekinematicassociation',
            name='machine_kinematic_association',
        ),
        migrations.RemoveField(
            model_name='machinesize',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='machiningsize',
            name='machining_capability',
        ),
        migrations.RemoveField(
            model_name='positioningcapability',
            name='machine_tool_requirement',
        ),
        migrations.AddField(
            model_name='installation',
            name='capacity_of_hydraulics_tank',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='electric_phase',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='electric_power',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='electrical_current',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='electrical_frequency',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='electrical_grounding',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='electrical_voltage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='machine_height',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='machine_length',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='machine_width',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='pump_outlet_pressure',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='installation',
            name='type_of_hydraulic_oil',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolrequirement',
            name='maximum_displacement_error_of_linear_axis',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolrequirement',
            name='maximum_repeatability_error_of_linear_axis',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolrequirement',
            name='number_of_axes',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolrequirement',
            name='number_of_simultaneous_axes',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolspecification',
            name='building',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolspecification',
            name='business_unit',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolspecification',
            name='cell',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolspecification',
            name='kinematics',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinetoolspecification',
            name='plant_location',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machiningcapability',
            name='machining_size_description',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='machiningcapability',
            name='machining_size_x',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machiningcapability',
            name='machining_size_y',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machiningcapability',
            name='machining_size_z',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rangeofmotion',
            name='positioning_capability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machinery.MachineToolRequirement'),
        ),
        migrations.DeleteModel(
            name='AxisCapability',
        ),
        migrations.DeleteModel(
            name='Electrical',
        ),
        migrations.DeleteModel(
            name='Hydraulics',
        ),
        migrations.DeleteModel(
            name='Locator',
        ),
        migrations.DeleteModel(
            name='MachineKinematicAssociation',
        ),
        migrations.DeleteModel(
            name='MachineSize',
        ),
        migrations.DeleteModel(
            name='MachiningSize',
        ),
        migrations.DeleteModel(
            name='PositioningCapability',
        ),
    ]
