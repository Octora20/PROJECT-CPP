import time

lirik_waktu = [
    ("Seize the day or die regretting the time you lost", 4),
    ("It's empty and cold without you here, too many people to ache over", 9),
    ("Trials in life, questions of us existing here", 5),
    ("Don't wanna die alone without you here", 3),
    ("Please tell me what we have is real", 5)
]

for lirik, waktu in lirik_waktu:
    print(lirik)
    time.sleep(waktu)