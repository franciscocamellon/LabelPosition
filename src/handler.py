from PyQt5.QtCore import QSettings, QTranslator, qVersion, QVariant
from PyQt5.QtWidgets import QAction, QMessageBox
from qgis.core import QgsProject, QgsWkbTypes, QgsField, QgsFields
from qgis.utils import *


class Manager:

    def __init__(self, iface):
        self.iface = iface

    def setQuadrantPos(self):

        # layer = QgsProject.instance().mapLayersByName(
        #     'rel_ponto_cotado_altimetrico_p')[0]
        layer = self.iface.activeLayer()
        selection = layer.selectedFeatures()
        n_sel = layer.selectedFeatureCount()

        if n_sel > 0:
            layer.startEditing()
            for feature in selection:
                pos = feature['offset_quad']
                pos = 0 if not pos else int(pos)
                if pos < 8:
                    pos += 1
                    layer.changeAttributeValue(feature.id(), 4, pos)
                    layer.triggerRepaint()
                elif pos == 8:
                    pos = 0
                    layer.changeAttributeValue(feature.id(), 4, pos)
                    layer.triggerRepaint()
                else:
                    pos = 0
                    layer.changeAttributeValue(feature.id(), 4, pos)
                    layer.triggerRepaint()
            layer.commitChanges()
        else:
            QMessageBox.critical(iface.mainWindow(), "Error",
                                 "Please select at least one feature from rel_ponto_cotado_altimetrico_p layer!")

    def validate_field(self):
        field_index = layer.fields().indexFromName(field_name)

        for feature in layer.getFeatures():
            try:
                # Throws exception if it does not exist
                feature.attribute("fieldName")
                found = true
            except KeyError as e:
                # all features have hte same fields, so if it doesn't exists in the first feature, it won't exist in the others
                break
            finally:
                # all features have the same fields, so only need to check the first
                break


""""
    def geomHandler(self):
        layer = iface.activeLayer()
        selection = layer.selectedFeatures()
        n_sel = layer.selectedFeatureCount()
        #features = layer.getFeatures()
        for feature in self.n_sel:
        # retrieve every feature with its geometry and attributes
        print("Feature ID: ", feature.id())
        # fetch geometry
        # show some information about the feature geometry
        geom = feature.geometry()
        geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
        if geom.type() == QgsWkbTypes.PointGeometry:
        # the geometry type can be of single or multi type
            if geomSingleType:
                x = geom.asPoint()
            pass
            elif:
                x = geom.asMultiPoint()
            print("MultiPoint: ", x)
        elif geom.type() == QgsWkbTypes.LineGeometry:
"""
