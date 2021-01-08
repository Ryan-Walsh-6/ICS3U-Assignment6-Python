#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program calculates the volume of a hexagonal prism

import math


def calculate_volume(base_edge, height):
    # calculates volume

    # process & output
    volume_of_hexagonal_prism = ((3 * (math.sqrt(3))) / 2 * (base_edge) ** 2 *
                                 (height))

    return volume_of_hexagonal_prism


def main():
    # this program calculates the volume of a hexagonal prism

    while True:
        try:
            base_edge_from_user = input("Enter the base edge of the hexagonal"
                                        "prism (cm):")
            base_edge_from_user = float(base_edge_from_user)
            height_from_user = input("Enter the height of the hexagonal"
                                     "prism (cm):")
            print("\n", end="")
            height_from_user = float(height_from_user)
            if base_edge_from_user < 0 or height_from_user < 0:
                print("Please ensure all values are positive.")
                print("\n", end="")
            else:
                break
        except Exception:
            print("Please enter a valid number.")
            print("\n", end="")

    # call function
    volume = calculate_volume(base_edge_from_user, height_from_user)

    print("The volume of a hexagonal prism with a base edge of {0}cm and a"
          " height of {1}cm is {2:,.2f}cm³".format(base_edge_from_user,
                                                   height_from_user, volume))


if __name__ == "__main__":
    main()
