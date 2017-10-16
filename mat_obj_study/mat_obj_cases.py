from pyne.material import Material
import argparse
import timeit

zaid_act = [
    90230, 90231, 90232, 90233, 90234, 91231, 91232, 91233, 92233, 92234,\
    92235, 92236, 92237, 92238, 92239, 92240, 93235, 93236, 93237, 93238,\
    93239, 94236, 94237, 94238, 94239, 94240, 94241, 94242]

zaid_nonact = [
    1001, 1002, 1003, 2003, 2004, 3006, 4009, 5010, 5011, 6012,\
    6013, 7014, 7015, 8016, 8017, 33074, 33075, 35079, 35081, 36078,\
    36080, 36082, 36083, 36084, 36086, 37085, 37087, 38086, 38087, 38088,\
    39088, 39089, 39090, 39091, 40090, 40091, 40092, 40093, 40094, 40095,\
    40096, 41093, 41094, 41095, 42092, 42094, 42095, 42096, 42097, 42098,\
    42099, 42100, 43099, 44101, 44103, 45103, 46102, 46104, 46105, 46106,\
    46108, 46110, 47107, 47109, 48106, 48108, 48110, 48111, 48112, 48113,\
    50120, 53127, 53129, 53135, 54124, 54126, 54129, 54130, 54131, 54132,\
    54134, 54135, 54136, 55133, 55134, 55135, 55136, 55137, 56138, 59141,\
    60143, 60145, 60147, 60148, 61147, 61148, 61149, 62147, 62149, 62150,\
    62151, 62152, 63151, 64152, 64154, 64155, 64156, 64157, 64158, 64160,\
    66158, 66160, 66161, 66162, 66163, 66164, 67165, 68162, 68164, 68166,\
    68167, 68168, 68170, 69169, 71175, 71176, 72174, 72176, 72177, 72178,\
    72179, 72180, 73181, 73182, 74182, 74183, 74184]


def make_dict_return_dict():
    """Make dictionary, return dictionary.

    Populate dictionaries with data, return dictionaries.

    Arguments:
        None.

    Returns:
        mat: Dictionary of (material number: (data dictionary)).
    """
    mat = {}
    for mat_num in mat_num_list:
        # Defining as dictionaries.
        act = {}
        nonact = {}
        # Processing as dictionaries.
        for idx, zaid in enumerate(sorted(zaid_act), start=1):
            act[zaid] = float(idx)
        for idx, zaid in enumerate(sorted(zaid_nonact), start=len(zaid_act)+1):
            nonact[zaid] = float(idx)
        # Returning as dictionaries.
        mat[mat_num] = {'actinide': act,
                        'nonactinide': nonact}

    return mat


def make_dict_return_obj():
    """Make dictionary, return Material objects.

    Populate dictionaries with data, make Material object from the dictionaries,
    return the objects.

    Arguments:
        None.

    Returns:
        mat: Dictionary of (material number: (data dictionary)).
    """
    mat = {}
    for mat_num in mat_num_list:
        # Defining as dictionaries.
        act = {}
        nonact = {}
        # Processing as dictionaries.
        for idx, zaid in enumerate(sorted(zaid_act), start=1):
            act[str(zaid)+'0000'] = idx
        for idx, zaid in enumerate(sorted(zaid_nonact), start=len(zaid_act)+1):
            nonact[str(zaid)+'0000'] = idx
        # Returning as PyNE material objects made with dictionaries.
        mat[mat_num] = {'actinide': Material(act),
                        'nonactinide': Material(nonact)}

    return mat


def make_empty_obj_return_obj():
    """Make emtpy Material object, return Material objects.

    Make empty Material object, populate the objects with data,
    return the objects.

    Arguments:
        None.

    Returns:
        mat: Dictionary of (material number: (data dictionary)).
    """
    mat = {}
    for mat_num in mat_num_list:
        # Defining as PyNE material objects.
        # No initialization.
        act = Material()
        nonact = Material()
        # Processing as PyNE material objects - adding key-value pair.
        # Size of material object increases.
        for idx, zaid in enumerate(sorted(zaid_act), start=1):
            act[str(zaid)+'0000'] = idx
        for idx, zaid in enumerate(sorted(zaid_nonact), start=len(zaid_act)+1):
            nonact[str(zaid)+'0000'] = idx
        # Returning as PyNE material objects.
        mat[mat_num] = {'actinide': act,
                        'nonactinide': nonact}

    return mat

def make_filled_obj_return_obj():
    """Make filled Material object, return Material objects.

    Initialize Material object with (zaid: 0.0), populate the objects with data,
    return the objects.

    Arguments:
        None.

    Returns:
        mat: Dictionary of (material number: (data dictionary)).
    """
    mat = {}

    draft_act = {}
    draft_nonact = {}
    for zaid in zaid_act:
        draft_act[str(zaid)+'0000'] = 0.0
    for zaid in zaid_nonact:
        draft_nonact[str(zaid)+'0000'] = 0.0

    for mat_num in mat_num_list:
        # Initialized as PyNE material objects with draft dictionaries.
        act = Material(draft_act)
        nonact = Material(draft_nonact)
        # Processing as PyNE material objects - re-assigning value.
        # Size of material object remains unchanged.
        for idx, zaid in enumerate(sorted(zaid_act), start=1):
            act[str(zaid)+'0000'] = idx
        for idx, zaid in enumerate(sorted(zaid_nonact), start=len(zaid_act)+1):
            nonact[str(zaid)+'0000'] = idx
        # Returning as PyNE material objects.
        mat[mat_num] = {'actinide': act,
                        'nonactinide': nonact}

    return mat


def write_dict(mat):
    """Write string with dicionary key, values.

    Note: Normalization is unabled with this method.

    Arguments:
        mat: Dictionary of (material number: (data dictionary)).

    Returns:
        inp: String to be written.
    """

    inp = ''
    for mat_num in sorted(mat):
        inp += 'm{0}\n'.format(mat_num)
        series_mat = mat[mat_num]
        for zaid, frac in sorted(series_mat['nonactinide'].items()):
            inp += '     {0:<5} -{1:.3e}\n'.format(zaid, frac)
        for zaid, frac in sorted(series_mat['actinide'].items()):
            inp += '     {0:<5} -{1:.3e}\n'.format(zaid, frac)
    return inp


def write_obj(mat):
    """Write string with Material objects.

    Using .mcnp() method, compositions will be automatically normalized.

    Arguments:
        mat: Dictionary of (material number: (data dictionary)).

    Returns:
        inp: String to be written.
    """
    inp = ''
    for mat_num in sorted(mat):
        # Add two material objects to use .mcnp() method once.
        mat_obj = mat[mat_num]['actinide'] + mat[mat_num]['nonactinide']
        mat_obj.metadata['mat_number'] = mat_num
        inp += mat_obj.mcnp()
    return inp


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Test timing for \
material object utilization")
    parser.add_argument("case", type=str, choices=['dict_dict',
                                                   'dict_obj',
                                                   'empty_obj',
                                                   'filled_obj'],
                        help="Cases to be compared.")
    parser.add_argument("-n", "--num_mat", type=int, default=1500,
                        help="Number of materials to be made. \
Default: 1500.")
    args = parser.parse_args()

    mat_num_list = range(1000, args.num_mat + 1000)
    make_func = {
        'dict_dict': make_dict_return_dict,
        'dict_obj': make_dict_return_obj,
        'empty_obj': make_empty_obj_return_obj,
        'filled_obj': make_filled_obj_return_obj}
    write_func = {
        'dict_dict': write_dict,
        'dict_obj': write_obj,
        'empty_obj': write_obj,
        'filled_obj': write_obj}

    inp_str = ''

    start_make = timeit.default_timer()
    mat = make_func[args.case]()
    end_make = timeit.default_timer()

    start_write = timeit.default_timer()
    inp_str += write_func[args.case](mat)
    end_write = timeit.default_timer()

    make_time = end_make - start_make
    write_time = end_write - start_write

    ifile = open("{0}_mat.txt".format(args.case), 'w')
    ifile.write("Case: {0}\nMake time: {1}\nWrite time: {2}\n\n\
{3}".format(args.case, make_time, write_time, inp_str))
    ifile.close()
