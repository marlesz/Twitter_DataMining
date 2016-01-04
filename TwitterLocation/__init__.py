# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TwitterLocation
                                 A QGIS plugin
 Lokalizacja obiektów na podstawie wpisów z Twittera
                             -------------------
        begin                : 2015-12-29
        copyright            : (C) 2015 by ML
        email                : leszczuk.marta@gmail.com
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
    """Load TwitterLocation class from file TwitterLocation.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .TwitterLocation import TwitterLocation
    return TwitterLocation(iface)
