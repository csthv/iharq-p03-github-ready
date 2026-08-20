from .physionet_mi import MOABBPhysionetMIAdapter
from .bnci2014_001 import MOABBBNCI2014001Adapter
from .lee2019_mi import MOABBLee2019MIAdapter
ADAPTERS={
 "MOABBPhysionetMIAdapter":MOABBPhysionetMIAdapter,
 "MOABBBNCI2014001Adapter":MOABBBNCI2014001Adapter,
 "MOABBLee2019MIAdapter":MOABBLee2019MIAdapter,
}
