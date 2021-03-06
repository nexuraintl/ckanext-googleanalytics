from ckan.plugins import toolkit
from ckanext.googleanalytics import model

from datetime import datetime

@toolkit.side_effect_free
def most_visited_packages(context, data_dict):

    start_date = data_dict.get('start_date', None)
    end_date = data_dict.get('end_date', None)

    dataset_type = data_dict.get('type', 'dataset')
    if start_date:
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
    if end_date:
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

    result = model.PackageStats.get_top(start_date=start_date, end_date=end_date, dataset_type=dataset_type)
    packages = []

    for package in result['packages']:
        package_with_extras = toolkit.get_action('package_show')(context, { 'id': package['package_id'] })
        package_with_extras['visits'] = package['visits']
        package_with_extras['visit_date'] = package['visit_date']
        packages.append(package_with_extras)

    from operator import itemgetter
    result['packages'] = sorted(packages, key=itemgetter('visits'), reverse=True)
    return result
