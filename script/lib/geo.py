from math import *

#http://www.oc.nps.edu/oc2902w/coord/llhxyz.htm

class Geo( object ):
    def __init__( self ):
        print( "geo init" )
        self.dtr = pi/180.0
        self.EARTH_A = 6378.137
        self.EARTH_B = 6356.752314245179
        self.ecc = 0.08181919084262157

    # def simpleCoorToXyz(  self, _lat, _lon, _r ):
    #
    #     # angle = _lon * pi/180 #radians
    #     # center = [0,0]
    #     # _x = float( center[0] + (radius * cos(angle)) )
    #     # _y = float( center[1] + (radius * sin(angle)) )
    #
    #     x = cos( _lat ) * cos( _lon ) * _r
    #     y = cos( _lat ) * sin( _lon ) * _r
    #     z = sin( _lat ) * _r
    #
    #     return [ x, y, z ]

    def setEarthRadius( self, _r ):
        self.EARTH_A = _r
        self.EARTH_B = _r

    def coorToXyz( self, _lat, _lon, _altkm ):
        dtr =  self.dtr
        ecc = self.ecc
        esq = ecc*ecc

        flat = float( _lat )
        clat = cos( dtr * _lat )
        slat = sin( dtr * _lat )
        clon = cos( dtr * _lon )
        slon = sin( dtr * _lon )

        rn  = self.radcur( flat )[1];

        x = ( rn + _altkm ) * clat * clon
        y = ( rn + _altkm ) * clat * slon
        z = ( ( 1-esq ) * rn + _altkm ) * slat

        return [ x, y, z ]


    def radcur( self, _lat ):
        dtr = self.dtr

        a = self.EARTH_A
        b = self.EARTH_B

        asq   = a * a
        bsq   = b * b
        eccsq  =  1 - bsq / asq
        ecc = sqrt( eccsq )

        clat  =  cos( dtr * _lat )
        slat  =  sin( dtr * _lat )

        dsq   =  1.0 - eccsq * slat * slat

        rn    =   a / sqrt( dsq )
        rm    =  rn * (1.0 - eccsq ) / dsq

        rho   =  rn * clat
        z     =  (1.0 - eccsq ) * rn * slat
        r     =  sqrt( rho * rho + z * z )

        return [ r, rn, rm ]
