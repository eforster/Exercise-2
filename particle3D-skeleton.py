"""
 CompMod Ex2: Particle3D, a class to describe point particles in 3D space

 An instance describes a particle in Euclidean 3D space: 
 velocity and position are [3] arrays

 Includes time integrator methods +...

author: ---------------

"""
import math
import numpy as np


class Particle3D(object):
    """
    Class to describe point-particles in 3D space

        Properties:
    label: name of the particle
    mass: mass of the particle
    pos: position of the particle
    vel: velocity of the particle

        Methods:
    __init__
    __str__
    kinetic_e  - computes the kinetic energy
    momentum - computes the linear momentum
    update_pos - updates the position to 1st order
    update_pos_2nd - updates the position to 2nd order
    update_vel - updates the velocity

        Static Methods:
    new_p3d - initializes a P3D instance from a file handle
    sys_kinetic - computes total K.E. of a p3d list
    com_velocity - computes total mass and CoM velocity of a p3d list
    """

    def __init__(self, label, mass, position, velocity):
        """
        Initialises a particle in 3D space

        :param label: String w/ the name of the particle
        :param mass: float, mass of the particle
        :param position: [3] float array w/ position
        :param velocity: [3] float array w/ velocity
        """
        CODE


    def __str__(self):
        """
        XYZ-compliant string. The format is
        <label>    <x>  <y>  <z>
        """
        CODE
        return xyz_string


    def kinetic_e(self):
        """
        Returns the kinetic energy of a Particle3D instance

        :return ke: float, 1/2 m v**2
        """
        CODE
        return ???


    def momentum(_fill_in_the_blank_):
        """
        FILL IN YOUR DOCSTRING COMMENT
        """
        CODE
        return ???


    def update_pos(self, dt):
        """
        FILL IN YOUR DOCSTRING COMMENT
        """
        CODE


    def update_pos_2nd(_fill_in_the_blank_):
        """
        FILL IN YOUR DOCSTRING COMMENT
        """
        CODE


    def update_vel(_fill_in_the_blank_):
        """
        FILL IN YOUR DOCSTRING COMMENT
        """
        CODE


    @staticmethod
    def new_p3d(file_handle):
        """
        Initialises a Particle3D instance given an input file handle.
        
        The input file should contain one line per planet in the following format:
        label   <mass>  <x> <y> <z>    <vx> <vy> <vz>
        
        :param inputFile: Readable file handle in the above format

        :return Particle3D instance
        """
        CODE
        return Particle3D()


    @staticmethod
    def sys_kinetic(p3d_list):
        """
        FILL IN YOUR DOCSTRING COMMENT
        """
        CODE
        return sys_ke


    @staticmethod
    def com_velocity(_fill_in_the_blank_):
        """
        Computes the total mass and CoM velocity of a list of P3D's

        :param p3d_list: list in which each item is a P3D instance
        :return total_mass: The total mass of the system 
        :return com_vel: Centre-of-mass velocity
        """
        CODE
        return total_mass, com_vel


