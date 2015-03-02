import numpy as np

from mbuild.coordinate_transform import x_axis_transform, translate
from mbuild.compound import Compound
from mbuild.port import Port


class Silane(Compound):
    """An Si(OH)2 group with two ports. """
    def __init__(self, ):
        super(Silane, self).__init__()
        self.append_from_file('silane.pdb', relative_to_module=self.__module__)

        # Transform the coordinate system such that the silicon atom is at the
        # origin and the oxygen atoms are on the x axis.
        x_axis_transform(self, new_origin=self.Si[0], point_on_x_axis=self.O[0])

        # Add bottom port.
        self.add(Port(anchor=self.Si[0]), 'down')
        translate(self.down, np.array([0, -.07, 0]))

        # Add top port.
        self.add(Port(anchor=self.Si[0]), 'up')
        translate(self.up, np.array([0, .07, 0]))

if __name__ == "__main__":
    m = Silane()
    m.visualize(show_ports=True)