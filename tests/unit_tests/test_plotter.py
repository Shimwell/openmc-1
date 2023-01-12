import openmc
import numpy as np


def test_calculate_cexs_elem_mat_sab():
    """Checks that sab cross sections are included in the
    _calculate_cexs_elem_mat method and have the correct shape"""

    mat_1 = openmc.Material()
    mat_1.add_element("H", 4.0, "ao")
    mat_1.add_element("O", 4.0, "ao")
    mat_1.add_element("C", 4.0, "ao")

    mat_1.add_s_alpha_beta("c_C6H6")
    mat_1.set_density("g/cm3", 0.865)

    energy_grid, data = openmc.plotter._calculate_cexs_elem_mat(
        mat_1,
        ["inelastic"],
        sab_name="c_C6H6",
    )

    assert isinstance(energy_grid, np.ndarray)
    assert isinstance(data, np.ndarray)
    assert len(energy_grid) > 1
    assert len(data) == 1
    assert len(data[0]) == len(energy_grid)
