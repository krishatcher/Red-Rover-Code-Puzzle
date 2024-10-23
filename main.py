"""
Red Rover
Applicant Code Challenge
"""

def orchestrator():
    """ Main function, coordinating all operations """
    INPUT_STRING = "(id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)"

    print("")
    print("Welcome!")
    print("String parsing into object model.")
    print("")
    print(f"Our source string is: \"{INPUT_STRING}\"")

    model_dict_unsorted = create_model(INPUT_STRING)
    print("")
    print("Our model, in the order it appears in the source string:")
    display_model(model_dict_unsorted, "")

    model_dict_sorted = order_model_alpha(model_dict_unsorted)
    print("")
    print("Our model, this time sorted alphabetically:")
    display_model(model_dict_sorted, "")

    print("")


def create_model(base: str) -> dict:
    """ Convert a string into a dictionary-based model """
    clean_base: str = base[1:-1]
    list_base: list[str] = clean_base.split(', ')
    result_dict: dict = {}
    skip_entries: bool = False

    for entry in list_base:
        if not skip_entries:
            if "(" in entry:
                skip_entries = True
                start_index: int = clean_base.find(entry)
                index_within_entry: int = entry.find("(")
                start_index += index_within_entry

                end_index: int = clean_base.rfind(")") + 1
                result_dict[entry.split("(")[0]] = create_model(clean_base[start_index:end_index])
            else:
                result_dict[entry] = {}
        else:
            if ")" in entry:
                skip_entries = False

    return result_dict


def display_model(model: dict, padding: str):
    """ Output a dictionary-based model to the screen """

    for key, value in model.items():
        print(f"{padding}- {key}")
        if value != {}:
            display_model(value, padding + "  ")


def order_model_alpha(model: dict) -> dict:
    """ Sort the passed-in dictionary-based model alphabetically """
    output: dict = {}

    output = dict(sorted(model.items()))

    for key, value in output.items():
        if value != {}:
            output[key] = order_model_alpha(value)

    return output


if __name__ == "__main__":
    orchestrator()
