import os

def format_attr_val(attr_val):
    if isinstance(attr_val, int) or isinstance(attr_val, str):
        return str(attr_val)
    elif isinstance(attr_val, list):
        return '{{ {0} }}'.format(' '.join(str(x) for x in attr_val))
    elif isinstance(attr_val, dict):
        dict_vals = []
        for key, val in attr_val.items():
            dict_vals.append('{0} = {1}'.format(key, val))
        return '{{ {0} }}'.format(' '.join(dict_vals))
    elif attr_val is None:
        return '{ }'
    else:
        raise Exception('Invalid attribute type', type(attr_val), attr_val)

def write_revolt_file(path, countries):
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    file = open(path, 'w+')
    for country_name, country_attrs in countries.items():
        file.write('{0} = {{\n'.format(country_name))
        for attr_name, attr_val in country_attrs.items():
            str_val = format_attr_val(attr_val)
            file.write('\t{0} = {1}\n'.format(attr_name, str_val))
        file.write('}\n')
    file.close()
