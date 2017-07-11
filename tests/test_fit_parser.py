from unittest import TestCase
from mock import Mock, patch

from context import FITParser, Uploader

FILENAME = 'data/FIT/5C6F3721.FIT'

class TestParseFITFile(TestCase):
    def setUp(self):
        self.filename = 'data/FIT/5C6F3721.FIT'
        self.parser = FITParser()

    def test_parse_get_run_id(self):
        self.parser.parse(self.filename)
        assert self.parser.run_id == "2015-12-06T14:37:21"
    
    def test_get_run_id_none_found(self):
        self.parser.parse(self.filename)
        assert self.parser.run_id == "No creation date found"

# class TestUploader(TestCase):

    # @patch('Uploader.table')
    # def test_upload(self, mock_table):
    #     uploader = Uploader(FITParser())
    #     uploader.run(FILENAME)
    #     assert mock_table.update_item.call_count == 0
