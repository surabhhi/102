import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.BJJmqe8ST9l36Cl9O-X4disnleP08JW20ZqB9mnwoUHIAuoPmBwP6OLrmzR9nLM5js34tcFqjYoaI3aBTYrm65cXh4pjetYY90ifPTFRRczJV7g7j9yjUBazp7OEkM2frys4RSg'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer: -")
    file_to = input("enter the full path to upload to dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
print("file has been moved")
if __name__ == '__main__':
    main()