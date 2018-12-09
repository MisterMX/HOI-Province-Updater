from revolt_reader import read_revolt_file
from revolt_writer import write_revolt_file
from province_reader import read_province_file_by_id, read_province_file_by_name

class HoiProvinceUpdater:
    def __init__(self, path_revolt_new, path_provinces_old, path_provinces_new):
        self.revolt = read_revolt_file(path_revolt_new)
        self.provinces_old = read_province_file_by_id(path_provinces_old)
        self.provinces_new = read_province_file_by_name(path_provinces_new)

    def find_new_province_id(self, old_id):
        old_province_name = self.provinces_old[old_id]
        if old_province_name in self.provinces_new:
            return self.provinces_new[old_province_name]
        else:
            return None

    def find_new_province_ids(self, old_ids):
        new_ids = []
        for old_id in old_ids:
            old_province_name = self.provinces_old[old_id]
            if old_province_name in self.provinces_new:
                new_ids.append(self.provinces_new[old_province_name])

        return new_ids

    def updateArrayIdAttribute(self, country_name, country_attrs, attr_name):
        if attr_name in country_attrs and country_attrs[attr_name] is not None:
            old_ids = country_attrs[attr_name]
            new_ids = self.find_new_province_ids(old_ids)
            country_attrs[attr_name] = new_ids

            skipped = len(old_ids) - len(new_ids)
            if skipped > 0:
                print('{0}.{1}: Skipped {2} not existing province(s)'.format(country_name, attr_name, skipped))

    def updateSingleIdAttribute(self, country_name, country_attrs, attr_name):
        if attr_name in country_attrs and country_attrs[attr_name] is not None:
            old_id = country_attrs[attr_name]
            new_id = self.find_new_province_id(old_id)
            country_attrs[attr_name] = new_id
            if new_id is None:
                print('{0}.{1}: Skipped not existing province'.format(country_name, attr_name))

    def updateProvince(self):
        for country_name, country_attrs in self.revolt.items():
            self.updateArrayIdAttribute(country_name, country_attrs, 'minimum')
            self.updateArrayIdAttribute(country_name, country_attrs, 'claims')
            self.updateArrayIdAttribute(country_name, country_attrs, 'extra')
            self.updateSingleIdAttribute(country_name, country_attrs, 'capital')

    def save(self, path):
        write_revolt_file(path, self.revolt)

updater = HoiProvinceUpdater('input/revolt_old.txt', 'input/province_names_old.csv', 'input/province_names_new.csv')
updater.updateProvince()
updater.save('output/revolt_updated.txt')
