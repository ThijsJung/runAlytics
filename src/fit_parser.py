from collections import defaultdict
import sys

from fitparse import FitFile, FitParseError

from runs.models import Run


def open_file(filename):
    """
    Tries to open a given file and return a FitFile object.

    Return:
        FitFile object or None (in case of error)
    """
    try:
        fit_file = FitFile(filename)
    except FitParseError as e:
        print("Error while parsing .FIT file: %s" % e)
        return

    return fit_file


def get_creation_timestamp(fit_file):
    """
    Extracts the time_created field from a fit file

    Returns:
        ISO formatted datetime string or None (if field not present)
    """
    fit_file_metadata = next(fit_file.get_messages(name='file_id'))
    metadata_timestamp = fit_file_metadata.get_value('time_created')

    return metadata_timestamp.isoformat()


def semicirle_to_coordinates(semicircle):
    return semicircle * (180/2**31)


def extract_data(fit_file):
    data = defaultdict(list)
    for record in fit_file.get_messages('record'):
        # Extract geocoordinates
        lat = record.get_value('position_lat')
        long = record.get_value('position_long')
        data['coordinates'].append(
            (semicirle_to_coordinates(lat),
             semicirle_to_coordinates(long))
        )

        # Extract heart rates
        data['heart_rates'].append(record.get_value('heart_rate'))

        # Extract distances ran
        data['distances'].append(record.get_value('distance'))

        # Extract timestamps
        timestamp = record.get_value('timestamp')
        data['timestamps'].append(timestamp.isoformat())

    return data


def parse_fit_file(filename):
    fit_file = open_file(filename)
    if fit_file is None:
        return

    created_at = get_creation_timestamp(fit_file)
    data = extract_data(fit_file)

    return dict(
        created_at=created_at,
        data=data
    )
