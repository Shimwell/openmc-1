from typing import Iterable

import numpy as np

from .checkvalue import check_length


class BoundingBox(tuple):
    """Axis-aligned bounding box.

    .. versionadded:: 0.13.4

    Parameters
    ----------
    lower_left : iterable of float
        The x, y, z coordinates of the lower left corner of the bounding box in [cm]
    upper_right : iterable of float
        The x, y, z coordinates of the upper right corner of the bounding box in [cm]

    Attributes
    ----------
    center : numpy.ndarray
        x, y, z coordinates of the center of the bounding box in [cm]
    lower_left : numpy.ndarray
        The x, y, z coordinates of the lower left corner of the bounding box in [cm]
    upper_right : numpy.ndarray
        The x, y, z coordinates of the upper right corner of the bounding box in [cm]
    volume : float
        The volume of the bounding box in [cm^3]
    width : {'x', 'y', 'z'}
        The width of the specified axis
    """

    def __new__(cls, lower_left: Iterable[float], upper_right: Iterable[float]):
        check_length("lower_left", lower_left, 3, 3)
        check_length("upper_right", upper_right, 3, 3)
        lower_left = np.array(lower_left, dtype=float)
        upper_right = np.array(upper_right, dtype=float)
        return tuple.__new__(cls, (lower_left, upper_right))

    def __repr__(self) -> str:
        return "BoundingBox(lower_left={}, upper_right={})".format(
            tuple(self.lower_left), tuple(self.upper_right))

    @property
    def center(self) -> np.ndarray:
        return (self[0] + self[1]) / 2

    @property
    def lower_left(self) -> np.ndarray:
        return self[0]

    @property
    def upper_right(self) -> np.ndarray:
        return self[1]

    @property
    def volume(self) -> float:
        return np.abs(np.prod(self[1] - self[0]))

    def width(self, axis: str):
        """The width of the specified axis

        Parameters
        ----------
        width : {'x', 'y', 'z'}
            The width of the specified axis

        Returns
        -------
        width : float
            width of axis
        """
        index = {'x': 0, 'y': 1, 'z': 2}[axis]
        return abs((self.lower_left - self.upper_right)[index])
