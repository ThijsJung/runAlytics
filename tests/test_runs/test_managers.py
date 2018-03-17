# class TestUploader(TestCase):

#     @patch('Uploader.table')
#     def test_upload(self, mock_table):
#         uploader = Uploader(FITParser())
#         uploader.run(FILENAME)
#         assert mock_table.update_item.call_count == 0
