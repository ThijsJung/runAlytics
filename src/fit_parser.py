from __future__ import print_function
import sys
import os
import decimal

import boto3

from fitparse import FitFile, FitParseError

def parse_fit_file(filename):
    try:
        fit_file = FitFile(filename)
    except FitParseError as e:
        print("Error while parsing .FIT file: %s" % e)
        raise e
    return fit_file

# class FITParser(object):
#     def __init__(self):
#         self.coordinates = list()
#         self.heart_rates = list()
#         self.distances = list()
#         self.timestamps = list()
#         self.run_id = None

#     def _
    
#     def get_run_id(self, fit_file):
#         file_id_data_message = next(fit_file.get_messages(name='file_id'))
#         creation_time = file_id_data_message.get_value('time_created')
#         if creation_time is not None:
#             return creation_time.isoformat()

#         # Who should know the filename? Not this method... And, raise exception?
#         # print("No creation time found. Check FIT file {}".format(filename))
#         return "No creation date found"
    

#     def parse(self, filename):
        

#         self.run_id = self.get_run_id(fit_file)

#         for record in fit_file.get_messages('record'):
#             self.coordinates.append(list([
#                 record.get_value('position_lat'),
#                 record.get_value('position_long')
#             ]))
#             self.heart_rates.append(record.get_value('heart_rate'))
#             self.distances.append(decimal.Decimal(
#                 str(record.get_value('distance'))))
#             self.timestamps.append(record.get_value('timestamp').isoformat())


# class Uploader(object):
#     def __init__(self, parser):
#         self.parser = parser
#         self.table = boto3.resource('dynamodb').Table(os.environ['RUNS_TABLE'])

#     def upload(self):
#         expression = "SET #timestamps = :timestamps, #heart_rates = :heart_rates, #distances = :distances, #coordinates = :coordinates"
#         names = {
#             '#timestamps': 'timestamps',
#             '#heart_rates': 'heart_rates',
#             '#distances': 'distances',
#             '#coordinates': 'coordinates'
#         }
#         values = {
#             ':timestamps': self.parser.timestamps,
#             ':heart_rates': self.parser.heart_rates,
#             ':distances': self.parser.distances,
#             ':coordinates': self.parser.coordinates
#         }

#         self.table.update_item(
#             Key={'run_id': self.parser.run_id},
#             UpdateExpression=expression,
#             ExpressionAttributeNames=names,
#             ExpressionAttributeValues=values
#         )

#     def run(self, filename):
#         self.parser.parse(filename)
#         print("Adding FIT file with run_id '{}'.".format(self.parser.run_id))
#         self.upload()
