Ky projekt është një mjet për deshifrimin e teksteve të koduara duke përdorur analizën e frekuencës së shkronjave (frequency analysis). 
Programi merr një tekst hyrës nga përdoruesi, e përpunon atë duke ruajtur formatimin origjinal (hapësirat dhe shenjat e pikësimit), 
dhe analizon vetëm shkronjat për të përcaktuar sa shpesh shfaqet secila prej tyre.

Bazuar në këtë analizë, krijohet një renditje e shkronjave sipas frekuencës dhe krahasohet me frekuencën standarde të gjuhës angleze. 
Në këtë mënyrë gjenerohet automatikisht një zëvendësim fillestar (mapping), 
i cili përdoret për të prodhuar një version të parë të deshifruar të tekstit.

Projekti nuk ndalet vetëm te kjo fazë automatike. 
Ai përfshin edhe një sistem interaktiv që i lejon përdoruesit të modifikojë manualisht zëvendësimet (p.sh. A->M), 
duke përditësuar menjëherë rezultatin. 
Gjithashtu, programi menaxhon konfliktet në mapping (kur dy shkronja përpiqen të marrin të njëjtin zëvendësim), 
duke i rregulluar automatikisht për të ruajtur një zgjidhje të vlefshme.

Ky kombinim i analizës automatike dhe kontrollit manual e bën mjetin të dobishëm për:

zgjidhjen e substitution ciphers

ushtrime kriptografie

puzzle logjike dhe eksperimente me tekste të koduara

Startup

downloado ose git clone repon

brenda command prompt

cd deri tek repo siguri

dhe starto programin me komanden

python siguri.py

pas startimit vendose tekstin e enkriptuar dhe programi do te ndihmoj dhe me pas mund manualisht te nderrosh shkronjat e gabuara
