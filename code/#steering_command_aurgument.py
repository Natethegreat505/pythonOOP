#4/21/23
from jetracer.nvidia_racecar import nvidiaracecar
import argparse
car = nvidia_racecar()
parser = argparse.ArgumentParser()
parser.add_argument('--value', type+float, required=True)
args = parser.parse_args()
car.steering = args.value
