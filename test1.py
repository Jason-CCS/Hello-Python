def remove_elements_from_list(target: list, removed_elems: list) -> list:
    # Enter your code here.
    for e in removed_elems:
        while target.count(e) > 0:
            target.remove(e)
    return target

print(remove_elements_from_list(['Apple', 'Tomato', 'Onion', 'Banana', 'Orange', 'Tomato'],
                                ['Tomato', 'Onion']))