import requests

DATASETS = [
    ("HHSAV.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHSAV.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"),
    ("HHDI.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHDI.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"),
    ("HHEXP.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHEXP.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"),
    ("HHSAV.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHSAV.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"),
    ("HHDEBT.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHDEBT.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"),
    ("HHFA.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHFA.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"),
    ("HHFT.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHFT.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"),
    ("HHWEALTH.csv", "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.HHWEALTH.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en")
]
DATADIR = "datasets/"

if __name__ == "__main__":
    for filename, url in DATASETS:
        print("Downloading ")
        with requests.get(url) as request:
            with open(DATADIR + filename, 'wb') as file:
                file.write(request.content)