import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'JnfMMed_zMoAAAAAAAAAAdRbOq7NvwfmPEFgGSxO2ZH_IDUc1Jz2cIh57fVPUu_1'
    transferData = TransferData(access_token)

    file_from = input('enter file path to transfer :')
    file_to = input('enter file path to upload :')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file moved successfully")
if __name__ == '__main__':
    main()