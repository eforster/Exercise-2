"""
 CompMod Ex2: Particle3D, a class to describe point particles in 3D space

 An instance describes a particle in Euclidean 3D space: 
 velocity and position are [3] arrays

 Includes time integrator methods + calculation methods + update methods

Author: E Forster, s1639706

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
    __init__ - initialises a particle in 3D space
    __str__ - sets up xyz of particle
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

    def __init__(self, label, mass, pos, vel):
        """
        Initialises a particle in 3D space

        :param label: String w/ the name of the particle
        :param mass: float, mass of the particle
        :param pos: [3] float array w/ position
        :param vel: [3] float array w/ velocity
        """
        self.label = label
        self.mass = mass
        self.pos = pos
        self.vel = vel


    def __str__(self):
        """
        XYZ-compliant string. The format is
        <label>    <x>  <y>  <z>

        :return xyz_string: (label, x, y, z)
        """
        xyz_string = str(self.label + "    " + self.pos[0] + "    " + self.pos[1] + "    " + self.pos[2])
        return xyz_string


    def kinetic_e(self):
        """
        Returns the kinetic energy of a Particle3D instance

        :return ke: float, 1/2 m v**2
        """
        ke = (1/2) * self.mass * (np.linalg.norm(self.vel) ** 2)
        return ke


    def momentum(self):
        """
        Calculates and returns the momentum of a particle

        :return p: returns momentum
        """
        p = self.mass * self.vel
        return p


    def update_pos(self, dt):
        """
        Calculates and updates the new position of a particle to 1st order

        :param dt: time-step
        """
        new_position = self.pos + dt * self.vel


    def update_pos_2nd(self, dt, force):
        """
        Calculates and updates the position of a particle to 2nd order

        :param dt: time-step
        :param force: force on particle
        """
        new_position = self.pos + dt * self.vel + (dt ** 2) * (force/(2 * self.mass))


    def update_vel(self, dt, force):
        """
        Updates the velocity of a particle to 1st order

        :param dt: time-step
        :param force: force on particle
        """
        new_velocity = self.vel + dt * (force/self.mass)


    @staticmethod
    def new_p3d(input_file):
        """
        Initialises a Particle3D instance given an input file handle.
        
        The input file should contain one line per planet in the following format:
        label   <mass>  <x> <y> <z>    <vx> <vy> <vz>
        
        :param input_file: Readable file handle in the above format

        :return Particle3D: instance label mass position velocity
        """
        data = input_file.readline()
        lines = data.split()

        label = str(lines[0])
        mass = float(lines[1])
        pos = np.array([lines[2], lines[3], lines[4]])
        vel = np.array([lines[5], lines[6], lines[7]])

        return Particle3D(label, mass, pos, vel)


    @staticmethod
    def sys_kinetic(p3d_list):
        """
        Returns the total kinetic energy of the system as a float

        :param p3d_list: list in which each item is a P3D instance

        :return sys_ke: sum of each particle's kinetic energy
        """

        sys_ke = 0

        for particle in p3d_list:

            ke = particle.kinetic_e()

            sys_ke += ke

        return sys_ke


    @staticmethod
    def com_velocity(p3d_list):
        """
        Computes the total mass and CoM velocity of a list of P3D's

        :param p3d_list: list in which each item is a P3D instance
        :return total_mass: The total mass of the system 
        :return com_vel: Centre-of-mass velocity
        """
        total_mass = 0
        com_vel = 0
        total = 0

        for particle in p3d_list:

            particle_mass = particle.mass
            total_mass += particle_mass


        for part in p3d_list :

            particle_vel = part.vel

            mass_x_vel = particle_mass * particle_vel
            total += mass_x_vel

            com_vel = total / total_mass

        return total_mass, com_vel
