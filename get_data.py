from bing_image_downloader import downloader

def download_images(request):
    print(request)
    downloader.download(request, limit=20, output_dir='dataset', adult_filter_off=False, force_replace=False, timeout=60)

    
pessoas = [
        'Jim Helpert',
        'Michael Scott',
        'Dwight Schrute',
        'Pam Beesly',
        'Ryan Howard',
        'Andy Bernard',
        'Kevin Malone',
        'Angela Martin',
        'Kelly Kapoor',
        'Oscar Martinez',
    ]

for pessoa in pessoas:
    download_images(pessoa + ' the office')