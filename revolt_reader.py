import re

def parse_date(str):
    matches = re.finditer('\w+\s*=\s*\w+', str)

    date_attrs = {}
    for match in matches:
        split = re.split('\s*=\s*', match.group(0), maxsplit=1)
        date_attrs[split[0]] = split[1]

    return date_attrs

def parse_int_array(str):
    matches = re.finditer('\d+', str)

    array = []
    for match in matches:
        num = int(match.group(0))
        array.append(num)

    return array

def parse_str_array(str):
    matches = re.finditer('\w+', str)

    array = []
    for match in matches:
        array.append(match.group(0))

    return array

def parse_int(str):
    return int(re.match('\d+', str).group(0))

def parse_country_attrs(str):
    attr_matches = re.finditer('\w+\s*=\s*({[\s\w=]*}|[\w=]+)', str)

    attrs = {}
    for attr_match in attr_matches:
        attr_split = re.split('\s*=\s*', attr_match.group(0), maxsplit=1)
        attr_name = attr_split[0]
        attr_value = None
        # Date
        if re.match('{(\s*\w+\s*=\s*\w+\s*)*}', attr_split[1]) is not None:
            attr_value = parse_date(attr_split[1])
        # Integer array
        elif re.match('{(\s*\d+\s*)+}', attr_split[1]) is not None:
            attr_value = parse_int_array(attr_split[1])
        # String array
        elif re.match('{(\s*\w+\s*)+}', attr_split[1]) is not None:
            attr_value = parse_str_array(attr_split[1])
        # Empty object
        elif re.match('{\s*}', attr_split[1]) is not None:
            attr_value = None
        # Integer
        elif re.match('\d+', attr_split[1]) is not None:
            attr_value = parse_int(attr_split[1])
        # String
        elif re.match('\w+', attr_split[1]) is not None:
            attr_value = attr_split[1]
        else:
            raise Exception('Invalid attribute value' , attr_split[1])

        attrs[attr_name] = attr_value

    return attrs

def prune_comments(str):
    return re.sub('#.*', ' ', str)

def parse_country(str):
    matches = re.finditer('\w+\s*=\s*{([^{}]|{[^{}]*})*}', str)

    countries = {}
    for match in matches:
        split = re.split('\s*=\s*', match.group(0), maxsplit=1)
        country_name = split[0]
        countries[country_name] = parse_country_attrs(split[1])

    return countries

def read_revolt_file(path):
    revolt_file = open(path, 'r')

    removed_comments = prune_comments(revolt_file.read())
    countries = parse_country(removed_comments)

    revolt_file.close()
    return countries
