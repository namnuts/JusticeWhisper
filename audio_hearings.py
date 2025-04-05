import requests
import os

def clean_url(url):
    return url.replace('..', '')

def download_audio(case_number, audio_url):
    try:
        full_url = clean_url(audio_url)
        print(f"Processing: {case_number} | Audio URL: {audio_url}")
        print(f"Full Audio URL: {full_url}")

        response = requests.get(full_url, stream=True)
        
        if response.status_code == 200:
            os.makedirs('downloads', exist_ok=True)
            file_path = os.path.join('downloads', f"{case_number}.mp3")
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded {case_number}.mp3 successfully!")
        else:
            print(f"Error downloading {case_number}.mp3: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {case_number}.mp3: {e}")

cases = [
    ("24-109", "https://www.supremecourt.gov/media/audio/mp3files/24-109.mp3"),
    ("23-1270", "https://www.supremecourt.gov/media/audio/mp3files/23-1270.mp3"),
    ("23-1229", "https://www.supremecourt.gov/media/audio/mp3files/23-1229.mp3"),
    ("23-1067", "https://www.supremecourt.gov/media/audio/mp3files/23-1067.mp3"),
    ("24-354", "https://www.supremecourt.gov/media/audio/mp3files/24-354.mp3"),
    ("24-154", "https://www.supremecourt.gov/media/audio/mp3files/24-154.mp3"),
    ("23-1345", "https://www.supremecourt.gov/media/audio/mp3files/23-1345.mp3"),
    ("24-20", "https://www.supremecourt.gov/media/audio/mp3files/24-20.mp3"),
    ("23-1275", "https://www.supremecourt.gov/media/audio/mp3files/23-1275.mp3"),
    ("23-7809", "https://www.supremecourt.gov/media/audio/mp3files/23-7809.mp3"),
    ("23-7483", "https://www.supremecourt.gov/media/audio/mp3files/23-7483.mp3"),
    ("23-1324", "https://www.supremecourt.gov/media/audio/mp3files/23-1324.mp3"),
    ("23-1039", "https://www.supremecourt.gov/media/audio/mp3files/23-1039.mp3"),
    ("23-1201", "https://www.supremecourt.gov/media/audio/mp3files/23-1201.mp3"),
    ("23-1259", "https://www.supremecourt.gov/media/audio/mp3files/23-1259.mp3"),
    ("23-1141", "https://www.supremecourt.gov/media/audio/mp3files/23-1141.mp3"),
    ("23-1300", "https://www.supremecourt.gov/media/audio/mp3files/23-1300.mp3"),
    ("24-656", "https://www.supremecourt.gov/media/audio/mp3files/24-656.mp3"),
    ("23-1002", "https://www.supremecourt.gov/media/audio/mp3files/23-1002.mp3"),
    ("23-997", "https://www.supremecourt.gov/media/audio/mp3files/23-997.mp3"),
    ("23-1095", "https://www.supremecourt.gov/media/audio/mp3files/23-1095.mp3"),
    ("23-971", "https://www.supremecourt.gov/media/audio/mp3files/23-971.mp3"),
    ("23-1122", "https://www.supremecourt.gov/media/audio/mp3files/23-1122.mp3"),
    ("23-1187", "https://www.supremecourt.gov/media/audio/mp3files/23-1187.mp3"),
    ("23-1226", "https://www.supremecourt.gov/media/audio/mp3files/23-1226.mp3"),
    ("23-1239", "https://www.supremecourt.gov/media/audio/mp3files/23-1239.mp3"),
    ("23-1007", "https://www.supremecourt.gov/media/audio/mp3files/23-1007.mp3"),
    ("23-1038", "https://www.supremecourt.gov/media/audio/mp3files/23-1038.mp3"),
    ("23-824", "https://www.supremecourt.gov/media/audio/mp3files/23-824.mp3"),
    ("23-867", "https://www.supremecourt.gov/media/audio/mp3files/23-867.mp3"),
    ("23-477", "https://www.supremecourt.gov/media/audio/mp3files/23-477.mp3"),
    ("23-909", "https://www.supremecourt.gov/media/audio/mp3files/23-909.mp3"),
    ("23-861", "https://www.supremecourt.gov/media/audio/mp3files/23-861.mp3"),
    ("23-975", "https://www.supremecourt.gov/media/audio/mp3files/23-975.mp3"),
    ("23-900", "https://www.supremecourt.gov/media/audio/mp3files/23-900.mp3"),
    ("23-1127", "https://www.supremecourt.gov/media/audio/mp3files/23-1127.mp3"),
    ("23-715", "https://www.supremecourt.gov/media/audio/mp3files/23-715.mp3"),
    ("23-217", "https://www.supremecourt.gov/media/audio/mp3files/23-217.mp3"),
    ("23-980", "https://www.supremecourt.gov/media/audio/mp3files/23-980.mp3"),
    ("23-929", "https://www.supremecourt.gov/media/audio/mp3files/23-929.mp3"),
    ("23-825", "https://www.supremecourt.gov/media/audio/mp3files/23-825.mp3"),
    ("23-970", "https://www.supremecourt.gov/media/audio/mp3files/23-970.mp3"),
    ("23-191", "https://www.supremecourt.gov/media/audio/mp3files/23-191.mp3"),
    ("23-677", "https://www.supremecourt.gov/media/audio/mp3files/23-677.mp3"),
    ("23-852", "https://www.supremecourt.gov/media/audio/mp3files/23-852.mp3"),
    ("23-621", "https://www.supremecourt.gov/media/audio/mp3files/23-621.mp3"),
    ("22-7466", "https://www.supremecourt.gov/media/audio/mp3files/22-7466.mp3"),
    ("23-365", "https://www.supremecourt.gov/media/audio/mp3files/23-365.mp3"),
    ("23-583", "https://www.supremecourt.gov/media/audio/mp3files/23-583.mp3"),
    ("23-713", "https://www.supremecourt.gov/media/audio/mp3files/23-713.mp3"),
    ("23-753", "https://www.supremecourt.gov/media/audio/mp3files/23-753.mp3"),
]

for case_number, audio_url in cases:
    download_audio(case_number, audio_url)

print("Download process completed.")
