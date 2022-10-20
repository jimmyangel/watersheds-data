layer = iface.activeLayer()

features = layer.getFeatures()

index = QgsSpatialIndex(layer.getFeatures())
print ("Created spatial index")

counter = 0


for polygon in features:
    polygonId = polygon.id()
    polygon['POP_TOTAL'] = polygon['POP_EST_19']
    layer.updateFeature(polygon)
    pointOnPolygon = polygon.geometry().pointOnSurface()
    p = pointOnPolygon.asPoint()
    isect = index.intersects(QgsRectangle(p,p))
    for i in isect:
        if polygonId != i:
            candidateFeature = layer.getFeature(i)
            if candidateFeature.geometry().intersects(pointOnPolygon):
                if polygon.geometry().area() <= candidateFeature.geometry().area():
                    polygon['POP_TOTAL'] += candidateFeature['POP_EST_19']
                    layer.updateFeature(polygon)
                    counter += 1
                    print(polygon['Water_prov'], "adds population from", candidateFeature['Water_prov'])
print(counter, "polygons visited")
    
