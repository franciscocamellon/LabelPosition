# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LabelPosition
                                 A QGIS plugin
 This plugin rotate the label around a point feature
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-03-12
        copyright            : (C) 2019 by Francisco CamelloN
        email                : franciscocamellon@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LabelPosition class from file LabelPosition.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LabelPosition import LabelPosition
    return LabelPosition(iface)
