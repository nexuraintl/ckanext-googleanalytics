def get_visits_for_resource(id):
    from ckanext.googleanalytics.model import ResourceStats

    return ResourceStats.get_all_visits(id)


def get_visits_for_dataset(id):

    from ckanext.googleanalytics.model import PackageStats

    return PackageStats.get_all_visits(id)