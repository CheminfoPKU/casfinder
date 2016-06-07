def handleUploadFile(f):
    with open(f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)