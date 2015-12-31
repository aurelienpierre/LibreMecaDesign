# -*- coding: utf-8 -*-
"""
Define aliases and equivalences
"""

import quantities as u

# Map SI multiples and sub-multiples
multiples = {
                'n': '* 1E-9',
                'µ': '* 1E-6',
                'm': '* 1E-3',
                # No mutliple
                'k': '* 1E+3',
                'M': '* 1E+6',
                'G': '* 1E+9',
                'T': '* 1E+12'
             }

# Map units strings with Quantities package's units
units = {
                # Force
                'mN': u.N * u.milli,
                'N': u.N,
                'kN': u.N * u.kilo,
                'MN': u.N * u.mega,
                # Pressure
                'Pa': u.Pa,
                'kPa': u.Pa * u.kilo,
                'MPa': u.Pa * u.mega,
                'GPa': u.Pa * u.giga,
                # Length
                'µm': u.m * u.micro,
                'mm': u.mm,
                'cm': u.m * u.centi,
                'm': u.m,
                'km': u.m * u.kilo,
                # Surface
                'm^2': u.m**2,
                'm²': u.m**2,
                # Volume
                'm^3': u.m**3,
                'm³': u.m**3,
                # Weigth
                'kg': u.kg,
                # Moments
                'mm^4': u.mm**4,
                'mm⁴': u.mm**4,
                'm^4': u.m**4,
                'm⁴': u.m**4,
                # Temperature
                '°C': u.C,
                'K': u.K,
        }

# Map usual names and aliases of materials properties with their symbol
materials_names = {
                'E': [
                       "modulus of elasticity",
                       "Young's modulus"
                       ],
                'G': [
                      "modulus of rigidity"
                      ],
                'nu': [
                       "Poisson's ratio"
                       ],
                'rho': [
                        "Volumic mass",
                        "Density"
                        ],
                'S_y': [
                        "tensile yield strength at 0.2% offset"
                        ],
                'S_ut': [
                         "ultimate tensile strength"
                         ],
                'alpha': [
                          "thermal expansion coefficient"
                          ],
                'HB': [
                       "Brinell hardness"
                       ],
                'HRC': [
                        "Rockwell C hardness"
                        ],
                'HRB': [
                        "Rockwell B hardness"
                        ],
                'S_f': [
                        "fatigue strength at 5E8 cycles"
                        ]
                    }

# Maps materials properties units and their symbol
materials_units = {
                'E': 'GPa',
                'G': 'GPa',
                'nu': 'none',
                'rho': 'kg/m^3',
                'S_y': 'MPa',
                'S_ut': 'MPa',
                'alpha': 'µ/°C',
                'HB': 'none',
                'HRC': 'none',
                'HRB': 'none',
                'S_f': 'MPa'
                    }

if __name__ == '__main__':
    print(multiples)
    print(units)
    print(materials_names)
    print(materials_units)
