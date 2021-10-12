__all__ = ["vietnam", "thailand"] # vietnam 모듈 공개

from travel import *
#trip_to = vietnam.VietnamPackage() # 베트남
trip_to = thailand.ThailandPackage()
trip_to.detail()