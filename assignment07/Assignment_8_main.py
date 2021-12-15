from tabulate import tabulate
import Assignment8Objects as ao


def main():
     package = ao.Booking()
     package.set_directory()
     package.display_menu_9()


     package.display_menu()
     package.generate_unique_id()
     package.display_menu_10()
     date = input()
     package.required_delivery_date(date)
     package.get_customer_name()
     package.package_description()
     package.display_menu_6()
     dangerous_contents = input()
     package.check_contents(dangerous_contents)
     weight = package.check_weight()
     length, width, height = package.get_dimensions()
     volume = package.get_volume(length, width, height)
     package.set_weight_boundaries(weight)
     package.set_dimension_boundaries(volume)
     shippable_package = package.determine_if_shippable(volume, weight)
     international_flag = package.determine_international()
     package.display_menu_2()
     urgency_selection = input()
     urgency = package.determine_urgency(urgency_selection)
     package.logistics_planning(shippable_package, international_flag, weight, volume, urgency)
     package.add_to_csv()
     package.display_menu_5()
     exit_1 = input()
     if exit_1 == '1':
       package.system_exit(True)
     if exit_1 == '0':
       main()


if __name__ == "__main__":

    main()