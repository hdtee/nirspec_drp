#import numpy as np

class Order:
    
    def __init__(self, orderNum):
        
        self.orderNum = orderNum
        self.integrationTime = 0.0
        self.yOffset = -1
        
        # pixel location of left hand end of top and bottom of order 
        # calc are locations based on evaluation of grating equation
        # meas are locations from analyzing the image and finding the 
        # actual edge of the order on the detector
        self.topCalc = 0.0
        self.topMeas = 0.0
        self.botCalc = 0.0
        self.botMeas = 0.0
        
        self.wavelengthScaleCalc = []
        #self.wavelengthShift = 0.0 this value is logged but not needed otherwise
        self.wavelengthScaleMeas = []
        
        # wavelength calibration lines, array of class WavelengthCalLine
        self.lines = []
        
        self.padding = 0
        
        self.objCutout = []
        self.flatCutout = []
        self.onOrderMask = []
        self.offOrderMask = []
        
        self.topTrace = []
        self.botTrace = []
        self.avgTrace = []
        self.smoothedTrace = []
        self.traceMask = []
        self.spectralTrace = []
        self.shiftOffset = 0
        
        self.flatNormalized = False
        self.flattened = False
        self.spatialRectified = False
        self.spectralRectified = False

        self.flatMean = 0.0
        
        self.flatImg = []
        self.normalizedFlatImg = []
        self.objImg = []
        self.flattenedObjImg = []
        self.noiseImg = []
        
        self.spatialProfile = []
        self.peakLocation = 0
        
        self.objWindow = []
        self.topSkyWindow = []
        self.botSkyWindow = []
        
        self.objSpec = []
        self.noiseSpec = []
        self.skySpec = []
        self.synthesizedSkySpec = []