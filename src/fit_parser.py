import sys
import os

import boto3

from fitparse import FitFile, FitParseError

class FITParser(object):
    def __init__(self):
        self.coordinates = list()
        self.heart_rate = list()
        self.distance = list()
        self.timestamp = list()

    def parse(self, filename):
        try:
            data = FitFile(filename).parse()
        except FitParseError, e:
            print "Error while parsing .FIT file: %s" % e
            sys.exit(1)

        for record in data:
            self.coordinates.append((
                record.get_value('position_lat'),
                record.get_value('position_long')))
            self.heart_rate.append(record.get_value('heart_rate'))
            self.distance.append(record.get_value('distance'))
            self.timestamp.append(record.get_value('timestamp'))



class Uploader(object):
    def __init__(self):
        self.parser = FITParser()
        self.dynamodb = boto3.resource('dynamodb').Table(os.environ['RUNS_TABLE'])

    def upload(self):
        pass



    def run(self, filename):
        self.parser.parse(filename)
