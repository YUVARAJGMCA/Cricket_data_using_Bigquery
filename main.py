from google.cloud import storage

storage_bucket = "circket_datas"
path_fil1 = "T20 World Cup 2009 matches.csv"
path_file2 = "T20 World Cup 2010 matches.csv"
path_file3= "T20 World Cup 2012 matches.csv"
path_file4 = "T20 World Cup 2014 matches.csv"
path_file5 = "T20 World Cup 2016 matches.csv"
path_file6 = "T20 World Cup 2021 matches.csv"

storage_client = storage.Client()
storage_buc = storage_client.bucket(storage_bucket)
blob = storage_buc.blob(path_fil1)
blob.upload_from_filename(path_fil1)

print(f"from the {path_fil1} uploaded to {storage_bucket}")

for datas in (path_file2,path_file3,path_file4,path_file5,path_file6):
    storage_client = storage.Client()
    storage_buc = storage_client.bucket(storage_bucket)
    blob = storage_buc.blob(datas)
    blob.upload_from_filename(datas)
print(f"from the {datas} uploaded to {storage_bucket}")