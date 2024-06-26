from google.cloud import storage

storage_bucket = "circket_datas"
path_fil1 = "test.json"
path_file2 = "udf.js"


for datas in (path_fil1,path_file2):
    storage_client = storage.Client()
    storage_buc = storage_client.bucket(storage_bucket)
    blob = storage_buc.blob(datas)
    blob.upload_from_filename(datas)
print(f"from the {datas} uploaded to {storage_bucket}")